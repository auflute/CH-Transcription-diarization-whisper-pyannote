import whisper

model = whisper.load_model("base")
result = model.transcribe("audio4p_short.mp3")
print(result["text"])