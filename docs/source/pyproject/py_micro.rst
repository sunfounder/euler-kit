.. _py_micro:

2.8 Press Gently
==========================

|img_micro_switch|

Micro Switch is also a 3-pin device, the sequence of the 3 pins are C (common pin), NO (normally open) and NC (normally closed) .

When the micro switch is not pressed, 1 (C) and 3 (NC) are connected together, when pressed 1 (C) and 2 (NO) are connected together.

* :ref:`cpn_limit_sw`


**Schematic**

|sch_limit_sw|

By default, GP14 is low and when pressed, GP14 is high.

The purpose of the 10K resistor is to keep the GP14 low during pressing.

The 104 ceramic capacitor is used here to eliminate jitter.



**Wiring**

|wiring_limit_sw|

.. 1. Connect the 3V3 pin of Pico to the positive power bus of the breadboard.
.. #. Insert the micro switch into the breadboard.
.. #. Use a jumper wire to connect NC pin of micro switch pin to the negative bus.
.. #. Connect the C pin to GP14 with a jumper wire.
.. #. Use a jumper wire to connect NO pin of micro switch pin to the positive bus
.. #. Use a 10K resistor to connect the C pin of the micro switch and the negative bus.
.. #. Use a 104 capacitor to connect the C pin of the micro switch and the negative bus to realize debounce that may arise from your toggle of switch.
.. #. Connect the negative power bus of the breadboard to Pico's GND.

.. When you press the switch, the circuit will be closed. 



**Code**

.. note::

    * Open the ``2.8_micro_switch.py`` file under the path of ``euler-kit/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    button = machine.Pin(14, machine.Pin.IN)
    while True:
        if button.value() == 1:
            print("The switch works!")
            utime.sleep(1)


After the program runs, when you toggle the slide switch to the right, "The switch works!" will appear in the shell.