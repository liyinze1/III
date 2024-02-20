import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

mqttBroker = '10.147.19.97:1883'
client = mqtt.Client('server')
client.connect(mqttBroker)

client.loop_start()
client.subscribe('test')
client.on_message = on_message
time.sleep(30)
client.loop_end()