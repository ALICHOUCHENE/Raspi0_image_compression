# Raspi0_image_compression
A raspi zero triggered by an arduino take two pictures from a Picam and compress it and send it to a payboard using UART port.

## * OS SETUP 
Install the full version of [Raspbian](https://www.raspberrypi.org/software/operating-systems/#raspberry-pi-os-32-bit) operating system 

## * UPDATE THE SYSTEM
Open the terminal and run the coomand lines : 

 sudo apt-get update
 
 sudo apt-get upgrade
 
 
 
 
 ## * Picam Installation 

This will ensure that picamera is easy to keep up to date, and easy to remove should you wish to do so. It will also make picamera available for all users on the system. To install picamera using apt simply:

 $ sudo apt-get update

$ sudo apt-get install python-picamera python3-picamera

To upgrade your installation when new releases are made you can simply use apt’s normal upgrade procedure:

$ sudo apt-get update

$ sudo apt-get upgrade
