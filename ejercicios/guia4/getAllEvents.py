import dbFunctions
import time

sensorEvents = dbFunctions.getAllEvents()

for event in sensorEvents:
    print("Sensor ID: " + event["sensorID"])
    print("date: " + time.strftime("%Z - %Y/%m/%d, %H:%M:%S", time.localtime(event["date"])))
    # Add other values to print
    print("\n")