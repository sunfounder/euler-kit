.. _ar_relay:


2.16 - Control Another Circuit
=================================

In our daily life, we can press the switch to light up or turn off the lamp.
But what if you want to control the lamp with Pico so that it can turn off automatically after ten minutes?

A relay can help you accomplish this idea.

A relay is actually a special kind of switch that is controlled by one side of the circuit (usually a low-voltage circuit) and used to control the other side of the circuit (usually a high-voltage circuit).
This makes it practical to modify our home appliances to be controlled by a program, to become smart devices, or even to access the Internet.

.. warning::
    Modification of electrical appliances comes with great danger, do not try it lightly, please do it under the guidance of professionals.

* :ref:`cpn_relay`

Here we only use a simple circuit powered by a breadboard power module as an example to show how to control it using relay.

* :ref:`cpn_power_module`

**Wiring**

First, build a low-voltage circuit for controlling a relay.
Driving the relay requires a high current, so a transistor is needed, and here we use the S8050.

|sch_relay_1|

|wiring_relay_1|



A diode (continuity diode) is used here to protect the circuit. The cathode is the end with the silver ribbon connected to the power supply, and the anode is connected to the transistor.

When the voltage input changes from High (5V) to Low (0V), the transistor changes from saturation (amplification, saturation, and cutoff) to cutoff, and there is suddenly no way for current to flow through the coil. 

At this point, if this freewheeling diode does not exist, the coil will produce a self-induced electric potential at both ends that is several times higher than the supply voltage, and this voltage plus the voltage from the transistor power supply is enough to burn it.  

After adding the diode, the coil and the diode instantly form a new circuit powered by the energy stored in the coil to discharge, thus avoiding the excessive voltage will damage devices such as transistors on the circuit.

* :ref:`cpn_diode`    
* `Flyback Diode - Wikipedia <https://en.wikipedia.org/wiki/Flyback_diode>`_

At this point the program is ready to run, and after running you will hear the "tik tok" sound, which is the sound of the contactor coil inside the relay sucking and breaking.

Then we connect the two ends of the load circuit to pins 3 and 6 of the relay respectively.

..(Take the simple circuit powered by the breadboard power module described in the previous article as an example.)

|sch_relay_2|

|wiring_relay_2|

At this point, the relay will be able to control the load circuit on and off.


**Code**


.. note::

   * You can open the file ``2.16_relay.ino`` under the path of ``euler-kit/arduino/2.16_relay``. 
   * Or copy this code into **Arduino IDE**.
   * Or run this code directly in the `Arduino Web Editor <https://create.arduino.cc/projecthub/Arduino_Genuino/getting-started-with-arduino-web-editor-on-various-platforms-4b3e4a>`_.

    Don't forget to select the Raspberry Pi Pico board and the correct port before clicking the Upload button.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/3be98f10-8223-49f2-8238-2acc53ebbf80/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


When the code is run, the relay will switch the operating state of the controlled circuit every two seconds.
You can manually comment out one of the lines to further clarify the correspondence between the relay circuit and the load circuit.


**What More?**

Pin 3 of the relay is normally open and only turns on when the contactor coil is operating; pin 4 is normally closed and turns on when the contactor coil is energized.
Pin 1 is connected to pin 6 and is the common terminal of the load circuit.

By switching one end of the load circuit from pin 3 to pin 4, you will be able to get exactly the opposite operating state.