import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone(device_index=0) as soure:
    print('recording...')
    audio = r.listen(soure)
text = r.recognize_google(audio, language='en')
print(text)
