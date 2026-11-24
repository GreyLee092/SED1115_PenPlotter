# Raspberry Pi Pico Brachiograph
<img width="1151" height="833" alt="image" src="https://github.com/user-attachments/assets/4fa9fbba-eb4d-41ed-bec4-a94a80efc28c" />

## Description
This project allows a user to draw with a pen affixed to a servo arm in the same manner as an Etch-a-Sketch. Users will control the horizontal and vertical position of the pen on the page by turning the appropriate potentiometer. The Pico microcontroller will then calculate the angle each servo motor needs to turn for the pen to move towards the desired position.

## Hardware Requirements
- 1x Raspberry PI Pico
- 2x Potentiometers
- 1x Button/Switch
- 2x MG995 Servos
- 1x Micro Servo
- Custom 3D-printed parts for arm fixture
  
## Installation 
You can clone this repository by running ``` git clone https://github.com/GreyLee092/SED1115_PenPlotter.git ``` 
Ensure that the ```Shoulder```, ```Elbow```, & ```Wrist``` Servos are plugged into the respective ports.

Update the ```Elbow_Servo_Recalibrated_Values.csv``` and ```Shoulder_Servo_Recalibrated_Values.csv``` files to match your servo settings.

## Usage
To run the program, ensure the potentiometer values start at their middle value so that the arm starts within the range of the board; otherwise, if set to max or min values, the arm could start off the board.

Slowly rotate each potentiometer to control the desired axis; lower the wrist to start drawing by pressing the button. 
