# Hangman
# Program by Owen McKenney

word = list(input("Player 1, what's the word? ").lower())
print("\n" * 20)

guess_list = []

for i in range(0, len(word)):
    guess_list.append("_")

print(guess_list)

while guess_list != word:
    valid_guess = False
    contains = False
    guess = str(input("\nPlayer 2, guess a letter: ").lower())

    for t in guess_list:
        if guess == t:
            valid_guess = True
           
    for i in word:
        if i == guess and valid_guess == False:
            contains = True
    
    if contains == True:
        indices = [i for i, x in enumerate(word) if x == guess]

        for j in range(0, len(indices)):
            guess_list.insert(indices[j], guess)
            guess_list.pop(indices[j] + 1)
        
        for x in range(0, len(guess_list)):
            print(guess_list[x], end=" ")
            
    elif valid_guess == False:
        print("Guess again!")
    else:
        print("You already guessed that letter")
       

