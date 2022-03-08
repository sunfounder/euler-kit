.. _py_led_bar:

2.2 Display the Level
=============================


The first project is simply to make the LED blink. In this project let's use the LED Bar Graph, which is made up of 10 LEDs packaged into a plastic case, generally used to display power or volume levels.

|img_led_bar_pin|

* :ref:`cpn_led_bar`

**Schematic**

|sch_ledbar|

The LED Bar Graph contains 10 LEDs, each of which is individually controllable. Here, the anode of each of the 10 LEDs is connected to GP6~GP15, and the cathode is connected to a 220ohm resistor, and then to GND.



**Wiring**

|wiring_ledbar|

**Code**

.. note::

    * Open the ``2.2_display_the_level.py`` file under the path of ``euler-kit/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

    while True:
        for i in range(10):
            led[i].toggle()
            utime.sleep(0.2)

When the program is running, you will see the LEDs on the LED Bar Graph light up and then turn off in sequence.

**How it works?**

Each of the ten LEDs on the LED Bar needs to be controlled by a pin, which means that we define these ten pins.
If we define them one by one, it would be too much trouble. So, here we use ``Lists``.

.. note::
    Lists are the most basic data structure in Python, used to store multiple items in a single variable, and created using square brackets.

.. code-block:: python

    pin = [6,7,8,9,10,11,12,13,14,15]    

This line of code defines a list ``pin`` that stores the ten elements ``6,7,8,9,10,11,12,13,14,15`` inside it.
The list sets a pointer for each element inside. The first lead is 0, the second is 1, and so on.
Using this list as an example, ``pin[0]`` is ``6`` and ``pin[4]`` is ``10``.

Next, declare an empty list ``led`` that will be used to define ten LED objects.

.. code-block:: python

    led = []    

At this point, a direct operation on the array, such as printing ``led[0]``, will not work because the list is of length 0, and the lead 0 is looking for the first item, which does not exist. We need to add new items to it.

.. code-block:: python

    led.append(None)

This ``append()`` method adds a new item to the end of the list, and now the list ``led`` has its first item, of length 1, and ``led[0]`` becomes a valid element, even though its current value is ``None`` (which stands for null).

Next, we define ``led[0]`` as the first LED object, which is the LED connected to pin 6.

.. code-block:: python

    led[0] = machine.Pin(6, machine.Pin.OUT)

This completes the definition of the first LED object.

We went ahead and created those ten pin numbers as a list ``pin``, which we can use here to substitute into this line, this is to make it easier for us to do bulk operations.

.. code-block:: python

    led[0] = machine.Pin(pin[0], machine.Pin.OUT)

Using a ``for loop``, we have each of the 10 pins perform the above steps once, resulting in the following code.

.. code-block:: python

    import machine

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

* :ref:`Lists`
* :ref:`For Loops`

Use another ``for`` loop to make the ten LEDs on the LED Bar switch states one by one.

.. code-block:: python

    for i in range(10):
        led[i].toggle()
        utime.sleep(0.2)

Finally, put the above small piece of code into a ``while`` loop, and the code is done.

.. code-block:: python

    import machine
    import utime

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

    while True:
        for i in range(10):
            led[i].toggle()
            utime.sleep(0.2)


