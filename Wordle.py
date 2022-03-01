import random
v = 0
wordlist= ("doofs","dylan","dystopia")
word = random.choice(wordlist)
while v == 0:
    wordle_guess = input('--> ') 
    if word == wordle_guess:
        print(f'Yay you did it!!')
    if wordle_guess[0] == word[0]:
        print(1)
    if wordle_guess[1] == word[1]:
        print(2)
    if wordle_guess[2] == word[2]:
        print(3)
    if wordle_guess[3] == word[3]:
        print(4)
    if wordle_guess[4] == word[4]:
        print(5)