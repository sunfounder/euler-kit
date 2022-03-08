.. _py_button:

2.5 Reading Button Value
==============================================

From the name of GPIO (General-purpose input/output), we can see that these pins have both input and output functions. 
In the previous lessons, we used the output function, in this chapter we will use the input function to input read the button value.

* :ref:`cpn_button`


**Schematic**

|sch_button|

One side of the button pin is connected to 3.3v, and the other side pin is connected to GP14, so when the button is pressed, GP14 will be high. However, when the button is not pressed, GP14 is in a suspended state and may be high or low. In order to get a stable low level when the button is not pressed, GP14 needs to be reconnected to GND through a 10K pull-down resistor.



**Wiring**

|wiring_button|


.. Let's follow the direction of the circuit to build the circuit!

.. 1. Connect the 3V3 pin of Pico to the positive power bus of the breadboard.
.. #. Insert the button into the breadboard and straddle the central dividing line.

.. note::
    We can think of the four-legged button as an H-shaped button. Its left (right) two feet are connected, which means that after it straddles the central dividing line, it will connect the two half rows of the same row number together. (For example, in my circuit, E23 and F23 have been connected, as are E25 and F25).

    Before the button is pressed, the left and right sides are independent of each other, and current cannot flow from one side to the other.

.. #. Use a jumper wire to connect one of the button pins to the positive bus (mine is the pin on the upper right).
.. #. Connect the other pin (upper left or lower left) to GP14 with a jumper wire.
.. #. Use a 10K resistor to connect the pin on the upper left corner of the button and the negative bus.
.. #. Connect the negative power bus of the breadboard to Pico's GND.

**Code**

.. note::

    * Open the ``2.5_read_button_value.py`` file under the path of ``euler-kit/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    button = machine.Pin(14, machine.Pin.IN)
    while True:
        if button.value() == 1:
            print("You pressed the button!")
            utime.sleep(1)

After the code runs, when you press the button, the shell will print "You pressed the button!

**Pull-up Working Mode**


Next is the wiring and code when the button in the pull-up working mode, please try it.

|sch_button_pullup|

|wiring_button_pullup|

The only difference you will see with the pull-down mode is that the 10K resistor is connected to 3.3V and the button is connected to GND, so that when the button is pressed, GP14 will get a low level, which is the opposite of the value obtained in pull-down mode.
So just change this code to ``if button.value() == 0:``.


Also see the reference here:  

* `machine.Pin <https://docs.micropython.org/en/latest/library/machine.Pin.html>`_