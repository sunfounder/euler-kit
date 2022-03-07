Plant Monitor
=============

|sc_img_plant_monitor|

|sc_app_plant_monitor|

这是一个智能灌溉系统，它会检测当前环境的温度和湿度，打印到APP里。
当你按下APP上的pump按钮，它将会为植物补充水分。待水量抵达water level sensor的位置后自动停止泵水。

.. note:: 由于水泵长时间运行会产生较大电流，导致pico死机。此时请将pico的run引脚接入低电平后约一秒后释放，以此复位pico。




**Wiring**

|wiring_app_plant_monitor|



**Code**

.. note:: 将示例名改为 ``main.py`` ,可以使该示例在开机后自动运行。

.. code-block:: python

    from ws import WS_Server
    import json
    import time

    from machine import Pin, I2C
    from dht import DHT11


    # dht 11
    pin = Pin(16, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)

    # water sensor
    water_sensor = machine.ADC(28)

    # pump
    motor1A = machine.Pin(14, machine.Pin.OUT)
    motor2A = machine.Pin(15, machine.Pin.OUT)


    # ESP8266
    NAME = 'my_esp8266'

    # Client Mode
    # WIFI_MODE = "sta"
    # SSID = "MakerStarsHall"
    # PASSWORD = "sunfounder"

    # AP Mode
    WIFI_MODE = "ap"
    SSID = ""
    PASSWORD = "12345678"

    ws = WS_Server(name=NAME, mode=WIFI_MODE, ssid=SSID, password=PASSWORD)
    ws.start()



    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def on_receive(data):
        
        # output
        # start pumping
        if data['G'] == True :
            motor1A.high()
            motor2A.low()
        
        # input
        # show dht11 message
        sensor.measure()
        value = sensor.temperature
        ws.send_dict['C'] = value
        value = sensor.humidity
        ws.send_dict['B'] = value
        
        # show water level sensor message
        value = water_sensor.read_u16()
        ws.send_dict['P'] = value
        # stop pumping
        if value>=10000:
            motor1A.low()
            motor2A.low()

    ws.on_receive = on_receive

    def main():
        print("start")
        while True:

            ws.loop()

    main()
