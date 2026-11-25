import serial

connection = serial.Serial(
    port="/dev/ttyACM0",
    baudrate=115200,
    write_timeout=2
)

try:
    while True:
        command = input("Enter command: ")

        if command == "EXIT":
            break

        connection.write((command + "\n").encode())
        connection.flush()

finally:
    connection.close()