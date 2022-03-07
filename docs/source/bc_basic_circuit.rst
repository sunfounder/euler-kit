Electronic Circuit
==================


Electricity powers many of the things you use every day, such as the lights in your home and the computer you are reading this article on.

Using electricity requires you to create an electrical circuit. An electric circuit is a conductive circuit made up of metal wires and electrical and electronic components.

All circuits need to get their power from somewhere. Many of the appliances in your home (e.g., TVs, lights) are powered by wall outlets that connect to the wires that supply power to your house from the power plant; many smaller, portable circuits (e.g., electronic toys and cell phones) are powered by batteries that store electricity. Batteries have two terminals, one is called the positive terminal and is marked with a plus sign (+). The other is called the negative terminal and is symbolized by a minus sign (-), but this symbol is not usually printed on the battery.

In order for current to flow, there needs to be a conductive path that connects the positive terminal of the battery to the negative terminal, which is called a closed circuit. (If it is disconnected, it is called an open circuit.) Electric current will flow through appliances such as lamps to make them work (e.g., light up).

|bc1|


In this kit, the Pico has some power output pins (positive) and some ground pins (negative).
Simply plug the Pico into a power source and let these pins act as the positive and negative sides of the power supply.

|bc2| 

Using electricity can create works with light, sound and motion for you.
Take an LED for example, let the long pin of the LED be connected to the positive terminal and the short pin to the negative terminal, and you can light it up.
However, if you do this, the LED will break down very quickly and you need to add a 220Ω resistor (note the label on the resistor) inside this circuit to protect it.

The circuit they form is shown below.

|bc2.5| 

This time you may have questions: how do I build this circuit? Hold the wires by hand, or tape the pins and wires?

At this point, the solderless breadboard will undoubtedly become your most powerful partner.


.. _bc_bb:

Hello, Breadboard!
------------------------------


The breadboard is a rectangular plastic plate with a bunch of small holes in it. 
These holes allow us to easily insert electronic components and build electronic circuits. 
The breadboard does not permanently fix the electronic components, 
which makes it easy for us to repair the circuit and start over when we make a mistake.

.. note::
    We can use the breadboard without using special tools. But many electronic components are very small. A pair of tweezers can help us pick up small parts better.

There are many detailed breadboard knowledge on the Internet, let us use it wisely.

* `How to Use a Breadboard - Science Buddies <https://www.sciencebuddies.org/science-fair-projects/references/how-to-use-a-breadboard#pth-smd>`_

* `What is a BREADBOARD? - Makezine <https://cdn.makezine.com/uploads/2012/10/breadboardworkshop.pdf>`_


For breadboards, what you need to know clearly is:

#. Each group of half rows inside the breadboard (such as column A-E in row 1 or column F-J in row 3) is connected. This means that when an electrical signal flows in from A1, it can flow from B1, C1, D1, E1, but not from F1 or A2.

#. Both sides of the breadboard are usually used as power buses, and the holes in each column (about 50 holes) are connected. Generally speaking, the hole near the red wire is used to connect the positive power supply, and the hole near the blue wire is used to connect the negative power supply.

#. When building a circuit, the current flows from the positive pole and must first flow through the consumer before it can flow into the negative pole. Otherwise, a short circuit may occur.


|bc3| 


Let us follow the direction of the current to build the circuit!

1. Here we use the 3V3 pin of the Pico board to make the LED work, and the circuit starts from here. Connect it to the red power bus with a male-to-male (M2M) jumper wire.
#. The current needs to pass through a 220 ohm resistor (used to protect the LED). Insert one end (either end) of the resistor into the red power bus, and insert the other end into the free row of the breadboard (row 24 in my circuit).

    .. note::
        The color ring of the 220 ohm resistor is red, red, black, black and brown.

#. Pick up the LED, you will see that one of its leads is longer than the other. Insert the longer lead into the same row as the end of the resistor, and connect the shorter lead across the middle gap of the breadboard to the same row.
    
    .. note::
        The longer lead is known as the anode, and represents the positive side of the circuit; the shorter lead is the cathode, and represents the negative side. 

        The anode needs to be connected to the GPIO pin through a resistor; the cathode needs to be connected to the GND pin.

#. Insert the male-to-male (M2M) jumper wire into the same row as the LED short pin, and then connect it to the negative power bus of the breadboard.
#. Use a jumper to connect the negative power bus to the GND pin of Pico.


Beware of short circuits
------------------------------
A short circuit can occur when two components that should not be connected are "accidentally" connected. 
In this kit, resistors, triodes, capacitors, LEDs, etc. have long metal pins; these pins can bump into each other and cause a short. Depending on the circuit, sometimes a short will simply prevent the circuit from functioning properly. However, sometimes a short circuit can "burn out" components and cause permanent damage, especially between the power supply and the ground bus, causing the circuit to get very hot, burning components and even melting the plastic on the breadboard!

Therefore, always make sure that the pins of all the electronics on the breadboard are not touching each other.

Direction of the circuit
-------------------------------
Circuits are oriented, and for certain electronic components, the orientation is important. Some devices have polarity, which means they have positive and negative poles that must be connected correctly. Building a circuit with the wrong orientation will prevent the circuit from functioning properly.

|bc3| 

In this simple circuit that we built earlier, you can try to reverse the LED and you will find that the LED no longer works.

For some devices, on the other hand, there is no direction, such as the resistors in this circuit, you can try to invert them and it will not affect the normal operation of the LEDs.

If you see "+", "-", "GND", "VCC" and other labels in some devices/modules or have pins of different lengths, most of them need to be connected to the circuit in a specific direction.


Protection of the circuit
-------------------------------------

The current flowing through an object (such as a wire) is called current (I) and it is measured in amperes (A).
The driving force (voltage) behind the flow of current is called voltage and is measured in volts (V).
The property of the material that restricts the flow of current is called resistance (R), and resistance is measured in ohms (Ω).

The relationship between current, voltage and resistance is expressed by Ohm's law (provided that the temperature remains constant).
This shows that the current flowing in a circuit is proportional to the applied voltage and inversely proportional to the resistance of the circuit. That is, current (I) = voltage (V) / resistance (R).

* `Ohm's law - Wikipedia <https://en.wikipedia.org/wiki/Ohm%27s_law>`_

About Ohm's law we can do a simple experiment.

|bc3| 

In this circuit, we change the wire connecting 3V3 to 5V (i.e. VBUS, the 40th pin of Pico), you will find that the LED becomes brighter than before.
Change the resistor from 220Ω to 1000Ω (color ring: brown, black, black, brown and brown), you will find that the LED becomes dimmer than before, the larger the resistor, the dimmer the LED will be.

.. note::
    See :ref:`cpn_res` for an introduction to resistors and how to calculate resistance values.

Any electrical device will need to be used at the specified power, which means you need to be aware of the supply voltage and resistor usage in your self-built circuits.
Some packaged modules usually only require attention to accessing the proper voltage (usually 3.3V or 5V), such as ultrasonic sensors.
Some devices require the addition of appropriate resistors and other devices to protect the circuit.
For example, the typical maximum current LED can use is about 25mA, according to Ohm's law can be learned, if we use 5V power supply, and the external resistance is less than 200Ω, it will burn LED.


