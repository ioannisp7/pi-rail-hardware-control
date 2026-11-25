import sys
from machine import Pin

# Initialize the onboard LED.
led = Pin(25, Pin.OUT)
led.off()

# Continuously wait for commands.
while True:

    # Read a command from the USB serial connection.
    command = sys.stdin.readline().strip()

    # Interpret the received command.
    if command == "LED_ON":
        led.on()

    elif command == "LED_OFF":
        led.off()