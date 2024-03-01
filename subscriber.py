import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect('mqtt.eclipseprojects.io', 1883)
client.on_message = on_message
client.subscribe('iii24/test')

client.loop_forever(10)