import paho.mqtt.client as mqtt
import time

mqttBROKER = "broker.emqx.io"
broker_port = 1883
client = mqtt.Client("groupD")


def on_message(client, userdata, message):
    decoded_message=str(message.payload.decode("utf-8"))
    msg=json.loads(decoded_message)


client.loop_start()

client.subscribe("sub")
client.on_message = on_message
client.connect(mqttBROKER,broker_port)
time.sleep(60)

client.loop_stop()