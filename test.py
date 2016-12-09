import guessit
import os

for file in os.listdir('/home/dadi15/Github/TEST'):
    print(guessit.guessit(file))