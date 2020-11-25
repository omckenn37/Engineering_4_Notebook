# Hangman
# Program by Owen McKenney

word = list(input("Player 1, what's the word? ").upper())
print("\n" * 40)

guessed = "_" * len(word)
guessed = list(guessed)
already_guessed = []
letter = ""
num_guesses = 5
print("Player 2, try to guess the word before Graham's face is printed out")

def draw(n):
    f = open("graham.txt", "r")
    for x in range(0, (5-n) * 4 + 1):
        print(f.readline(), end="")

while True:
    print("-" * 40)
    letter = input("Player 2, guess a letter: ")

    if letter.upper() in already_guessed:
        letter = ""
        print("Player 2, you already guessed this letter")

    elif letter.upper() in word:
        already_guessed.append(letter.upper())
        index = word.index(letter.upper())
        guessed[index] = letter.upper()
        word[index] = "_"
        print("".join(guessed))

    elif letter.upper() not in word:
        already_guessed.append(letter.upper())
        num_guesses -= 1
        print("Wrong! Guesses left: " + str(num_guesses))
        print("")
        draw(num_guesses)
        print("")

        if num_guesses == 0:
            print("Player 2, you ran out of guesses. You lose!")
            break            
        
    if "_" not in guessed:
        print("Player 2, you won")
        break
    

