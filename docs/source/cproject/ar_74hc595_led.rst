Microchip - 74HC595
===========================

Integrated circuit (integrated circuit) is a kind of miniature electronic device or component, which is represented by the letter "IC" in the circuit.

A certain process is used to interconnect the transistors, resistors, capacitors, inductors and other components and wiring required in a circuit, fabricate on a small or several small semiconductor wafers or dielectric substrates, and then package them in a package , it has become a micro-structure with the required circuit functions; all of the components have been structured as a whole, making electronic components a big step towards micro-miniaturization, low power consumption, intelligence and high reliability.

The inventors of integrated circuits are Jack Kilby (integrated circuits based on germanium (Ge)) and Robert Norton Noyce (integrated circuits based on silicon (Si)).

This kit is equipped with an IC, 74HC595, which can greatly save the use of GPIO pins.
Specifically, it can replace 8 pins for digital signal output by writing an 8-bit binary number.

* `Binary number - Wikipedia <https://en.wikipedia.org/wiki/Binary_number>`_

* :ref:`74HC595`


**Wiring**

The 74HC595 is a 16-pin IC with a semi-circular notch on one side (usually the left side of the label). With the notch facing upwards, its pins are shown in the diagram below.

|img_74jc595_1|

Refer to the figure below to build the circuit.


|sch_74hc_led|

|wiring_74hc_led|

1. Connect 3V3 and GND of Pico to the power bus of the breadboard.
#. Insert 74HC595 across the middle gap into the breadboard.
#. Connect the GP0 pin of Pico to the DS pin (pin 14) of 74HC595 with a jumper wire.
#. Connect the GP1 pin of Pico to the STcp pin (12-pin) of 74HC595.
#. Connect the GP2 pin of Pico to the SHcp pin (pin 11) of 74HC595.
#. Connect the VCC pin (16 pin) and MR pin (10 pin) on the 74HC595 to the positive power bus.
#. Connect the GND pin (8-pin) and CE pin (13-pin) on the 74HC595 to the negative power bus.
#. Insert 8 LEDs on the breadboard, and their anode leads are respectively connected to the Q0~Q1 pins (15, 1, 2, 3, 4, 5, 6, 7) of 74HC595.
#. Connect the cathode leads of the LEDs with a 220Ω resistor in series to the negative power bus.


**Code**

.. :raw-code:

When the program is running, you can see the LEDs turning on one after another.

**How it works?**

Declare an array, store several 8 bit binary numbers that are used to change the working state of the eight LEDs controlled by 74HC595. 

.. code-block:: arduino

    int datArray[] = {B00000000, B00000001, B00000011, B00000111, B00001111, B00011111, B00111111, B01111111, B11111111};

Set ``STcp`` to low level first and then high level. It will generate a rising edge pulse of ``STcp``.

.. code-block:: arduino

    digitalWrite(STcp,LOW); 

``shiftOut()`` is used to shift out a byte of data one bit at a time, which means to shift a byte of data in datArray[num] to the shifting register with the DS pin. MSBFIRST means to move from high bits.

.. code-block:: arduino

    shiftOut(DS,SHcp,MSBFIRST,datArray[num]);

After ``digitalWrite(STcp,HIGH)`` is run, the STcp will be at the rising edge. At this time, the data in the shift register will be moved to the memory register. 

.. code-block:: arduino

    digitalWrite(STcp,HIGH);

A byte of data will be transferred into the memory register after 8 times. Then the data of memory register are output to the bus (Q0-Q7). For example, shiftout ``B00000001`` will light up the LED controlled by Q0 and turn off the LED controlled by Q1~Q7. 
