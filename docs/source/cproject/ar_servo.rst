.. _ar_servo:

3.7 - Swinging Servo
=======================

In this kit, in addition to LED and passive buzzer, there is also a device controlled by PWM signal, Servo.

Servo is a position (angle) servo device, which is suitable for those control systems that require constant angle changes and can be maintained. It has been widely used in high-end remote control toys, such as airplanes, submarine models, and remote control robots.

Now, try to make the servo sway!

* :ref:`cpn_servo`

**Schematic**

|sch_servo|

**Wiring**

|wiring_servo|

* Orange wire is signal and connected to GP15.
* Red wire is VCC and connected to VBUS(5V).
* Brown wire is GND and connected to GND.

**Code**


.. note::

   * You can open the file ``3.7_swinging_servo.ino`` under the path of ``euler-kit/arduino/3.7_swinging_servo``. 
   * Or copy this code into **Arduino IDE**.
   * For detailed tutorials, please refer to :ref:`open_run_code_ar`.
   * Or run this code directly in the `Arduino Web Editor <https://create.arduino.cc/projecthub/Arduino_Genuino/getting-started-with-arduino-web-editor-on-various-platforms-4b3e4a>`_.

    Don't forget to select the Raspberry Pi Pico board and the correct port before clicking the Upload button.
    

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/d52a67be-be6b-4cbf-b411-810160f56928/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


When the program is running, we can see the Servo Arm swinging back and forth from 0° to 180°. 


**How it works?**

By calling the library ``Servo.h``, you can drive the servo easily. 

.. code-block:: arduino

    #include <Servo.h> 

**Library Functions：**

.. code-block:: arduino

    Servo

Create **Servo** object to control a servo.

.. code-block:: arduino

    uint8_t attach(int pin); 

Turn a pin into a servo driver. Calls pinMode. Returns 0 on failure.

.. code-block:: arduino

    void detach();

Release a pin from servo driving.

.. code-block:: arduino

    void write(int value); 

Set the angle of the servo in degrees, 0 to 180.

.. code-block:: arduino

    int read();

Return that value set with the last write().

.. code-block:: arduino

    bool attached(); 

Return 1 if the servo is currently attached.