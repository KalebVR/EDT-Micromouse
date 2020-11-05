import RPi.GPIO as io
io.setwarnings(False)
io.setmode(io.BCM)
 
in1_pin = 4
in2_pin = 17
en1_pin = 18
 
io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)
io.setup(en1_pin, io.OUT)

pwm = io.PWM(18, 500) 

def clockwise():
    io.output(in1_pin, True)    
    io.output(in2_pin, False)
 
def counter_clockwise():
    io.output(in1_pin, False)
    io.output(in2_pin, True)
 
clockwise()

dc = 0
pwm.start(dc)

try:
    while True:
        for dc in range(50,101):
            clockwise()
            en1_pin.ChangeDutyCycle(dc)
            time.sleep(.1)
        for dc in range(50,101):
            counter_clockwise()
            en1_pin.ChangeDutyCycle(dc)
            time.sleep(.1)
except KeyboardInterrupt:
    print("Interrupt")

pwm.stop()
io.cleanup()