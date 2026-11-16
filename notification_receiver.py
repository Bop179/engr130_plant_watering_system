from microbit import *
import radio

radio.config(channel=17)
radio.on()
previous_status = ""

print("Plant notification receiver started.")
print("Waiting for the plant system...")

while True:
    message = radio.receive()

    if message is not None:
        if message == "NEED_WATER":
            if previous_status != "DRY":
                print("Notification: The soil is dry. Water is needed.")
                display.show(Image.SAD)
            previous_status = "DRY"

        elif message == "MOISTURE_OK":
            if previous_status != "OK":
                print("Notification: The soil is not below the watering threshold.")
                display.show(Image.HAPPY)
            previous_status = "OK"

        elif message == "WATERED":
            print("Notification: The watering cycle is complete.")

    sleep(100)
