from ws import WS_Server
import json
import time

NAME = 'my_esp8266'

# Client Mode
# WIFI_MODE = "sta"
# SSID = "YOUR SSID HERE"
# PASSWORD = "YOUR PASSWORD HERE"

# AP Mode
WIFI_MODE = "ap"
SSID = ""
PASSWORD = "12345678"

ws = WS_Server(name=NAME, mode=WIFI_MODE, ssid=SSID, password=PASSWORD)
ws.start()

potentiometer = machine.ADC(28)
button = machine.Pin(14,machine.Pin.IN)

def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def on_receive(data):
    
    # output

    
    # input
    
    value=button.value()
    ws.send_dict['C'] = value
    value=int(interval_mapping(potentiometer.read_u16(),0,65535,0,100))
    ws.send_dict['B'] = value
    

ws.on_receive = on_receive

def main():
    print("start")
    while True:
        ws.loop()

main()



