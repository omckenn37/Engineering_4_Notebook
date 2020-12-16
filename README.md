# Engineering_4_Notebook
Engineering 4 repo
## Python Assignments

### Hello Python

#### Description
In this assignment, we created a simple [dice rolling program](https://github.com/omckenn37/Engineering_4_Notebook/blob/main/Python/dice_roller.py).

Here is a screenshot of this program in action:

<img src="Python/media/hello_python_screenshot.png" width="500">

#### Lessons Learned

This assignment was pretty easy. It involved a while loop with a couple of if statements to check what the users's input was. For whatever reason, the one time I screenshot my output it happened to randomly select to print two sixes then two twos then two fours in a row.

### Calculator
#### Description
In this assignment, we created a simple [calculator](https://github.com/omckenn37/Engineering_4_Notebook/blob/main/Python/Calculator.py) function that does different operations to the two input numbers. 

Here is a screenshot of this program in action:

<img src="Python/media/Calculato_screenshot.png" width="500">

#### Lessons Learned

One issue that I had when trying to code this was the "can't concatenate str and int objects" error. I realized that I was getting this error because I was trying to print both a string and an integer in the same line. I fixed this by making my doMath() function return a string instead of an int. This made the print statement contain the same type, so I no longer had an error. 
Also, through these assignments, I think I'm getting better at using git commands. I finally understand when and how to add, commit, and push files which has been pretty helpful. 

### Quadratic Solver
#### Description
In this assignment, we created a [quadratic calculator](https://github.com/omckenn37/Engineering_4_Notebook/blob/main/Python/quadratic_solver.py) to find the roots for any given quadratic. The program either returns two real roots or returns that there are no real roots. 

Here is a screenshot of this program in action:

<img src="Python/media/quadratic_solver_screenshot.png" width="500">

The first quadratic has two real roots, 2 and -2, while the second quadratic had no real roots. 

#### Lessons Learned

When coding this assignment I tried to create the least amount of variables possible. This is why in my function solve(), I only have one list called roots which either gets set to the two roots or two strings which says there are no roots. One issue I had was accessing the contents of the list once it had been returned from my solve() function. I realized that by adding a [0] or a [1] at the end of the called function, I could access either the 1st or 2nd element of that list. This helped me print out the correct values. 

### Strings and Loops
#### Description

In this assignment, we created a [program which takes in a string and prints out each letter in that string](https://github.com/omckenn37/Engineering_4_Notebook/blob/main/Python/string_splitter.py). It also prints a minus sign for every whitespace in that string.

Here is a screenshot of this program in action:

<img src="Python/media/string_splitter_screenshot.png" width="500">

#### Lessons Learned

There were a bunch of different ways that this assignment could have been completed. You could have actually gotten the same result without using any lists at all. In python, you are able to print out specific letters in a string which in a way defeats the purpose of converting the string to a list. In my version, I opted to convert my string into a list anways and then used a for loop to print each element in that list. To convert the whitespaces to minus signs, I used the replace() function in python which takes two parameters: the string you want replaced and what you will replace it with. I had used this before, but this assignment reminded me that in order to use it you have to make a new variable or set your previous variable equal to itself in order for the replace() function to work. 

### Hangman
#### Description

In this assignment, we created a 2 player [hangman program](https://github.com/omckenn37/Engineering_4_Notebook/blob/main/Python/hangman.py). Player 1 picks a word while player 2 tries to guess the word. 

#### Pictures 

Here's what happens when player 2 guesses the right letters and wins the game:
<img src="Python/media/hangman1.png" width="500">

<img src="Python/media/hangman2.png" width="500">

Here's the picture of Graham that is printed once you guess 5 wrong letters, as well as the image it is based off of; if you lean back and squint, it does actually kind of look like Graham.

<p float="left">
  <img src="Python/media/hangman4.png" width="500" />
  <img src="Python/media/graham.png" width="300" />
</p>

The program also prints sections of the [graham.txt](https://github.com/omckenn37/Engineering_4_Notebook/blob/main/Python/graham.txt) file every time player 2 guesses wrong, it was just hard to screenshot so I only included the final product.

#### Lessons Learned

This assignment was definitely harder than the others. It was quite a bit longer than the others and involved for loops, if statements, lists, strings, and a  bunch of ther stuff. For me, the biggest problem I ran into was trying to find all indices of a letter in the word. For example, words like "cool" or "letter" contain multiple instances of the same letter. The issue was that the code I had written only recognized the first instance of this letter, which would ruin the program becuase the second instance of that letter would essentially be unguessable making the game go on forever. I solved this problem by changing my index variable to a list and using enumerate() to find all instances of the letter. 

For this assignment, I also decided to use a text file to print a picture rather than make an array or list and print sections of that. I figured it would be easier and cleaner to use a text file, plus it was easier to make this text file anything that I wanted it to be. I used a [image to ASCII converter](https://manytools.org/hacker-tools/convert-images-to-ascii-art/) to convert the picture of Graham into ASCII characters that could be printed in a terminal window. Once I had this file, I added it to my Python folder via file upload and pulled those changes to my pi so the file was on my pi. After that, all I had to do was figure out how to use the built in text file commands that python has such as open() and readline().

### SSH

#### Description

In this assignment, I connected to my pi via SSH. 

Here is a picture of my wiring:

<img src="Python/media/sshpic.JPG" width="300">

#### Lessons Learned

This assignment was super helpful because it showed me how to access my pi without having to deal with the uart cable. Now I can also put my pi anywhere that I want and still be able to access it. All I had to do was enable SSH on my pi, get the ip, and the connect to it in a seperate terminal window. Once I was connected I ran this simple [led blink](https://github.com/omckenn37/Engineering_4_Notebook/blob/main/Python/led_blink.py) program to make sure everything was working properly.

### Bash

#### Description

In this assignment, I created a [blink.sh](https://github.com/omckenn37/Engineering_4_Notebook/blob/main/Python/blink.sh) bash file to blink two LED's on and off 10 times.

I started by using the command line commands. First I used `gpio mode 29 out` to set 29 as an output. Then, I used `gpio write 29 1` to set that pin to high and `gpio write 29 0` to set the pin to low. 
With that done, I just had to figure out how to do it in a bash file. I created a .sh file and put in a simple for loop which ran 10 times. Then, I had to find a way to blink an led in the bash file. Using [this website](https://www.teknotut.com/en/first-raspberry-pi-project-blink-led/#Blink_Project), I was able to figure out how to do this in a bash file. Also, instead of using two pins for the two different LEDs I just opted to wire both to the same pin for simplicity. I ended up with this code:
```
#!/bin/bash

for i in {1..20} # for loop that runs 20 times
do	
	# for simplicity, I wired both LED's to one pin
	/usr/bin/gpio toggle 29 # this toggles gpio29 on and off
	sleep .5	
done
```

#### Lessons Learned

This assignment was a lot more difficult than I initially expected it to be. I had some difficulty just running the command line commands; I think this was because I kept confusing the physical pin with the gpio pin and vice versa. After finally getting that to work, I tried using those commands in the bash file. Obviously that didn't work. After looking on the internet for a while, I came across the previously linked website. This was super helpful because it outlined pretty much the exact thing I was trying to do. After finding this, it was smooth sailing. The only other issue I had was the LEDs not blinking enough. When the for loop ran 10 times, they would only blink 5 times. I quickly realized this was because the toggle command just toggles to the opposite state that the pin is currently at. So, this means that for every 2 times through the loop, there is only one blink. All I did was change the loop to run 20 times and I was done. 

