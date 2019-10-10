import paho.mqtt.publish as publish

publish.single("/unicauca", "Juan Pablo from Python",\
 hostname="broker.hivemq.com")
