Swinging Servo
===================

In this kit, in addition to LED and passive buzzer, there is also a device controlled by PWM signal, Servo.

Servo is a position (angle) servo device, which is suitable for those control systems that require constant angle changes and can be maintained. It has been widely used in high-end remote control toys, such as airplanes, submarine models, and remote control robots.

Now, try to make the servo sway!

* :ref:`cpn_servo`

**Wiring**

|sch_servo|

|wiring_servo|

1. Press the Servo Arm into the Servo output shaft. If necessary, fix it with screws.
#. Connect **VBUS** (not 3V3) and GND of Pico to the power bus of the breadboard.
#. Connect the red lead of the servo to the positive power bus with a jumper.
#. Connect the yellow lead of the servo to the GP15 pin with a jumper wire.
#. Connect the brawn lead of the servo to the negative power bus with a jumper wire.


**Code**

When the program is running, we can see the Servo Arm swinging back and forth from 0° to 180°. 

:raw-code:

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