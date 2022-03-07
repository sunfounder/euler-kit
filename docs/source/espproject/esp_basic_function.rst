First-time Use APP
==================


本篇将会指引你完成Sunfounder Controller APP与Pico之间的通信，你可以在APP上读取到电位器的值，也可以通过APP操控LED的亮灭。


**How to do?**

#. 搭建一个电路

   |wiring_app_test|

#. 上传库

    这个功能集成到了 ``ws.py`` 库中，它位于 ``esp8266_code`` 路径下，请先将其上传到Pico。

#. Coding


    To make things easier, let’s use ``ws_test.py`` in the tests folder (this code will be explained later) for the first Sunfounder Controller experiment!

    After running the program, Pico does not show anything, while the Thonny script shows the following message:

    .. code-block:: 

        >>> %Run -c $EDITOR_CONTENT
            Connecting
            WebServer started on ws://192.168.4.1:8765
            start    

#. Install Sunfounder Controller

    Search for Sunfounder Controller in APP Store (or Google Play) and download it.

    |sc_app_install|

#. Connect to mobile devices.

    Find **my_esp8266** on the WLAN of the mobile phone (tablet), enter the password (12345678) and connect to it. This is an ``AP`` released by Pico RDP and is not connected to the World Wide Web.
    
    If you need to keep the phone (tablet) network, you can switch to ``STA`` mode, which will be discussed later.

    After the connection is successful, the Thonny script will show the IP of the newly connected device:

    .. code-block:: python
        :emphasize-lines: 5

        >>> %Run -c $EDITOR_CONTENT
            Connecting
            WebServer started on ws://192.168.4.1:8765
            start
            Connected from 192.168.4.3    

#. Open **Sunfounder Controller** , and you will see the home page，click the red letter **disconnected** on the top right corner to complete the connection between pico and the phone (tablet).

    |sc_app_add_new_controller|

    .. note:: It should be noted that the Sunfounder Controller can connect successfully only when the device is running the program (you will need to reconnect after re-burning the code).

    * The big **plus** button in the middle can create a controller, and you can create multiple controller schemes in Sunfounder Controller.
    * Click on the **exclamation mark** icon in the upper left corner to view "ABOUT US"
    * The letter on the upper right shows the current connection status of Sunfounder Controller. You will need to click here to connect to the mobile device.
    * The **edit** icon allows you to delete redundant controllers.
    
    
#. Create a controller.

    点击大的 **+** 号，会弹出Create controller选项，选择 Blank->Dual Stick.

    |sc_app_create_controller|

    You will be able to see boxes (some are rectangles, some are squares), we need to adjust them to apply to ``ws_test.py``.

    |sc_app_interface|

    Click on area G and select the **Number** widget.

    |sc_app_add_number|

    Click on area H and sclect the **Slider** widget。

    |sc_app_add_slider|

    Click the **save** icon at the top right, and the controller will be saved. At the same time it enters the working state, and the empty widget box is hidden.
    
    At this time, the original **save** icon will become an **edit** icon, click on it to return to the edit state to adjust the widget.

    |sc_app_add_saved|

#. Click the run icon next to the edit icon, pico finally starts to move！
    

    If it fails to proceed as expected, or **Disconnected** is displayed next to the **Run** icon, please reconnect the pico to the phone (tablet), and try again!
    
    * The G box on the Sunfounder Controller will display the value of the potentiometer.
    * If you slide the slider of the H box, the brightness of the LED will change.

**How it works?**

The communication between pico and Sunfounder Controller is based on the ``websocket protocol``.

* `WebSocket - Wikipedia <https://en.wikipedia.org/wiki/WebSocket>`_

The specific workflow of APP Control gameplay is as follows:

    |ws_flowchart|

.. code-block:: python

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
        # write control codes here.
        pass
        
        # write sensor codes here.
        pass

    ws.on_receive = on_receive

    def main():
        print("start")
        while True:
            ws.loop()

    main()


This code constitutes the basic framework of APP control. Here, you need to pay attention to the following two parts:

