import time
import dbFunctions

sensor = {}
sensor["date"] = time.time()
sensor["sensorID"] = "sensor8"

dbFunctions.insertSensorEvent(sensor)