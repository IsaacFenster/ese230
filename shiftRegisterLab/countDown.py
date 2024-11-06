# import RPi.GPIO as GPIO
# import time

switchPin = 16
aPin = 12
bPin = 13
cPin = 14
dPin = 15
ePin = 17
fPin = 18
gpin = 19

myList = [aPin, bPin, cPin]

for i in myList:
    print(i)

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# GPIO.cleanup()

# GPIO.setup(switchPin, GPIO.IN)
# GPIO.setup(ledPin, GPIO.OUT)
# GPIO.setup(buzzPin, GPIO.OUT)

# while True:
#     if(GPIO.input(switchPin)):
#         GPIO.output(ledPin,True)
#         GPIO.output(buzzPin,True)
#         time.sleep(1)
#     else:
#         GPIO.output(ledPin,False)
#         GPIO.output(buzzPin,False)
