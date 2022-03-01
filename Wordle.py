import random
wordlist, v = ("doofs","dylan","doodo"), 0
word = random.choice(wordlist)
while v < 6:
    wordle_guess = input('--> ') 
    if word == wordle_guess:
        print(f'Yay you did it!!')
    else:
        v += 1
    
    for i in range(len(word)):
        if (wordle_guess[i] == word[i]):
            print(i+1)
