.. _py_rgb:


2.4 Colorful Light
==============================================

As we know, light can be superimposed. For example, mix blue light and green light give cyan light, red light and green light give yellow light.
This is called "The additive method of color mixing".

* `Additive color - Wikipedia <https://en.wikipedia.org/wiki/Additive_color>`_

Based on this method, we can use the three primary colors to mix the visible light of any color according to different specific gravity. For example, orange can be produced by more red and less green.

In this chapter, we will use RGB LED to explore the mystery of additive color mixing!

RGB LED is equivalent to encapsulating Red LED, Green LED, Blue LED under one lamp cap, and the three LEDs share one cathode pin.
Since the electric signal is provided for each anode pin, the light of the corresponding color can be displayed. By changing the electrical signal intensity of each anode, it can be made to produce various colors.

* :ref:`cpn_rgb`

**Schematic**

|sch_rgb|

The PWM pins GP13, GP14 and GP15 control the Red, Green and Blue pins of the RGB LED respectively, and connect the common cathode pin to GND. This allows the RGB LED to display a specific color by superimposing light on these pins with different PWM values.




**Wiring**

|img_rgb_pin|

An RGB LED has 4 pins: the longest pin is the common cathode pin, which is usually connected to GND, the left pin next to the longest pin is Red, and the 2 pins on the right are Green and Blue.

|wiring_rgb|

.. 1. Connect the GND pin of the Pico to the negative power bus of the breadboard.
.. #. Insert the RGB LED into the breadboard so that its four pins are in different rows.
.. #. Connect the red lead to the GP13 pin via a 330Ω resistor. When using the same power supply intensity, the Red LED will be brighter than the other two, and a slightly larger resistor needs to be used to reduce its brightness.
.. #. Connect the Green lead to the GP14 pin via a 220Ω resistor.
.. #. Connect the Blue lead to the GP15 pin via a 220Ω resistor.
.. #. Connect the GND lead to the negative power bus.
.. #. Connect the negative power bus to Pico's GND.

.. .. note::
..     * The color ring of the 220Ω resistor is red, red, black, black and brown.
..     * The color ring of the 330Ω resistor is orange, orange, black, black and brown.

**Code**



.. note::

    * Open the ``2.4_colorful_light.py`` file under the path of ``euler-kit/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner.

.. code-block:: python

    import machine
    import utime

    red = machine.PWM(machine.Pin(13))
    green = machine.PWM(machine.Pin(14))
    blue = machine.PWM(machine.Pin(15))
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def color_to_duty(rgb_value):
        rgb_value = int(interval_mapping(rgb_value,0,255,0,65535))
        return rgb_value

    def color_set(red_value,green_value,blue_value):
        red.duty_u16(color_to_duty(red_value))
        green.duty_u16(color_to_duty(green_value))
        blue.duty_u16(color_to_duty(blue_value))

    color_set(255,128,0)

Here, we can choose our favorite color in drawing software (such as paint) and display it with RGB LED.

|img_take_color|

Write the RGB value into ``color_set()``, you will be able to see the RGB light up the colors you want.


**How it works?**

We defined a ``color_set()`` function to let the three primary colors work together.

At present, pixels in computer hardware usually adopt a 24-bit representation method. The three primary colors are divided into 8 bits, and the color value range is 0 to 255. With 256 possible values for each of the three primary colors (don't forget to count 0!), that 256 x 256 x 256 = 16,777,216 colors can be combined in this way.
The ``color_set()`` function also follows the 24-bit notation, which makes it easier for us to select the desired color.

And since the value range of ``duty_u16()`` is 0~65535 (instead of 0 to 255) when the output signals to RGB LED through PWM, we have defined ``color_to_duty()`` and ``interval_mapping ()`` function to map the color values to the duty values.