.. _py_alarm_lamp:

7.3 Alarm Siren Lamp
=======================

In life (or in the movie), you can often see the police lights. It is generally used to maintain traffic, play a warning role, is an important prop to protect people's lives and property safety, often in police cars, engineering vehicles, fire trucks, emergency vehicles. If you see its lights or hear its sound, then you have to beware, which means you (or around the people) may be in danger.

Here we use LEDs and buzzers to create a small warning light, and a slide switch to activate it.


**Schematic**

|sch_alarm_siren_lamp|

* GP17 is connected to the middle pin of the slider switch after connecting a 10kΩ resistor in series, which enables the slider to output high or low level when toggled to the left or right.
* When GP15 goes high, the S8050 (NPN transistor) turns on and the passive buzzer starts to sound. The passive buzzer is programmed to gradually increase in frequency, thus producing a siren sound with a modulation effect.
* The GP16 is connected to the LED and is also programmed to change its brightness periodically to simulate the effect of a siren.

**Wiring**

|wiring_alarm_siren_lamp|


**Code**

.. note::

    * Open the ``7.3_alarm_siren_lamp.py`` file under the path of ``euler-kit/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import time


    buzzer = machine.PWM(machine.Pin(15))
    led = machine.PWM(machine.Pin(16))
    led.freq(1000)

    switch = machine.Pin(17,machine.Pin.IN)

    def noTone(pin):
        pin.duty_u16(0)


    def tone(pin,frequency):
        pin.freq(frequency)
        pin.duty_u16(30000)

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def toggle(pin):
        global bell_flag
        bell_flag = not bell_flag
        print(bell_flag)
        if bell_flag:
            switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=toggle)
        else:
            switch.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle)


    bell_flag = False
    switch.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle)



    while True:
        if bell_flag == True:
            for i in range(0,100,2):
                led.duty_u16(int(interval_mapping(i,0,100,0,65535)))
                tone(buzzer,int(interval_mapping(i,0,100,130,800)))
                time.sleep_ms(10)
        else:
            noTone(buzzer)
            led.duty_u16(0)

After the program runs, toggle the slide switch to the left, the buzzer will emit a gradual warning tone and the LED will change its brightness accordingly; toggle the slide switch to the right, the buzzer and LED will stop working.