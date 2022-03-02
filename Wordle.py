import numpy as np
import random 
filename = 'wordlist.txt'
wordlist, v = np.loadtxt(filename, skiprows=0, dtype=str), 0
word = random.choice(wordlist)
print(word)
while v < 6:
    wordle_guess = input('--> ') 
    if word == wordle_guess:
        print(f'Yay you did it!!')
    else:
        v += 1 
    for i in range(len(word)):
        if (wordle_guess[i] == word[i]):
            print(i+1)
