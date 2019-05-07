
from pydub import AudioSegment

main = AudioSegment.from_wav("/home/loopsun/code/Python/Poetryboy/src/audio/hts0000fbce@dx2873102cf9896f2300.wav")

bgm = AudioSegment.from_mp3("/home/loopsun/code/Python/Poetryboy/src/audio/bgm1.mp3")


combined = main.overlay(bgm)

combined.export("/home/loopsun/code/Python/Poetryboy/src/audio/out.wav", format='wav')
