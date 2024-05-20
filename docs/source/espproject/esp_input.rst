.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

1.4 APP Display Widgets
===========================

#. Build the circuit.

    |wiring_app_display|

#. Create a new controller and add the following widgets.

    |sc_app_display|


#. Run ``1.4_ws_display.py``.

    .. note::

        * Open the ``1.4_ws_display.py`` file under the path of ``euler-kit/esp8266`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

        * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.


#. Each time you rerun the code, you need to connect your device's Wi-Fi to ``my_esp8266``, then turn on SunFounder Controller and reconnect.
#. After clicking the **Run/Stop** button, you can try to press a button or rotate a potentiometer and see how the values of the widgets in area **B** and area **C** on the app change.


**Widget List**

|sc_app_widget_dis|