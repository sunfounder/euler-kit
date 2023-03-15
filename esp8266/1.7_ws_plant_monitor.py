from ws import WS_Server
import json
import time

from machine import Pin, I2C
from dht import DHT11


# dht11
pin = Pin(16, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)

# water sensor
water_sensor = machine.ADC(28)

# pump
motor1A = machine.Pin(14, machine.Pin.OUT)
motor2A = machine.Pin(15, machine.Pin.OUT)

motor1A.low()
motor2A.low()   

# ESP8266
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

def on_receive(data):
    # input
    # show dht11 message
    try:
        sensor.measure()
        value = sensor.temperature
        ws.send_dict['G'] = value
        value = sensor.humidity
        ws.send_dict['H'] = value
    except:
        pass
    
    # show water level sensor message
    value = water_sensor.read_u16()
    ws.send_dict['P'] = value 

    # output
    if 'M' in data.keys():
        # start pumping
        if data['M'] == True and value < 30000:
            motor1A.high()
            motor2A.low()
        else:
        # stop pumping
            motor1A.low()
            motor2A.low()

ws.on_receive = on_receive

def main():
    print("start")
    while True:
        ws.loop()

main()


