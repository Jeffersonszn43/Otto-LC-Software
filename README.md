## Otto LC Robot Project

##### The goal of this project is to learn how to build your own Otto LC robot and program the robot to do various creative movements using MicroPython. This repository will contain the skeleton code that you will have to finish to correctly make your robot do the required movements.

## Created By
##### Perry Weinthal
##### Corey Chang
##### Jefferson Charles

## Project Components

##### The skeleton software that must be completed to correctly showcase that your Otto LC robot was correctly built following the instruction guide can be found in the `Otto_LC_Software` folder in the repository. The design of your Otto LC robot included a Photoresistor, which is a light sensor, that will be responisble for when the robot will do the movements shown in the code. If the room the robot is in is dark, then the robot should do a certain gesture and display a certain emotion on the LED Matrix. When the room the robot is in is bright, then the robot will do it's walking and dancing movements along with displaying it's different emotions on the LED Matrix and the robot should also do emotional gestures. 

## Hardware Compatibility

##### The software we created for the project was designed to work on the Microcontroller below:
- Raspberry Pi Pico H

## Setup

#### Note: Before you proceed to this section, you must have your robots wired and fully built to follow the steps below.

#### Required Libraries

##### The OttoDIYPython library is the library that you will have to download to complete the software setup below for your robots and to work on the skeleton program written for your robots. The library was put inside of a zip file that you will download below and once you download the zip file proceed with the steps:

- [OttoDIYPython](https://github.com/Jeffersonszn43/Otto-LC-Software/releases/download/v1.0.0/OttoLCMicroPythonLibrary.zip)

##### The files in the zip file must be in the same directory as the MicroPython skeleton program for your Otto LC robot. Instructions on how to bring the files over from your local file explorer to the file explorer of the Raspberry Pi Pico H can be found in the setup section below.

##### This section will contain information on how to setup your environment for working with your robots:

1. First, you have to install the Thonny Python IDE to work with your Otto LC robot to run MicroPython programs on the robot. You can download the IDE using this link: [Thonny](https://thonny.org/)
2. Once you have installed Thonny, you must make sure you downloaded the OttoDIYPython library zip file above that contains all of the files that were built for the library. Note: Since the library was designed to run on the ESP8266 Microcontroller, some of the files had to be modified to work with the Pi Pico H Microcontroller. 
3. Next, you must setup MicroPython on the Raspberry Pi Pico H by downloading the MicroPython firmware file from this link: https://www.raspberrypi.com/documentation/microcontrollers/micropython.html
4. Once you are on the webpage, you must go down to where it says: `Download the correct MicroPython UF2 file for your board` and select Pico and that will download the MicroPython firmware file into your downloads folder.
5. Next, you have to connect the Raspberry Pi Pico H to your computer via USB while holding on to the BOOTSEL button on the board. This will open up the mass storage file explorer of the Pico where you will take the MicroPython firmware file that you just downloaded and copy and paste the file into the mass storage device of the Pico. After completing this, MicroPython should be setup on your Raspberry Pi Pico H board. Now when you go to the Thonny IDE, you should see the Raspberry Pi Pico as an option to choose for the COM port that is used for the Pico on the bottom right corner and you should choose the option that has the full Raspberry Pi Pico name.
6. Now that you have MicroPython setup on your Raspberry Pi Pico H Microcontroller, you must open the file explorer for the Pico and bring the contents of the OttoDIYPython library that you downloaded earlier to the file explorer of the Pico. Before you continue, you must make sure that the contents of the folder is unzipped and able to be brought over to the file explorer of the Pico. To open up the file explorer of the Pico you must go to View -> Files in Thonny. If you selected the com port of the Pico on the bottom right corner, you should see a split window that shows the file explorer of the directory that you are in in your local computer on top and the file explorer of the Pico on the bottom shown on the left side of Thonny. Locate where you downloaded the OttoDIYPython library and you are going to select all of the source code files in that folder. With all of the files selected, right click and select `Upload to /` to bring all of the files of the library to the file explorer of the Pico. 
7. Now, you should be setup to start working on the skeleton program to work with your robots. Go to the `Otto_LC_Software` folder and download the `Otto_LC.py` program and bring the file to the file explorer of the Pico using the same method used for bringing the files of the Otto MicroPython library over from your local computer to the Raspberry Pi Pico H. You will work on and run your code on your robot from Thonny. 
8. Before working on your skeleton program after building your robot, you must run the `demo.py` program under the `Otto_LC_Software` folder to test to see if you built your robot correctly and to make sure that your robot is fully functional.     

## Acknowledgements

##### This project is inspired from the OttoDIY and the Otto LC robot platform below:

- [OttoDIY](https://www.ottodiy.com/)
- [Otto LC](https://hackaday.io/project/26244-otto-lc)
