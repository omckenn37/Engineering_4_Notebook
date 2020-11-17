word = list(input("Player 1, what's the word? ").lower())
print("\n" * 10)

guess_list = []

for i in range(0, len(word)):
    guess_list.append("_")

print(guess_list)

#while guess_list != word:

for x in range(0,1):
    guess = str(input("Player 2, guess a letter: ").lower())

    for i in word:
        if(i == guess):
            guess_list.insert(word.index(guess), guess)
            guess_list.pop(word.index(guess) + 1)


print(guess_list)

