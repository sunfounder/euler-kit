.. _py_passage_counter:


7.4 Passager Counter
====================


Passenger traffic is an indispensable data for large shopping malls, shopping centers, chain stores, airports, stations, museums, Public places such as exhibition halls are indispensable data for management and decision making.

In airports and stations, for example, the number of people needs to be strictly controlled in order to avoid exceeding the capacity for the safety and smooth flow of people.
For shopping centers and chain stores, it is also possible to know more about the time of day when there are more visitors, how many orders each user can generate, and so on.
Thus, we can analyze people's consumption habits and get more turnover.

To sum up, a passager counter can help people understand the operation of these public places and organize their operations effectively!

Here we use a PIR sensor to make a simple passager counter and a 4-digit 7-segment display to display the flow of people.


**Schematic**

|sch_passager_counter| 

* This circuit is based on the :ref:`py_74hc_4dig` with the addition of a PIR module.
* The PIR will send a high signal of about 2.8s long when someone passes by.


**Wiring**


|wiring_passager_counter| 


**Code**

.. note::

    * Open the ``7.4_passager_counter.py`` file under the path of ``euler-kit/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner.


.. code-block:: python

    import machine
    import time


    pir_sensor = machine.Pin(16, machine.Pin.IN)

    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)

    placePin = []
    pin = [10,13,12,11]
    for i in range(4):
        placePin.append(None)
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

    count = 0


    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)
        placePin[digit].value(0)

    def clearDisplay():
        hc595_shift(0x00)

    def hc595_shift(dat):
        rclk.low()
        time.sleep_us(200)
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_us(200)
            value = 1 & (dat >> bit)
            sdi.value(value)
            time.sleep_us(200)
            srclk.high()
            time.sleep_us(200)
        time.sleep_us(200)
        rclk.high()

    def motion_detected(pin):
        global count
        count = count+1

    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

    while True:
        #print(count)
        
        pickDigit(0)
        hc595_shift(SEGCODE[count%10])

        pickDigit(1)
        hc595_shift(SEGCODE[count%100//10])
        
        pickDigit(2)
        hc595_shift(SEGCODE[count%1000//100])
        
        pickDigit(3)
        hc595_shift(SEGCODE[count%10000//1000])


After the code runs, whenever someone passes by, the number on the 4-digit 7-segment display is added by 1.

