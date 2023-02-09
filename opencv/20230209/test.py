from gtts import gTTS

# text = '初めまして。私はズンと申しま、ベトナムハノイから参りました。よろしくお願いいたします。'

text = 'Hello every body. I am Dung I live in the small town the next to capital Hanoi'
tts = gTTS(text, lang='ja')
tts.save('kadai1.mp3')


