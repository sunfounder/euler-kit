.. _py_led:

2.1 Hello, LED! 
=======================================

Just as printing "Hello, world!" is the first step in learning to program, using a program to drive an LED is the traditional introduction to learning physical programming.

* :ref:`cpn_led`

**Schematic**

|sch_led|

The principle of this circuit is simple and the current direction is shown in the figure. When GP15 outputs high level(3.3v), the LED will light up after the 220ohm current limiting resistor. When GP15 outputs low level (0v), the LED will turn off.

**Wiring**

|wiring_led|

Let us follow the direction of the current to build the circuit!

1. Here we use the electrical signal from the GP15 pin of the Pico board to make the LED work, and the circuit starts from here.
#. The current needs to pass through a 220 ohm resistor (used to protect the LED). Insert one end (either end) of the resistor into the same row as the Pico GP15 pin (row 20 in my circuit), and insert the other end into the free row of the breadboard (row 24 in my circuit).

    .. note::
        The color ring of the 220 ohm resistor is red, red, black, black and brown.

#. Pick up the LED, you will see that one of its leads is longer than the other. Insert the longer lead into the same row as the end of the resistor, and connect the shorter lead across the middle gap of the breadboard to the same row.
    
    .. note::
        The longer lead is known as the anode, and represents the positive side of the circuit; the shorter lead is the cathode, and represents the negative side. 

        The anode needs to be connected to the GPIO pin through a resistor; the cathode needs to be connected to the GND pin.

#. Insert the male-to-male (M2M) jumper wire into the same row as the LED short pin, and then connect it to the negative power bus of the breadboard.
#. Use a jumper to connect the negative power bus to the GND pin of Pico.


**Code**

.. note::

    * Open the ``2.1_hello_led.py`` file under the path of ``euler-kit/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    
    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.value(1)
        utime.sleep(2)
        led.value(0)
        utime.sleep(2)

After the code runs, you will see the LED blinking.


**How it works?**

.. The onboard LED is connected to the GP25 pin, if you carefully observe the Pico pinout, you will find that GP25 is one of the hidden pins, which means that we cannot use this pin (even if GP25 is used in exactly the same way as other pins). The advantage of this design is that even if you don't connect any external components, you can still have an OUTPUT to test the program.

The machine library is required to use GPIO.

.. code-block:: python

    import machine

This library contains all the instructions needed to communicate between MicroPython and Pico. 
Without this line of code, we will not be able to control any GPIOs.

The next thing to notice is this line:

.. code-block:: python

    led = machine.Pin(15, machine.Pin.OUT)

An object named ``led`` is defined here. Technically, it can be any name, it can be x, y, banana, Micheal_Jackson, or any character, 
but it is best to use a name that describes the purpose to ensure that the program is easy to read.

The second part of this line (the part after the equal sign) calls the Pin function in the machine library. It is used to tell Pico's GPIO pins what to do.
The Pin function has two parameters: the first parameter (15) means the pin you want to set; 
the second parameter (machine.Pin.OUT) tells that the pin should be used as an output instead of an input.

The above code has "set" the pin, but it will not light up the LED. To do this, we also need to "use" the pin.

.. code-block:: python

    led.value(1)

We have set up the GP15 pin before and named it led. The function of this statement is to set the value of ``led`` to 1 to turn the on-board LED on.

All in all, to use GPIO, these steps are necessary:

* **import machine library**: This is necessary, and it is only executed once in the entire program.
* **Set GPIO**: Each pin should be set before use.
* **Use**: Assign a value to the pin, each assignment will change the working state of the pin.

If we follow the above steps to write an example, then you will get code like this:

.. code-block:: python

    import machine
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)

Run it and you will be able to light up the LED.

Next, we try to add the "extinguished" statement:

.. code-block:: python

    import machine   
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)
    led.value(0)

According to the code line, this program will make the LED turn on first and then turn off. 
But when you use it, you will find that this is not the case. 
The LED never seems to light up. This is because the execution speed between the two lines is very fast, much faster than the reaction time of the human eye. 
The moment the LED lights up is not enough to make us perceive the light. To fix that, we need to slow down the program.

Insert the following statement into the second line of the program:

.. code-block:: python

    import utime

Like machine, the ``utime`` library is introduced here, which handles all time-related things, 
including the delay we need to use. Let's insert a delay sentence between ``led.value(1)`` and ``led.value(0)``, let them be separated by 2 seconds:

.. code-block:: python

    utime.sleep(2)

Now, the code should look like this. 
Run it, we will be able to see that the LED turns on first and then turns off:

.. code-block:: python

    import machine 
    import utime  
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)
    utime.sleep(2)
    led.value(0)

Finally, we should make the LED blink. 
Create a loop, rewrite the program, and it will be what you saw at the beginning of this chapter.

.. code-block:: python

    import machine
    import utime
    
    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.value(1)
        utime.sleep(2)
        led.value(0)
        utime.sleep(2)

* :ref:`While Loops`

**Learn More**


Usually, the library will have a corresponding API (Application Programming Interface) file. 
This is a concise reference manual that contains all the information needed to use this library, detailed introduction to functions, classes, return types, parameters, etc., and even comes with a tutorial.

In this article, we used MicroPython's ``machine`` and ``utime`` libraries, we can find more ways to use them here.

* `machine.Pin <https://docs.micropython.org/en/latest/library/machine.Pin.html>`_

* `utime <https://docs.micropython.org/en/latest/library/utime.html>`_

The following is also an example of making the LED blink, please try to read the API file to understand it!

.. note::

    * Open the ``2.1_hello_led_2.py`` file under the path of ``euler-kit/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.toggle()
        utime.sleep(1)