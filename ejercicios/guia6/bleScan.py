from bluetooth.ble import DiscoveryService

service = DiscoveryService()
devices = service.discover(5)   # Scan for 2 seconds

for address, name in devices.items():
    print("name: {}, address: {}".format(name, address))
