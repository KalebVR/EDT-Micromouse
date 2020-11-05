import RPi.GPIO as io
import time
io.setmode(io.BCM)

TRIG = 23
ECHO = 24

print("Distance measurement in progress...")

io.setup(TRIG, io.OUT)
io.setup(ECHO, io.IN)

io.output(TRIG, False)
print("Waiting for sensor to settle...")
time.sleep(2)

io.output(TRIG, True)
time.sleep(.00001)
io.output(TRIG, False)

while io.input(ECHO) == 0:
    pulse_start = time.time()
while io.input(ECHO) == 1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150
distance = round(distance, 2)

print("Distance: ", distance, " cm")

io.cleanup()
