.. _py_light_theremin:

7.1 Light Theremin
=========================

Theremin is an electronic musical instrument that does not require physical contact. It produces different tones by sensing the position of the player's hand.

The instrument's controlling section usually consists of two metal antennas that sense the relative position of the thereminist's hands and control oscillators for frequency with one hand, and amplitude (volume) with the other. The electric signals from the theremin are amplified and sent to a loudspeaker.

We cannot reproduce the same instrument through Pico, but we can use photoresistor and passive buzzer to achieve similar gameplay.

* `Theremin - Wikipedia <https://en.wikipedia.org/wiki/Theremin>`_

**Schematic**

|sch_light_theremin|

Before starting the project, you need to debug the range of light taken under the current environment by lifting up and down above the photoresistor by hand. The LED connected in GP16 is used to indicate the debugging time, and the LED is lit to start debugging and off to end debugging.


When GP15 outputs high level, S8050 (NPN transistor) conducts and the passive buzzer starts to sound.

GP28 reads the value of the photoresistor, when the stronger the light, the smaller the value GP28 gets; and vice versa, the larger.
By programming the value of the photoresistor to affect the frequency of the passive buzzer, the Light Theremin is simulated.


**Wiring**

|wiring_light_theremin|

.. #. Connect 3V3 and GND of Pico to the power bus of the breadboard.
.. #. Connect one lead of the photoresistor to the GP28 pin, then connect the same lead to the positive power bus with a 10K ohm resistor.
.. #. Connect another lead of photoresistor to the negative power bus.
.. #. Insert the LED into the breadboard, connect its anode pin to the GP16 in series with a 220Ω resistor, and connect its cathode pin to the negative power bus.
.. #. Insert the passive buzzer and S8050 transistor into the breadboard. The anode pin of the buzzer is connected to the positive power bus, the cathode pin is connected to the **collector** lead of the transistor, and the **base** lead of the transistor is connected to the GP15 pin through a 1kΩ resistor. **emitter** lead is connected to the negative power bus.

.. .. note::
..     * The color ring of the 22Ω resistor is red, red, black, black and brown.
..     * The color ring of the 10kΩ resistor is brown, black, black, red and brown.

**Code**

.. note::

    * Open the ``7.1_light_theremin.py`` file under the path of ``euler-kit/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner.

.. code-block:: python

    import machine
    import utime

    led = machine.Pin(16, machine.Pin.OUT)
    photoresistor = machine.ADC(28) 
    buzzer = machine.PWM(machine.Pin(15))

    light_low=65535
    light_high=0

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def tone(pin,frequency,duration):
        pin.freq(frequency)
        pin.duty_u16(30000)
        utime.sleep_ms(duration)
        pin.duty_u16(0)

    # calibrate the photoresistor max & min values.
    timer_init_start = utime.ticks_ms()
    led.value(1)    
    while utime.ticks_diff(utime.ticks_ms(), timer_init_start)<5000:
        light_value = photoresistor.read_u16()
        if light_value > light_high:
            light_high = light_value
        if light_value < light_low:
            light_low = light_value   
    led.value(0)    

    # play
    while True:
        light_value  = photoresistor.read_u16()
        pitch = int(interval_mapping(light_value,light_low,light_high,50,6000))
        if pitch > 50 :
            tone(buzzer,pitch,20)
        utime.sleep_ms(10)

When the program runs, the LED will light up, and we will have five seconds to calibrate the detection range of the photoresistor by lifting up and down above the photoresistor by hand. This is because we may be in a different light environment each time we use it (e.g. the light intensity is different between midday and dusk).

At this time, we need to swing our hands up and down on top of the photoresistor, and the movement range of the hand will be calibrated to the playing range of this instrument.

After five seconds, the LED will go out and we can wave our hands on the photoresistor to play.

