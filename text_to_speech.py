# TTS (Text To Speech)
# STT (Speech To Text)

import os
from gtts import gTTS
from playsound import playsound

# text = 'Imagine that you have just arrived at a hotel after a tiring 7-hour overnight flight.'
# file_name = 'sample.mp3'
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name)
# playsound(file_name)

file_name = 'play_now.mp3'

# text = '안녕하세요, 저는 에이오러스 인공지능 스피커입니다.'
# tts_ko = gTTS(text=text, lang='ko')
# tts_ko.save(file_name)
# playsound(file_name)

with open('play_now.txt', 'r', encoding='utf8') as f:
    text = f.read()

tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)
playsound(file_name)
