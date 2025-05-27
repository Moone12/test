import speech_recognition as sr
audio_file = './a.wav'
r = sr.Recognizer()
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)
# 识别音频文件
result = r.recognize_sphinx(audio, language="zh-CN")
print(result)