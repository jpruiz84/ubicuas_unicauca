from bluetooth.ble import BeaconService
import dbFunctions
import Beacon
import time

DISCOVER_TIME = 3  # In seconds, scan interval duration.

service = BeaconService()   # Start the service object as beacon service
dbFunctions.createTable()   # If not exist, create the table sensors

while True:

    devices = service.scan(DISCOVER_TIME)   # Scan the devices inside the beacon service

    for address, data in list(devices.items()): # Run for loop for the scanned beacons
        b = Beacon.Beacon(data, address)    # Create the object b from class Beacon
        print(b)

        sensor = {}                      # Initialize the dictonary sensor
        sensor["date"] = time.time()     # Add current time
        sensor["address"] = b._address   # Add beacon address
        sensor["rssi"] = b._rssi         # Add beacon signal level rssi

        dbFunctions.insertSensorEvent(sensor)   # Insert sensor event to database
