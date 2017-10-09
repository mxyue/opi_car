import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc, status):
    print('status >>', status)
    print("Connected with result code "+str(rc))
    client.subscribe("$SYS/#")
    client.subscribe("test")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print('on message')
    print(msg.topic+" - "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mxyue.com", 1883, 60)
client.username_pw_set('user', '123')

client.loop_forever()
