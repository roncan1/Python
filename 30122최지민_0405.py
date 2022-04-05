from gtts import gTTS
import playsound
myText = '''Good time chillin' good time roll
    각자 좋은 시간들 have some toast
    기분은 즐기면 더 오래가
    이런 느낌은 오랜만
    I never thought that I would be here
    매일 내게 되물었었지 (What?)
    Can I be real?'''
    
tts = gTTS(text = myText, lang='ko')
fileNmae = "30122tts.mp3"
tts.save(fileNmae)
playsound.playsound("30122tts.mp3")