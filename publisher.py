import time
import paho.mqtt.client as mqtt



mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

mqttc.connect('mqtt.eclipseprojects.io', 1883)
mqttc.loop_start()

msg = 0
for i in range(1000):
    time.sleep(1)
    msg_info = mqttc.publish('iii24/test', msg)
    msg += 1

# Due to race-condition described above, the following way to wait for all publish is safer
# msg_info.wait_for_publish()

mqttc.disconnect()
mqttc.loop_stop()