import time
import paho.mqtt.client as mqtt

def on_publish(client, userdata, mid):
    print("message published")


client = mqtt.Client("rpi_teamx") #this name should be unique (different from broker)
client.on_publish = on_publish
client.connect('127.0.0.1',1883) #IP Address of MQTT Broker
client.loop_start()

var = "Hello World!"

msg = str(var)
pubMsg = client.publish(
    topic='rpi', #topic must be similar to the one you're subscribing to
    payload=msg.encode('utf-8'),
    qos=0,
)

pubMsg.wait_for_publish()
print(pubMsg.is_published())