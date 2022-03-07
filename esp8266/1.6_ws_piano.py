from ws import WS_Server
import json
import time
import _thread


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
buzzer = machine.PWM(machine.Pin(14))

#note 
note = [262,294,330,349,392,440,494,523]

#melody
NOTE_C4 = 262
NOTE_G3 = 196
NOTE_A3 = 220
NOTE_B3 = 247
melody =[NOTE_C4,NOTE_G3,NOTE_G3,NOTE_A3,NOTE_G3,NOTE_B3,NOTE_C4]

def light_led():
    global brightness
    brightness = 65535
    led.duty_u16(brightness)


def tone(pin,frequency):
    pin.freq(frequency)
    pin.duty_u16(30000)
    light_led()
    
def noTone(pin):
    pin.duty_u16(0)

def music_box(duration):
    for n in melody:
        tone(buzzer,n)
        time.sleep_ms(duration)
        noTone(buzzer)
        time.sleep_ms(duration)
    noTone(buzzer)
        

def on_receive(data):
  
    global bpm_flag,gap,brightness
    bpm = data['H']
    bpm_flag = data['G']
    gap = 60 * 1000 / bpm
    
    # fade led
    if brightness >= 6000:
        brightness = brightness-30000
        led.duty_u16(brightness)

    # music box
    if data['G'] == True:
        music_box(int(gap/4))
        return
    
    # piano
    if data['N'] == True:
        tone(buzzer,note[0])
    elif data['O'] == True:
        tone(buzzer,note[1])
    elif data['P'] == True:
        tone(buzzer,note[2])
    elif data['S'] == True:
        tone(buzzer,note[3])
    elif data['M'] == True:
        tone(buzzer,note[4])
    elif data['Q'] == True:
        tone(buzzer,note[5])
    elif data['R'] == True:
        tone(buzzer,note[6])
    else:
        noTone(buzzer)
        
    
ws.on_receive = on_receive

gap = 500
bpm_flag = False
brightness = 0

def main():
    print("start")
    while True:
        ws.loop()

main()


