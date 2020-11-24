# Hangman
# Program by Owen McKenney

word = list(input("Player 1, what's the word? ").upper())
print("\n" * 40)

guessed = "_" * len(word)
guessed = list(guessed)
first_guessed = []
letter = input("Player 2, guess a letter: ")
num_guesses = 5

while True:
    if letter.upper() in first_guessed:
        letter = ""
        print("Player 2, you already guessed this letter")
    elif letter.upper() in word:
        index = word.index(letter.upper())
        guessed[index] = letter.upper()
        word[index] = "_"

    else:
        num_guesses -= 1
        print("Wrong! Guesses left: " + str(num_guesses))
        print("".join(guessed))
        if num_guesses == 0:
            print("Player 2, you ran out of guesses. You lose!")
            break
        
        if letter is not "":
            first_guessed.append(letter.upper())
        letter = input("Player 2, guess a letter: ")

    if "_" not in guessed:
        print(word)
        print("Player 2, you won")

        break
       

