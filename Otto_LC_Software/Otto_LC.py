# Here is the skeleton code that will have the control logic for your Otto LC robot.
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

# This function is responsible for the light sensor integration on your robot
def light_levels():
    sensor_value = LDR_Pin.read_u16()  # Here we are reading the ADC value (0 - 65535)
    
    # Here we are showing the ADC value as a 12-bit scale (0 - 4095)
    sensor_value = sensor_value >> 4
    
    # Here we are computing the deazone that will be 5% from the sensor value of the light sensor
    deadzone = int(sensor_value * 0.05)
    
    # Here we are observing the light levels of the room your robot is in
    if sensor_value >= 56 + deadzone:
        return "dark"
        
    elif sensor_value <= 45 - deadzone:
        return "bright"
        
    
# This function will be responsible for getting the distance values of the distance sensor
def get_distance ():
    # Here we are sending a 10us pulse to trigger the sensor
    Trig_Pin.low()
    time.sleep_us(2)
    Trig_Pin.high()
    time.sleep_us(10)
    Trig_Pin.low()
    
    # Here is where we are measuring the duration of the echo signal with a 50ms timeout
    duration = time_pulse_us(Echo_Pin, 1, 50000)
    
    # Here is a test to see if we get an echo signal
    if duration < 0:
        print("There is an error in getting an echo signal.")
        return -1
    
    # Here we are converting the echo signal to distance in cm using the speed of sound (343 m/s or 0.0343 cm)
    distance = (duration * 0.0343) / 2
    return distance


# Function that will allow your robot to implement obstacle avoidance during its movements
def obstacle_avoidance():
    detected_object = get_distance()
    
    if detected_object != -1 and detected_object <= 30:
        print("Object in front of me")
        otto.putMouth(20)
        otto.playGesture(5)
        time.sleep_ms(500)
        # This will make your robot walk back a little bit and turn once it detects an object in front of it
        otto.walk(2, 1000, -1)
        otto.turn(2, 1000, 1)
        time.sleep_ms(500)
    else:
        print("No object in front of me")
            

# Here are the functions for the main control logic for your robot that you will have to complete

# This function will be responsible for the movement options your robot can perform, while implementing obstacle avoidance
def otto_movements():
    """
    Enter the code for the movement logic for your robot here using methods like:
    - walk()
    - turn() 
    
    Note: Make sure to implement a 200 ms delay in between your logic.
    """

    # Enter your code below:


    otto.home() # Makes your robot go to its default position
    time.sleep_ms(100)

# This function will be responsible for your robot performing dances
def otto_dances():
    """
    Enter the code for the dancing logic for your robot here using methods like: 
    - moonwalker()
    - crusaito()

    Note: Make sure to implement a 200 ms delay in between your logic.
    """
    
    # Enter your code below:


    otto.home() # Makes your robot go to its default position
    time.sleep_ms(100)

# This function is responsible for the robotic sounds that your robot can produce
def otto_sounds():
    """
    Enter the code to have your robot produce robotic sounds here using methods like:
    - sing(#)
    """

    # Enter your code below:


# This function is responsible for the emotional gestures performed by your robot
def otto_gestures():
    """
    Enter the code here to have your robot perform emotional gestures using methods like:
    - playGesture(#)

    Note: Make sure that you implement a 200 ms delay in between your logic.
    """

    # Enter your code below:


# This function is responsible for displaying the emotions of your robot
def otto_emotions():
    """
    Enter the code here to have your robot display facial expressions on the LED Matrix using methods like:
    - putMouth(#)

    Note: Make sure to implement a 200 ms delay in between your logic.
    """   

    # Enter your code below:

    
# This loop will be responsible for executing what your robot will do depending on the light levels of the room your robot is in
while True:
    otto.home() # Sets your robot in its neutral position
    time.sleep(1)
    
    current_light = light_levels() # Here will be the light sensor values produced by your robot
    
    # If the room your robot is in is dark, then the robot will perform these actions
    if current_light == "dark":
        otto.putMouth(24) # Sadclosed emotion
        otto.sing(2) # Surprise sound
        otto.playGesture(5) # Confused gesture
        
    # If the room your robot is in is bright enough, then your robot will perferm these actions instead   
    elif current_light == "bright":
        # This function call is responsible for the implementation of obstacle avoidance on your robot
        obstacle_avoidance()
        
        otto_movements()
        time.sleep(1)
        otto_dances()
        time.sleep(1)
        otto_sounds()
        time.sleep(1)
        otto_gestures()
        time.sleep(1)
        otto_emotions()
        time.sleep(1)
    
    # Here we have a 500ms delay in the loop
    time.sleep_ms(500)
    

