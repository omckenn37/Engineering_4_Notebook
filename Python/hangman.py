# Hangman
# Program by Owen McKenney

word = list(input("Player 1, what's the word? ").upper())
print("\n" * 20)

guessed = "_" * len(word)
guessed = list(guessed)
first_guessed = []
letter = input("Player 2, guess a letter: ")

while True:
    if letter.upper() in first_guessed:
        letter = ""
        print("Player 2, you already guessed this letter")
    elif letter.upper() in word:
        index = word.index(letter.upper())
        guessed[index] = letter.upper()
        word[index] = "_"

    else:
        print("".join(guessed))

        if letter is not "":
            first_guessed.append(letter.upper())
        letter = input("Player 2, guess a letter: ")

    if "_" not in guessed:
        print(word)
        print("Player 2, you won")

        break






        
       

