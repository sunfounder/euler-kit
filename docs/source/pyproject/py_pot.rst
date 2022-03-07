Turn the Knob
===========================

In the previous projects, we have used the digital input on the Pico.
For example, a button can change the pin from low level (off) to high level (on). This is a binary working state.

However, Pico can receive another type of input signal: analog input.
It can be in any state from fully closed to fully open, and has a range of possible values.
The analog input allows the microcontroller to sense the light intensity, sound intensity, temperature, humidity, etc. of the physical world.

Usually, a microcontroller needs an additional hardware to implement analog input-the analogue-to-digital converter (ADC).
But Pico itself has a built-in ADC for us to use directly.


|pin_adc|

Pico has three GPIO pins that can use analog input, GP26, GP27, GP28. That is, analog channels 0, 1, and 2.
In addition, there is a fourth analog channel, which is connected to the built-in temperature sensor and will not be introduced here.

In this project, we try to read the analog value of potentiometer.

* :ref:`cpn_pot`


**Wiring**

|sch_pot|

|wiring_pot|

#. Connect 3V3 and GND of Pico to the power bus of the breadboard.
#. Insert the potentiometer into the breadboard, its three pins should be in different rows.
#. Use jumper wires to connect the pins on both sides of the potentiometer to the positive and negative power bus respectively.
#. Connect the middle pin of the potentiometer to GP28 with a jumper wire.
#. Connect the anode of the LED to the GP15 pin through a 220Ω resistor, and connect the cathode to the negative power bus.


**Code**

When the program is running, we can see the analog value currently read by the GP28 pin in the shell. 
Turn the knob, and the value will change from 0 to 65535.
At the same time, the brightness of the LED will increase as the analog value increases.

.. code-block:: python

    import machine
    import utime

    potentiometer = machine.ADC(28)
    led = machine.PWM(machine.Pin(15))
    led.freq(1000)

    while True:
        value=potentiometer.read_u16()
        print(value)
        led.duty_u16(value)
        utime.sleep_ms(200)

**How it works?**

.. code-block:: python

    potentiometer = machine.ADC(28)

Access the ADC associated with a source identified by id. In this example it is GP28.

.. code-block:: python

    potentiometer.read_u16()

Take an analog reading and return an integer in the range 0-65535. The return value represents the raw reading taken by the ADC, scaled such that the minimum value is 0 and the maximum value is 65535.


* `machine.ADC - MicroPython Docs <https://docs.micropython.org/en/latest/library/machine.ADC.html>`_