.. _py_10_second:

7.5 GAME - 10 Second
=======================


To challenge your concentration, follow me next to make a game device. 
Make a magic wand by connecting the tilt switch with a stick. When you shake the wand, the 4-digit segment display will start counting, and when you shake it again, it will stop counting. In order to win, you must keep the displayed count at **10.00**. You can play the game with your friends to see who is the time wizard.


**Schematic**


|sch_10_second|


* This circuit is based on :ref:`py_74hc_4dig` with the addition of a tilt switch.
* GP16 is high when the tilt switch is upright; low when tilted.

**Wiring**

|wiring_game_10_second| 


**Code**


.. note::

    * Open the ``7.5_game_10_second.py`` file under the path of ``euler-kit/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import time

    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)

    placePin = []
    pin = [10,13,12,11]
    for i in range(4):
        placePin.append(None)
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

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
        #time.sleep_us(200)
        

    def display(num):
        
        pickDigit(0)
        hc595_shift(SEGCODE[num%10])

        pickDigit(1)
        hc595_shift(SEGCODE[num%100//10])
        
        pickDigit(2)
        hc595_shift(SEGCODE[num%1000//100]+0x80)
        
        pickDigit(3)
        hc595_shift(SEGCODE[num%10000//1000])    


    tilt_switch = machine.Pin(16,machine.Pin.IN)

    count_flag = False

    def shake(pin):
        global timeStart,count_flag
        count_flag = not count_flag
        if count_flag == True:
            timeStart = time.ticks_ms()

    tilt_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=shake)


    count = 0
    while True:
        if count_flag == True:
            count = int((time.ticks_ms()-timeStart)/10)
        display(count)

The 4-digit 7-segment display will begin counting when you shake the wand, and will stop counting when you shake it again. 
You win if you manage to keep the displayed count at 10.00. The game will continue after one more shake.