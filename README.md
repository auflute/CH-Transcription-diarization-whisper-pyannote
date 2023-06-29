# CH-Transcription-diarization-whisper-pyannote
修复原作者的代码的一些bug，同时支持对中文语音的多角色识别和语音转文本<p>
Transcription and diarization (speaker identification). Fix bugs from the original repo and support language detection.

# Install

Refer to the demo video of the original author of the code :<p>
https://www.youtube.com/watch?v=Wn2avfPZiSw

For Pyannote you must register on huggingface website to get the access token.
Support me by subscribing to my channel and leave a like.

Github repository for the source code:<p>
https://github.com/Mastering-Python-GT/Transcription-diarization-whisper-pyannote

OpenAi github link :<p>
https://github.com/openai/whisper

Pyannote github link :<p>
https://github.com/pyannote/pyannote-audio

Pydub github link :<p>
https://github.com/jiaaro/pydub

Recommend to use python anaconda to create development environment.
Then install whisper openai ,after installing this library run a simple test to check if everything works correctly.
Then install pyannote library and also run a simple test.
You can use the test files under the "test" directory.

For optimal output quality, the default whisper model is "large-v2". However, if you want a faster download and testing process, you can switch to the "tiny" or "base" models. Alternatively, you can download the model files beforehand and store them in the local folder.<p>
The Whisper models are stored in ~/.cache/whisper. (The Whisper.cpp models are stored in ~/Library/Caches/Buzz (Mac OS), ~/.cache/Buzz (Unix), or C:\Users\<username>\AppData\Local\Buzz\Buzz\Cache (Windows). The Hugging Face models are stored in ~/.cache/huggingface/hub. The Whisper.cpp and Hugging Face models are not used in this repo.)

