# Here is the software that will have the control logic for the Otto LC robot.
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

# Here is where we are initializing and defining all of the pins of the sensors on the robot
LDR_Pin = ADC(28)  # ADC pin for the Photoresistor.

Trig_Pin = Pin(22, Pin.OUT) # Trigger pin on Ultrasonic Distance Sensor.
Echo_Pin = Pin(21, Pin.IN)  # Echo pin on the Ultrasonic Distance Sensor.

# Here we are initializing the 8x8 LED Matrix that will be used for displaying the different emotions of the robot.
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

# This function is responsible for the light sensor integration on the robot
def light_levels():
    sensor_value = LDR_Pin.read_u16()  # Here we are reading the ADC value (0 - 65535)
    
    # Here we are showing the ADC value as a 12-bit scale (0 - 4095)
    sensor_value = sensor_value >> 4
    
    # Here we are computing the deazone that will be 5% from the sensor value of the light sensor
    deadzone = int(sensor_value * 0.05)
    
    # Here we are observing the light levels of the room Jerry is in
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


# Function that will allow the robot to implement obstacle avoidance during its movements
def obstacle_avoidance():
    detected_object = get_distance()
    
    if detected_object != -1 and detected_object <= 30:
        print("Object in front of me")
        otto.putMouth(20)
        otto.playGesture(5)
        time.sleep_ms(500)
        # This will make the robot walk back a little bit and turn once it detects an object in front of it
        otto.walk(2, 1000, -1)
        otto.turn(2, 1000, 1)
        time.sleep_ms(500)
    else:
        print("No object in front of me")
            

# Here are the functions for the main control logic for the robot

# This function will be responsible for the movement options the robot can perform, while implementing obstacle avoidance
def otto_movements():
    otto.walk(4, 1000, 1) # Walking forward
    time.sleep_ms(200)
    otto.walk(4, 1000, -1) # Walking backwards
    time.sleep_ms(200)
    otto.turn(2, 1000, 1) # Turning to the left
    time.sleep_ms(200)
    otto.turn(2, 1000, -1) # Turning to the right
    time.sleep_ms(200)
    otto.bend(1, 500, 1) # Bending the left foot
    time.sleep_ms(200)
    otto.bend(1, 2000, -1) # Bending the right foot
    time.sleep_ms(200)
    otto.home() # Makes the robot go to its default position
    time.sleep_ms(100)

# This function will be responsible for the robot dancing
def otto_dances():
    otto.shakeLeg(1, 1500, 1) # Left
    otto.shakeLeg(1, 2000, -1) # Right
    otto.moonwalker(4, 1000, 25, 1) # Left
    otto.moonwalker(4, 1000, 25, -1) # Right
    otto.crusaito(3, 1000, 20, 1) # Left
    otto.crusaito(3, 1000, 20, -1) # Right
    time.sleep_ms(100)
    otto.flapping(3, 1000, 20, 1) # Left
    otto.flapping(3, 1000, 20, -1) # Right
    time.sleep_ms(100)
    otto.swing(3, 1000, 20)
    otto.tiptoeSwing(3, 1000, 20)
    otto.jitter(3, 1000, 20)
    otto.updown(3, 1500, 20)
    otto.ascendingTurn(3, 1000, 50)
    otto.jump(1, 2000)
    otto.home()
    time.sleep_ms(100)

# This function is responsible for sounds that the robot can produce
def otto_sounds():
    otto.sing(0) # Connection sound
    otto.sing(1) # Disconnection sound
    otto.sing(3) # OHOOH sound
    otto.sing(18) # Buttonpressed sound

# This function is responsible for gestures performed by the robot
def otto_gestures():
    otto.playGesture(0) # Happy gesture
    time.sleep_ms(600)
    otto.playGesture(2) # Sad gesture
    time.sleep_ms(600)
    otto.playGesture(11) # Victory gesture
    time.sleep_ms(600)
    otto.playGesture(3) # Sleeping gesture
    time.sleep_ms(600)

# This function is responsible for displaying the emotions of the robot
def otto_emotions():
    otto.putMouth(10) # Smile emotion
    time.sleep_ms(700)
    otto.putMouth(11) # Happyopen emotion
    time.sleep_ms(700)
    otto.putMouth(22) # Sad emotion
    time.sleep_ms(700)
    otto.putMouth(20) # Confused emotion
    time.sleep_ms(700)    
    
# This loop will be responsible for 
while True:
    otto.home() # Sets the robot in its neutral position
    time.sleep(1)
    
    current_light = light_levels() # Here will be the light sensor values produced by the robot
    
    # If the room the robot is in is dark, then the robot will perform these actions instead
    if current_light == "dark":
        otto.putMouth(24) # Sadclosed emotion
        otto.sing(2) # Surprise sound
        otto.playGesture(5) # Confused gesture
        
    # If there is enough light in the room the robot is currently in, then it will perform its movements    
    elif current_light == "bright":
        # This function call is responsible for the implementation of obstacle avoidance on the robot
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
    

