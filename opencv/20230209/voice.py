from gtts import gTTS

text = 'hello'

tts = gTTS(text, lang='vi')

tts.save('hello.mp3')


