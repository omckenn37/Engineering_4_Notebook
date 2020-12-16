#!/bin/bash

for i in {1..20} # for loop that runs 20 times
do	
	# for simplicity, I wired both LED's to one pin
	/usr/bin/gpio toggle 29 # this toggles gpio29 on and off
	sleep .5	
done

