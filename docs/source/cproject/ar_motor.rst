.. _ar_motor:

3.5 - Small Fan
=======================
Now we use the L293D to drive the DC motor to make it rotate clockwise and counterclockwise. 
Since the DC motor requires a relatively large current, for safety reasons, 
here we use a power module to supply power to the motor.

* :ref:`cpn_motor`
* :ref:`cpn_l293d`
* :ref:`cpn_power_module`


**Schematic**

|sch_motor|

In this circuit, you will see that the button is connected to the RUN pin. This is because the motor is operating with too much current, which may cause the Pico to disconnect from the computer, and the button needs to be pressed (for the Pico's **RUN** pin to receive a low level) to reset.

L293D is a motor driver chip, EN is connected to 5V to make L293D work. 1A and 2A are the inputs connected to GP15 and GP14 respectively; 1Y and 2Y are the outputs connected to the two ends of the motor.

Y (output) is in phase with A (input), so if GP15 and GP14 are given different levels respectively, the direction of motor rotation can be changed.




**Wiring**

|wiring_motor|

Since DC motors require a high current, we use a power supply module to power the motor here for safety reasons.

**Code**

.. note::

   * You can open the file ``3.5_small_fan.ino`` under the path of ``euler-kit/arduino/3.5_small_fan``. 
   * Or copy this code into **Arduino IDE**.
   * Or run this code directly in the `Arduino Web Editor <https://create.arduino.cc/projecthub/Arduino_Genuino/getting-started-with-arduino-web-editor-on-various-platforms-4b3e4a>`_.

    Don't forget to select the Raspberry Pi Pico board and the correct port before clicking the Upload button.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/26d75a18-6b91-40f4-80ab-f2cdf58644ac/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Once the program is running, the motor will rotate back and forth in a regular pattern.


.. note::

    * If you can not upload the code again, this time you need to connect the **RUN** pin on the Pico with a wire to GND to reset it, and then unplug this wire to run the code again.
    * This is because the motor is operating with too much current, which may cause the Pico to disconnect from the computer. 

    |wiring_run_reset|