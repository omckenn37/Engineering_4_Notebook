# Hangman
# Program by Owen McKenney

word = list(input("Player 1, what's the word? ").lower())
print("\n" * 10)

guess_list = []

for i in range(0, len(word)):
    guess_list.append("_")

print(guess_list)

#while guess_list != word:

while guess_list != word:
    guess = str(input("Player 2, guess a letter: ").lower())

    for i in word:
        if(i == guess):
            indices = [i for i, x in enumerate(word) if x == guess]

            for j in range(0, len(indices)):
                guess_list.insert(indices[j], guess)
                guess_list.pop(indices[j] + 1)

            print(guess_list)

       

