from bluetooth.ble import BeaconService
import Beacon

service = BeaconService()
devices = service.scan(5)

for address, data in list(devices.items()):
    b = Beacon.Beacon(data, address)
    print(b)

