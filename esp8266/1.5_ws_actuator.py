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

lastdata = 0

def on_receive(data):
    
    # output
    global lastdata
    if data != lastdata:
        print(' ')
        print("F: ",data['F'])
        print("G: ",data['G'])
        print("H: ",data['H'])
        print("K: ",data['K'])
        print("Q: ",data['Q'])
    lastdata = data
    
    
    
    # input
    

ws.on_receive = on_receive

def main():
    print("start")
    while True:
        ws.loop()

main()


