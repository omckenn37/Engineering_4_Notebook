# String Splitter
# Program by Owen McKenney

string = str(input("Enter a sentence: "))

for x in string:
    if x == " ":
        print("-")
    else:
        print(x)

