Hello, LED! 
=======================================

就像打印“Hello, world!” 是学习编程的第一步，用程序驱动LED是学习物理编程的传统入门。

* :ref:`cpn_led`


**Wiring**


|sch_led|

|wiring_led|

Let us follow the direction of the current to build the circuit!

1. Here we use the electrical signal from the GP15 pin of the Pico board to make the LED work, and the circuit starts from here.
#. The current needs to pass through a 220 ohm resistor (used to protect the LED). Insert one end (either end) of the resistor into the same row as the Pico GP15 pin (row 20 in my circuit), and insert the other end into the free row of the breadboard (row 24 in my circuit).
#. Pick up the LED, you will see that one of its leads is longer than the other. Insert the longer lead into the same row as the end of the resistor, and connect the shorter lead across the middle gap of the breadboard to the same row.
#. Insert the male-to-male (M2M) jumper wire into the same row as the LED short pin, and then connect it to the negative power bus of the breadboard.
#. Use a jumper to connect the negative power bus to the GND pin of Pico.


**Code**

打开示例 ``3.1_hello_led.ino`` ，或者 copy this code into Arduino IDE and click "upload" to run it to make the LED blink!

Don't forget to switch the Board to Raspberry Pi Pico under the Tools menu.

.. code-block:: C

    const int ledPin = 15;

    // the setup function runs once when you press reset or power the board
    void setup() {
    // initialize digital pin as an output.
        pinMode(ledPin, OUTPUT);
    }

    // the loop function runs over and over again forever
    void loop() {
        digitalWrite(ledPin, HIGH);   // turn the LED on (HIGH is the voltage level)
        delay(1000);                       // wait for a second
        digitalWrite(ledPin, LOW);    // turn the LED off by making the voltage LOW
        delay(1000);                       // wait for a second
    }

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
