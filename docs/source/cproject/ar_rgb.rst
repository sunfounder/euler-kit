Colorful Light
==============================================

As we know, light can be superimposed. For example, mix blue light and green light give cyan light, red light and green light give yellow light.
This is called "The additive method of color mixing".

* `Additive color - Wikipedia <https://en.wikipedia.org/wiki/Additive_color>`_

Based on this method, we can use the three primary colors to mix the visible light of any color according to different specific gravity. For example, orange can be produced by more red and less green.

In this chapter, we will use RGB LED to explore the mystery of additive color mixing!

RGB LED is equivalent to encapsulating Red LED, Green LED, Blue LED under one lamp cap, and the three LEDs share one cathode pin.
Since the electric signal is provided for each anode pin, the light of the corresponding color can be displayed. By changing the electrical signal intensity of each anode, it can be made to produce various colors.

* :ref:`cpn_rgb`

**Wiring**

|img_rgb_pin|

Put the RGB LED flat on the table, we can see that it has 4 leads of different lengths.
Find the longest one (GND) and turn it sideways to the left.
Now, the order of the four leads is Red, GND, Green, Blue from left to right.



|sch_rgb|

|wiring_rgb|

1. Connect the GND pin of the Pico to the negative power bus of the breadboard.
#. Insert the RGB LED into the breadboard so that its four pins are in different rows.
#. Connect the red lead to the GP13 pin via a 330Ω resistor. When using the same power supply intensity, the Red LED will be brighter than the other two, and a slightly larger resistor needs to be used to reduce its brightness.
#. Connect the Green lead to the GP14 pin via a 220Ω resistor.
#. Connect the Blue lead to the GP15 pin via a 220Ω resistor.
#. Connect the GND lead to the negative power bus.
#. Connect the negative power bus to Pico's GND.

.. .. note::
..     * The color ring of the 220Ω resistor is red, red, black, black and brown.
..     * The color ring of the 330Ω resistor is orange, orange, black, black and brown.

**Code**

Here, we can choose our favorite color in drawing software (such as paint) and display it with RGB LED.

:raw-code:

|img_take_color|

Write the RGB value into color_set(), you will be able to see the RGB light up the colors you want.


**How it works?**

In this example, the function used to assign values to the three pins of RGB is packaged in an independent subfunction ``color()``.

.. code-block:: C

    void color (unsigned char red, unsigned char green, unsigned char blue)
    {
        analogWrite(redPin, red);
        analogWrite(greenPin, green);
        analogWrite(bluePin, blue);
    }

In ``loop()``, RGB value works as an input argument to call the function ``color()`` to realize that the RGB can emit different colors.

.. code-block:: C

    void loop() 
    {    
        color(255, 0, 0); //  red 
        delay(1000); 
        color(0,255, 0); //  green  
        delay(1000);  
        color(0, 0, 255); //  blue  
        delay(1000);
    }

    