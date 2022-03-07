APP Actuator Widget
===================

1. 新建一个控制器，添加以下widget。

    |sc_app_actuator|

#. 运行 ``ws_actuator.py`` 示例。

#. 尝试拨动这些widget，你能在thonny的shell中看到相应的值变化。

#. 你可以将这些值用于控制电路，如控制LED。

   |wiring_app_actuator|


    .. code-block:: python

        from ws import WS_Server
        import json
        import time

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

        led = machine.PWM(machine.Pin(15))
        led.freq(1000)


        def interval_mapping(x, in_min, in_max, out_min, out_max):
            return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

        def on_receive(data):
            print(data)
            
            # output
            value = data['H']
            led.duty_u16(interval_mapping(value,0,100,0,65535))
            
            # input

        ws.on_receive = on_receive

        def main():
            print("start")
            while True:
                ws.loop()

        main()

**Widget List**

|sc_app_widget_act|