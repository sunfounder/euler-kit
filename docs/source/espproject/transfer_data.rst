.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

1.3 What Data is Transferred between APP & Pico？
===================================================

#. From APP to Pico

    Let's take a look at what kind of data Pico will get from the APP. Print ``data`` directly in ``on_receive``.

    .. note::

        * Open the ``1.3_ws_test_print.py`` file under the path of ``euler-kit\esp8266`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.
        * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.
        * Each time you rerun the code, you need to connect your device's Wi-Fi to ``my_esp8266``, then turn on SunFounder Controller and reconnect.


    .. code-block:: python
        :emphasize-lines: 21,22

        from ws import WS_Server
        import json
        import time

        NAME = 'my_esp8266'

        ## Client Mode
        # WIFI_MODE = "sta"
        # SSID = "YOUR SSID HERE"
        # PASSWORD = "YOUR PASSWORD HERE"

        ## AP Mode
        WIFI_MODE = "ap"
        SSID = ""
        PASSWORD = "12345678"


        ws = WS_Server(name=NAME, mode=WIFI_MODE, ssid=SSID, password=PASSWORD)
        ws.start()

        def on_receive(data):
            print(data)

            # output

            # input

        ws.on_receive = on_receive

        def main():
            print("start")
            while True:
                ws.loop()

        main()

    You will see the data for each area in the Shell. When we drag the Slider in the H area, the value of the H area will change. This is because we only add one control widget (H area). The widget in the G area is not used for control but only for show.


    |sc_ws_test_data|


    We can also add other control widgets, and use the same method to view the values ​​sent by these widgets to Pico.

    You can get the value of the corresponding widget by just using the label. As shown below, print the value of the H widget:

    .. note::

        * Open the ``1.3_ws_test_print_h.py`` file under the path of ``euler-kit\esp8266`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.
        * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.
        * Each time you rerun the code, you need to connect your device's Wi-Fi to ``my_esp8266``, then turn on SunFounder Controller and reconnect.

    .. code-block:: python
        :emphasize-lines: 22,23

        from ws import WS_Server
        import json
        import time

        NAME = 'my_esp8266'

        ## Client Mode
        # WIFI_MODE = "sta"
        # SSID = "YOUR SSID HERE"
        # PASSWORD = "YOUR PASSWORD HERE"

        ## AP Mode
        WIFI_MODE = "ap"
        SSID = ""
        PASSWORD = "12345678"


        ws = WS_Server(name=NAME, mode=WIFI_MODE, ssid=SSID, password=PASSWORD)
        ws.start()


        def on_receive(data):
            print(data['H'])

            # output

            # input


        ws.on_receive = on_receive

        def main():
            print("start")
            while True:
                ws.loop()

        main()
    
    .. code-block::

        >>> %Run -c $EDITOR_CONTENT
            Connecting
            WebServer started on ws://192.168.4.1:8765
            start
            Connected from 192.168.4.3
            34
            50
            87

#. From Pico to APP
    
    Use the ``send_dict`` function to show the value in G Widget.

    .. note::

        * Open the ``1.3_ws_test_input.py`` file under the path of ``euler-kit\esp8266`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.
        * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.
        * Each time you rerun the code, you need to connect your device's Wi-Fi to ``my_esp8266``, then turn on SunFounder Controller and reconnect.

    .. code-block:: python
        :emphasize-lines: 21,22,23,30,31

        from ws import WS_Server
        import json
        import time

        NAME = 'my_esp8266'

        ## Client Mode
        # WIFI_MODE = "sta"
        # SSID = "YOUR SSID HERE"
        # PASSWORD = "YOUR PASSWORD HERE"

        ## AP Mode
        WIFI_MODE = "ap"
        SSID = ""
        PASSWORD = "12345678"


        ws = WS_Server(name=NAME, mode=WIFI_MODE, ssid=SSID, password=PASSWORD)
        ws.start()

        led = machine.PWM(machine.Pin(15))
        led.freq(1000)
        potentiometer = machine.ADC(28)

        def on_receive(data):

            # output

            # input
            value=potentiometer.read_u16()
            ws.send_dict['G'] = value # the value show on the G area


        ws.on_receive = on_receive

        def main():
            print("start")
            while True:
                ws.loop()

        main()

    After running the code, turn the potentiometer and you will be able to see the value of the G widget change.


#. Widget List

* Control Widgets

|sc_app_control_widget|

* Show Widgets

|sc_app_show_widget|
