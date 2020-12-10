#!/bin/bash
for i in {1..10}
do
	echo "1" > /sys/class/gpio/gpio2/value
	sleep 1
	echo "0" > /sys/class/gpio/gpio2/value
	sleep 1
done
