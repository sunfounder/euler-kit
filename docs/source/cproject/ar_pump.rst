.. _ar_pump:

3.6 - Pumping
=======================


Small centrifugal pumps are suitable for projects with automatic plant watering.
It can also be used to make tiny smart water features.

Its power component is an electric motor, driven in exactly the same way as a normal motor.

* :ref:`cpn_pump`
* :ref:`cpn_motor`
* :ref:`cpn_l293d`
* :ref:`cpn_power_module`

.. note::

    #. Connect the tube to the motor outlet, submerge the pump in water, and then power it on.
    #. You need to make sure that the water level is always higher than the motor. Idling may damage the motor due to heat generation and will also generate noise.
    #. If you are watering plants, you need to avoid soil being drawn in, as this can clog the pump.
    #. If water does not come out of the tube, there may be residual water in the tube blocking the air flow and needs to be drained first.


**Schematic**

|sch_pump|

In this circuit, you will see that the button is connected to the RUN pin. This is because the motor is operating with too much current, which may cause the Pico to disconnect from the computer, and the button needs to be pressed (for the Pico's **RUN** pin to receive a low level) to reset.

L293D is a motor driver chip, EN is connected to 5V to make L293D work. 1A and 2A are the inputs connected to GP15 and GP14 respectively; 1Y and 2Y are the outputs connected to the two ends of the motor.

Y (output) is in phase with A (input), so if GP15 and GP14 are given different levels respectively, the direction of motor rotation can be changed.


**Wiring**

|wiring_pump|

**Code**

.. note::

   * You can open the file ``3.6_pumping.ino`` under the path of ``euler-kit/arduino/3.6_pumping``. 
   * Or copy this code into **Arduino IDE**.
   * Or run this code directly in the `Arduino Web Editor <https://create.arduino.cc/projecthub/Arduino_Genuino/getting-started-with-arduino-web-editor-on-various-platforms-4b3e4a>`_.

    Don't forget to select the Raspberry Pi Pico board and the correct port before clicking the Upload button.
    


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/4194feb8-92d4-4ab4-b51c-286d014af0a6/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe> 



After the code is run, the pump starts working and you will see water flowing out of the tube at the same time.


.. note::

    * If you can not upload the code again, this time you need to connect the **RUN** pin on the Pico with a wire to GND to reset it, and then unplug this wire to run the code again.
    * This is because the motor is operating with too much current, which may cause the Pico to disconnect from the computer. 

    |wiring_run_reset|