1. Setup websocket

    There are two connection mode between Sunfounder Controller and Pico: One is **AP** mode, the other is **STA** mode.

    * **AP Mode**: You need to connect Sunfounder Contorller to the hotspot released by pico.
    * **STA Mode**: You need to connect Sunfounder Controller and pico to the same LAN.
    
    The default connection mode is **AP Mode**: The car releases the hotspot (the Wifi name is ``NAME`` in the code, here is ``my_esp8266``), the mobile phone (tablet) is connected to this WLAN. 
    This mode allows you to remotely control pico in any situation, but will make your phone (tablet) temporarily unable to connect to the Internet.

    .. code-block:: python
        :emphasize-lines: 3,4,5,6,8,9,10,11

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

    You can also use **STA** mode: Let the pico connects to your home WLAN, and your mobile phone (tablet) should also be connected to the same WLAN. 
    
    This mode is opposite to the **AP** mode and will not affect the normal use of the mobile phone (tablet), but will limit your pico from leaving the WLAN radiation range.

    The way to start this mode is to comment out the three lines under ``## AP Mode``, uncomment the three lines under ``## Client Mode``, and change the SSID and PASSWORD to your home WIFI at the same time.

    .. code-block:: python
        :emphasize-lines: 3,4,5,6,8,9,10,11

        NAME = 'my_esp8266'

        ## Client Mode
        WIFI_MODE = "sta"
        SSID = "Sunfounder"
        PASSWORD = "12345678"

        ## AP Mode
        # WIFI_MODE = "ap"
        # SSID = ""
        # PASSWORD = "12345678"

        ws = WS_Server(name=NAME, mode=WIFI_MODE, ssid=SSID, password=PASSWORD)    
        ws.start()

    After completing the connection mode settings, Websocket will set up and start the server.

    .. code-block:: python

        ws = WS_Server(name=NAME, mode=WIFI_MODE, ssid=SSID, password=PASSWORD)    
        ws.start()    

#. Responding

    The specific operation code of Pico and Sunfounder Controller is written on the ``on_receive()`` function. Usually, we need to write the codes for APP to control Pico on the front and the codes for APP to show Pico sensor data on the back.

    .. code-block:: python

        def on_receive(data):
            # write control codes here.
            pass
            
            # write sensor codes here.
            pass

        ws.on_receive = on_receive

    Finally, ``on_receive()`` will be assigned to ``ws.on_receive`` and then called by ``ws.loop``.

**Transfer Data**

* From APP to Pico

    Let's take a look at what kind of data Pico will get from the APP. Print ``data`` directly in ``on_receive``.

    .. code-block:: python

        def on_receive(data):
            print(data)

            # write control codes here.
            pass

            # write sensor codes here.
            pass


    You will be able to see the following string:

    .. code-block:: python

        {'C': None, 'B': None, 'M': None, 'L': None, 'O': None, 'N': None, 'I': None, 'H': 50, 'K': None, 'J': None, '': None, 'T': None, 'Q': None, 'P': None, 'S': None, 'E': None, 'D': None, 'G': None, 'F': None, 'A': None, 'R': None}

    As we can see, the value of H Box is 50 ( ``'H': 50``), and the others are None. This is because we only add one control widget (H Box). The widget in the D area is not used for control but only for show.

    We can also add other control widgets, and use the same method to view the values ​​sent by these widgets to Pico.

    You can get the value of the corresponding widget by just using the label. As shown below, print the value of the H Box widget:

    .. code-block:: python

        def on_receive(data):
            # write control codes here.
            print(data['H'])
            
            # write sensor codes here.
            pass
    
    .. code-block:: python

        >>> %Run -c $EDITOR_CONTENT
            Connecting
            WebServer started on ws://192.168.4.1:8765
            start
            Connected from 192.168.4.3
            50
            50
            50

* From Pico to APP
    
    Use the ``send_dict`` function to show the value in G Widget.

    .. code-block:: python

        def on_receive(data):
            # write control codes here.
            # print(data)        

            # write sensor codes here.
            value=potentiometer.read_u16()
            ws.send_dict['G'] = value

    运行代码后，旋转旋钮，你将能看到APP上的G widget数字变化。
