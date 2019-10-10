import time
import dbFunctions

while True:
    sensor = {}
    sensor["date"] = time.time()
    sensor["sensorID"] = raw_input("Inserte sensorID, fin para terminar: ")

    if sensor["sensorID"].upper() == "fin".upper():
        break

    dbFunctions.insertSensorEvent(sensor)