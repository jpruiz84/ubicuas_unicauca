import paho.mqtt.publish as publish
from bluetooth.ble import BeaconService
import Beacon
import time

publish.single("/unicauca", "Juan Pablo from Python",\
 hostname="broker.hivemq.com")


beaconDir = []
 
while True: 
  service = BeaconService()
  devices = service.scan(3)

  #{'BeaconMAC': '11:22:33:44:55:66', 'time': '2017/09/27, 18:45:55'}|
  for address, data in list(devices.items()):
      b = Beacon.Beacon(data, address)
      print(b)
      dirOut = {}
      dirOut["BeaconMAC"] = b._address
      dirOut["time"] = time.strftime("%Y/%m/%d, %H:%M:%S", \
      time.localtime(time.time()))
      
      
      if b._rssi > -60:
        beaconData = {}
        beaconData["MAC"] = b._address
        beaconData["stateSent"] = False # If the MQTT was sent   
        itWasSent = True    
        
        exist = False
        for beaconinDir in beaconDir:
          if beaconinDir["MAC"] == beaconData["MAC"]:
            exist = True
            itWasSent = beaconinDir["stateSent"] 
            
            
        if exist == False or itWasSent == False:
          beaconData["stateSent"] = False # If the MQTT was sent       True # If the MQTT was sent       
          beaconDir.append(beaconData)
        
          print dirOut
          publish.single("/unicauca", str(dirOut),\
            hostname="broker.hivemq.com")
        
      else:
    
        exist = False
        for beaconinDir in beaconDir:
          if beaconinDir["MAC"] == b._address:
            beaconinDir["stateSent"] = False

        
        

      
