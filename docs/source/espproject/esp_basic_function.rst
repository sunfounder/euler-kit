.. _first_time_use:

1.1 First-time Use the APP
==============================


This section will guide you to complete the communication between Sunfounder Controller APP and Pico, you can read the value of the potentiometer on the APP, and you can also control the LED on and off through the APP.


**How to do?**

#. Build a circuit.

    |wiring_app_test|

#. Upload the library.

    Reference :ref:`download_upload` to download the code and upload the library. But in this project, you need to upload ``ws.py`` from the ``euler-kit/esp8266/`` path to the Raspberry Pi Pico.

    |sc_upload_ws|

#. Run ``1.1_ws_test.py`` file.

    Double click the ``1.1_ws_test.py`` file under the ``euler-kit/esp8266/`` path, then click **run current script** button or just press F5 to run it.

    After running the program, you will see the IP address and the ``start`` prompt in the Shell.

    .. warning::

        If the wiring is OK, but still no successful connection prompt after several runs, the firmware of ESP8266 module may need to be re-burned, please refer to :ref:`burn_firmware` for details.

    |sc_run_test|

#. Connect to ESP8266.

    Find **my_esp8266** on the WLAN of the mobile phone (tablet), enter the password (12345678) and connect to it. 
    
    |sc_app_my_esp8266|

    The default used in ``1.1_ws_test.py`` is `AP mode <https://www.windowscentral.com/whats-difference-between-access-point-ap-mode-and-router-mode#:~:text=AP%20mode%20allows%20you%20to,individual%2C%20self%2Dcontained%20networks>`_. So after you connect, there will be a prompt telling you that there is no Internet access on this WLAN network, please choose to continue connecting.

    |sc_app_connect_anyway|

#. Install Sunfounder Controller.

    Search for **Sunfounder Controller** in **APP Store** (or **Google Play**) and download it.

    |sc_app_install|

#. Connect to SunFounder Controller.
    
    Now open SunFounder Controller and click **Disconnected** in the upper right corner.

    |sc_app_click-disconnect|

    Because it is AP mode, it will connect automatically here. 
    
    .. note::
        If the connection has not been successful, please make sure the ``1.1_ws_test.py`` file is running properly and connect your device's Wi-Fi to ``my_esp8266``.

    |sc_app_auto_connect|

    After the connection is successful, the Thonny script will show the IP of the newly connected device:

    .. code-block::
        :emphasize-lines: 5

        >>> %Run -c $EDITOR_CONTENT
            Connecting
            WebServer started on ws://192.168.4.1:8765
            start
            Connected from 192.168.4.3    

#. Create a controller.

    Click the **+** button in the middle of the page, then the Create controller page will pop up. Enter the name of the controller, select **Blank** -> **Dual Stick** and click **Confirm**.

    |sc_app_add_new_controller|

    You will be able to see boxes (some are rectangles, some are squares), we need to adjust them to apply to ``1.1_ws_test.py``.

    Click on area **G** and select the **Number** widget.

    |sc_sec_number|

    Click on area **H** and sclect the **Slider** widget.

    |sc_sec_slide|

#. Save and Run the controller.
    
    Click the **Save/Edit** button and the controller will be saved. At the same time it enters the working state, and the empty widget box is hidden.

    Then click the **Run/Stop** button to get this controller running！

    |sc_run_save|

    * The value of the potentiometer will displayed on the **G** area.
    * If you slide the slider of the **H** box, the brightness of the LED will change.

    .. note::
        If it does not work as expected, or if it shows **disconnected**, make sure that the ``1.1_ws_test.py`` file is running properly and that your mobile device's Wi-Fi is connected to the ``my_esp8266``.



**FAQ**

#. Error during running code.

   * When the following error occurs, please check if the ESP8266 connection is stable.

    .. code-block:: 
        
        Traceback (most recent call last):
        File "<stdin>", line 43, in <module>
        File "<stdin>", line 41, in main
        File "ws.py", line 115, in loop
        File "ws.py", line 46, in read
        UnicodeError:

   * Then hit Stop to stop running the code, and then run the code again.

#. Each time you re-run the code, you need to reconnect your device (phone/tablet) WIFI to ``my_esp8266``, and then go to SunFounder Controller and click Disconnnected to reconnect.


#. If the connection has not been successful, or suddenly disconnect.please make sure the ``1.1_ws_test.py`` file is running properly and your mobile device is connected to ``my_esp8266``.