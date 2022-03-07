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

led = machine.PWM(machine.Pin(15))
led.freq(1000)
potentiometer = machine.ADC(28)

def on_receive(data):
    print(data)
    
    # output
    value = data['H']
    led.duty_u16(value*655)
    
    # input
    value=potentiometer.read_u16()
    ws.send_dict['G'] = value

ws.on_receive = on_receive

def main():
    print("start")
    while True:
        ws.loop()

main()

