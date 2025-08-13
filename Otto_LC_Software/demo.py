# This will be a demo program that can be used to test your Otto LC robot after building it to make sure the robot was built and setup correctly.
# Written By: Jefferson Charles

# Here are the libraries needed for the program
import otto9, time
from machine import Pin, ADC, time_pulse_us

# Here we are initializing the Servo and Buzzer pins
LeftLeg = 3
RightLeg = 7
LeftFoot = 12
RightFoot = 10
Buzzer = 20

# Here is where we are initializing and defining all of the pins of the sensors on your robot
LDR_Pin = ADC(28)  # ADC pin for the Photoresistor.

Trig_Pin = Pin(22, Pin.OUT) # Trigger pin on Ultrasonic Distance Sensor.
Echo_Pin = Pin(21, Pin.IN)  # Echo pin on the Ultrasonic Distance Sensor.

# Here we are initializing the 8x8 LED Matrix that will be used for displaying the different emotions of your robot.
Din = 19
SCLK = 18
CS = 17

# This is the orientation on the 8x8 LED Matrix. This will allow the LEDs on the Matrix to display things in a normal orientation on the robot.
Orientation = 3

# Here is where we are initializing the Otto LC Robot along with the 8x8 LED Matrix.
# The values 1 and 2 are dummy values used to initalize the trigger and echo pins of the Ultrasonic Distance Sensor.
otto = otto9.Otto9()
otto.init(3, 7, 12, 10, True, 20, 1, 2, 19) 
otto.initMATRIX(Din, CS, SCLK, Orientation)
otto.home()

sensor_value = LDR_Pin.read_u16() # Here we are reading the ADC values from the light sensor in the range from 0-65535
    
sensor_value = sensor_value >> 4 # Here we are treating the sensor value as a 12-bit scale in the range from 0-4095
    
deadzone = int(sensor_value * 0.05) # Here we are creating a deadzone that will be 5% from the sensor value
    
# This if statement is responsible for testing the light sensor to make sure it works
if sensor_value >= 56 + deadzone:
    print("Your light sensor works! This room is dark!")
elif sensor_value <= 45 - deadzone:
    print("Your light sensor works! This room is bright!")

# Here we are sending 10us pulse to trigger the distance sensor
Trig_Pin.low()
time.sleep_us(2)
Trig_Pin.high()
time.sleep_us(10)
Trig_Pin.low()
    
# Here we are measuring the duration of the echo signal with a 50ms timeout
duration = time_pulse_us(Echo_Pin, 1, 50000)
    
# This is a test to make sure that we are getting an echo signal
if duration < 0:
    print("There was an error getting an echo signal.")
    
# Here we are converting the echo signal that was received to a distance in cm using the speed of sound (343 m/s or 0.0343 cm)
distance = (duration * 0.0343) / 2

# Here is where we are testing the distance sensor 
if distance != -1 and distance <= 30:
    print("Your distance sensor is working fine - object detected.")
else:
    print("Your distance sensor is working - no object detected.")

# Here are some of the basic functionalities that the Otto LC robot is capable of doing to test if your hardware components were wired and setup correctly
otto.walk(2, 1000, 1)
time.sleep_ms(200)
otto.walk(2, 1000, -1)
time.sleep_ms(200)
otto.turn(2, 1000, 1)
time.sleep_ms(200)
otto.turn(2, 1000, -1)
time.sleep_ms(200)
otto.bend(1, 500, 1)
time.sleep_ms(200)
otto.bend(1, 2000, -1)
time.sleep_ms(200)
otto.moonwalker(2, 1000, 25, 1)
time.sleep_ms(200)
otto.sing(3)
time.sleep_ms(200)
otto.putMouth(10)
time.sleep_ms(200)
otto.playGesture(11)
time.sleep_ms(200)
otto.home()
