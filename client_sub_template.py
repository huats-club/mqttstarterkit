# Huats Club 2022
import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
   global flag_connected
   flag_connected = 1
   client_subscriptions(client)
   print("Connected to MQTT Broker")

def on_disconnect(client, userdata, rc):
   global flag_connected
   flag_connected = 0
   print("Disconnected from MQTT Broker")
   
# Callback Function - Decoding received messages from various topics
def callback_rpi(client, userdata, msg):
    print('Raspberry Pi Broadcast message: {}'.format(str(msg.payload.decode('utf-8'))))
    print("Message End")

# A list of topics you wish to subscribe to
def client_subscriptions(client):
    client.subscribe("rpi") 

client = mqtt.Client("rpi_master") #this should be a unique name
flag_connected = 0

# Declare Connection
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.message_callback_add('rpi', callback_rpi)
client.connect('127.0.0.1',1883) # IP Address of MQTT Broker (Local Host or External Devices)

# Start Connection
client.loop_start()
client_subscriptions(client)
print("......client setup complete............")


while True:
    time.sleep(4)
    if (flag_connected != 1):
        print("trying to connect MQTT Broker...")