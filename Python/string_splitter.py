# String Splitter
# Program by Owen McKenney

string = str(input("Enter a sentence: ")) # gets user input
string = string.replace(" ", "-") # replaces whitespaces with -
string_list = list(string) # converts string to list
string_list.append("-") # adds - at end

for x in string_list: # prints all elements in the list
    print(x)


