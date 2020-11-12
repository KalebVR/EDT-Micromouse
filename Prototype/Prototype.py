'''
Chicago EDT MicroMouse
Fall 2020
Author: Kaleb Vicary-Rzab
'''
import RPi.GPIO as io
import time
io.setwarnings(False)
io.setmode(io.BCM)


# Ultrasonic Ranger Right Pins
# GND, ECHO, TRIG, VCC 
TRIG_1 = 23
ECHO_1 = 24


# Ultrasonic Ranger Left Pins
# GND, ECHO, TRIG, VCC 
TRIG_2 = 22
ECHO_2 = 27


# Motor Pins
# EN1:1; IN1:2,  IN2:7;  OUT1:3;  OUT2:6
# EN2:9; IN3:10, IN4:15; OUT3:11; OUT4:14
# GND:4,5,12,13
# Vss:16; Vs:8

# Right Motor
in1_pin = 4
in2_pin = 17
en1_pin = 18

# Left Motor
in3_pin = 5
in4_pin = 16
en2_pin = 13

pwm_r = io.PWM(18, 500) 
pwm_l = io.PWM(13, 500) 


def ranger_right():
    pulse_start = 0
    pulse_end = 0
    pulse_duration = 0
    distance = 0

    # print("Distance measurement in progress...")
    io.setup(TRIG_1, io.OUT)
    io.setup(ECHO_1, io.IN)

    io.output(TRIG_1, False)
    # print("Waiting for sensor to settle...")
    time.sleep(.00001)

    io.output(TRIG_1, True)
    time.sleep(.00001)
    io.output(TRIG_1, False)

    while io.input(ECHO_1) == 0:
        pulse_start = time.time()
    while io.input(ECHO_1) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)

    print("Right Distance: ", distance, " cm")
    return distance


def ranger_left():
    pulse_start = 0
    pulse_end = 0
    pulse_duration = 0
    distance = 0

    # print("Distance measurement in progress...")
    io.setup(TRIG_2, io.OUT)
    io.setup(ECHO_2, io.IN)

    io.output(TRIG_2, False)
    # print("Waiting for sensor to settle...")
    time.sleep(.00001)

    io.output(TRIG_2, True)
    time.sleep(.00001)
    io.output(TRIG_2, False)

    while io.input(ECHO_2) == 0:
        pulse_start = time.time()
    while io.input(ECHO_2) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)

    print("Left Distance: ", distance, " cm")
    return distance


def clockwise():
    io.output(in1_pin, True)    
    io.output(in2_pin, False)


def motor_control(d_right, d_left):
    if distance_left > 10.0:
        dc_r = 100
        dc_l = 50
    elif distance_right > 10.0:
        dc_r = 50
        dc_l = 100
    else:
        dc_r = 100
        dc_l = 100
        
    en1_pin.ChangeDutyCycle(dc_r)
    en2_pin.ChangeDutyCycle(dc_l)


def color_sensor():
    pass


def main():
    distance_right = ranger_right()
    distance_left = ranger_left()
    motor_control(distance_right, distance_left)
    time.sleep(2)


clockwise()
dc = 0
pwm_r.start(dc)
pwm_l.start(dc)

try:
    while True:
        main()
except KeyboardInterrupt:
    print("Interrupt")

pwm.stop()
io.cleanup()
