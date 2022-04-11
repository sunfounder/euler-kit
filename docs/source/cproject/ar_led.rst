.. _ar_led:



2.1 - Hello, LED! 
=======================================

Just as printing “Hello, world!” is the first step in learning to program, using a program to drive an LED is the traditional introduction to learning physical programming.

* :ref:`cpn_led`


**Schematic**

|sch_led|

The principle of this circuit is simple and the current direction is shown in the figure. When GP15 outputs high level(3.3v), the LED will light up after the 220ohm current limiting resistor. When GP15 outputs low level (0v), the LED will turn off.

**Wiring**

|wiring_led|

Let us follow the direction of the current to build the circuit!

1. Here we use the electrical signal from the GP15 pin of the Pico board to make the LED work, and the circuit starts from here.
#. The current needs to pass through a 220 ohm resistor (used to protect the LED). Insert one end (either end) of the resistor into the same row as the Pico GP15 pin (row 20 in my circuit), and insert the other end into the free row of the breadboard (row 24 in my circuit).
#. Pick up the LED, you will see that one of its leads is longer than the other. Insert the longer lead into the same row as the end of the resistor, and connect the shorter lead across the middle gap of the breadboard to the same row.
#. Insert the male-to-male (M2M) jumper wire into the same row as the LED short pin, and then connect it to the negative power bus of the breadboard.
#. Use a jumper to connect the negative power bus to the GND pin of Pico.


**Code**

.. note::

   * You can open the file ``2.1_hello_led.ino`` under the path of ``euler-kit/arduino/2.1_hello_led``. 
   * Or copy this code into **Arduino IDE**.
   * For detailed tutorials, please refer to :ref:`open_run_code_ar`.
   * Or run this code directly in the `Arduino Web Editor <https://docs.arduino.cc/cloud/web-editor/tutorials/getting-started/getting-started-web-editor>`_.

    Don't forget to select the Raspberry Pi Pico board and the correct port before clicking the Upload button.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/898b8ba7-9bdf-468d-9181-ca8535e8dca6/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

.. .. code-block:: C

..     const int ledPin = 15;

..     // the setup function runs once when you press reset or power the board
..     void setup() {
..     // initialize digital pin as an output.
..         pinMode(ledPin, OUTPUT);
..     }

..     // the loop function runs over and over again forever
..     void loop() {
..         digitalWrite(ledPin, HIGH);   // turn the LED on (HIGH is the voltage level)
..         delay(1000);                       // wait for a second
..         digitalWrite(ledPin, LOW);    // turn the LED off by making the voltage LOW
..         delay(1000);                       // wait for a second
..     }

After the code runs, you will see the LED blinking.

**How it works?**

Here, we connect the LED to the digital pin 15, so we need to declare an int variable called ledpin at the beginning of the program and assign a value of 15.

.. code-block:: C

    const int ledPin = 15;


Now, initialize the pin in the ``setup()`` function, where you need to initialize the pin to ``OUTPUT`` mode.

.. code-block:: C

    void setup() {
        pinMode(ledPin, OUTPUT);
    }

In ``loop()``, ``digitalWrite()`` is used to provide 3.3V high level signal for ledpin, which will cause voltage difference between LED pins and light LED up.

.. code-block:: C

    digitalWrite(ledPin, HIGH);

If the level signal is changed to LOW, the ledPin’s signal will be returned to 0 V to turn LED off.

.. code-block:: C

    digitalWrite(ledPin, LOW);


An interval between on and off is required to allow people to see the change, 
so we use a ``delay(1000)`` code to let the controller do nothing for 1000 ms.

.. code-block:: C

    delay(1000);   
