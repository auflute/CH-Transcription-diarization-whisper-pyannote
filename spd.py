from pyannote.audio import Pipeline
from pydub import AudioSegment
import whisper
import numpy as np
import gc
import re
from pywhispercpp.model import Model
import datetime
import os


pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization", use_auth_token="")


#def read(k):
#    y = np.array(k.get_array_of_samples())
#    return np.float32(y) / 32768


def millisec(timeStr):
    spl = timeStr.split(":")
    return (int)((int(spl[0]) * 60 * 60 + int(spl[1]) * 60 + float(spl[2])) * 1000)



k = str(pipeline(
    "audio4p_short.mp3")).split('\n')

del pipeline
gc.collect()

audio = AudioSegment.from_mp3(
    "audio4p_short.mp3")
#audio = audio.set_frame_rate(16000)

model = whisper.load_model("large-v2")
#model = Model('base', n_threads=6)

# 获取当前时间并格式化为字符串
current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 构造带有时间后缀和输出路径的文件名
file_name = os.path.join("output", f"tr_file_{current_time}.txt")

for l in range(len(k)):

    #j = k[l].split(" ")
    pattern = r"\[ (\d\d:\d\d:\d\d\.\d\d\d) -->  (\d\d:\d\d:\d\d\.\d\d\d)\] ([A-Z]) (\w+)"
    match = re.search(pattern, k[l])
    if match:
        j = [match.group(1), match.group(2), match.group(3), match.group(4)]
        print("j is",j)
    else:
        print("No match found")


    start = int(millisec(j[0]))
    end = int(millisec(j[1]))
  
    segment = audio[start:end]
    #tr = read(audio[start:end])

    segment.export("audio_temp.mp3", format="mp3")
    
    prompt = "这是一段关于科技话题的播客节目。光是什么？光是活着就已经筋疲力尽了。读完《三体》的那个下午，我遇到了“外卖叶文洁”, 明明备注“不要打电话！不要打电话！！不要打电话！！！”结果还是打了。"
    
    result = model.transcribe(
    "audio_temp.mp3",
    fp16=False,
    temperature=0.2,
    #language='zh',
    verbose=True,
    initial_prompt=prompt
)
    print("result is",result["text"])

    # 打开文件并写入内容
    with open(file_name, "a") as f:
        f.write(f'\n[ {j[0]} -- {j[1]} ] {j[3]} : {result["text"]}')

    # f = open("tr_file.txt", "a")
    # f.write(f'\n[ {j[0]} -- {j[1]} ] {j[3]} : {result["text"]}')
    # f.close()

    del f
    del result
    #del tr
    del j
    gc.collect()
