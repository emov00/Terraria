from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

#to get ip address type 'ping raspberry pi' into windows cmd

factory = PiGPIOFactory(host="2601:240:8101:af40::762b")
led = LED(17, pin_factory=factory)

print('running')
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)

    if KeyboardInterrupt:
        led.off()

