.. _py_lcd:

Liquid Crystal Display
===============================

LCD1602 is a character type liquid crystal display, which can display 32 (16*2) characters at the same time.

As we all know, though LCD and some other displays greatly enrich the man-machine interaction, 
they share a common weakness. When they are connected to a controller, 
multiple IOs will be occupied of the controller which has no so many outer ports. 
Also it restricts other functions of the controller. 
Therefore, LCD1602 with an I2C bus is developed to solve the problem.

* :ref:`cpn_lcd`
* `Inter-Integrated Circuit - Wikipedia <https://en.wikipedia.org/wiki/I2C>`_


|pin_i2c|

Here we will use the I2C0 interface to control the LCD1602 and display text.


**Wiring**

|sch_lcd|

|wiring_lcd|

1. Connect VCC of LCD to VBUS of Pico.
#. Connect the GND of LCD to the GND of Pico.
#. Connect SDA of LCD to GP0 of Pico, which is GP6(I2C1 SDA).
#. Connect SCL of LCD to GP1 of Pico, which is GP7(I2C1 SCL).

**Code**

The following is the library of lcd1602 packaged by Sunfounder.

You need to save it in Pico, name it **lcd1602.py** and use it as a library.


.. code-block:: python

    import machine
    import time

    class LCD():
        def __init__(self, addr=0x27, blen=1):
            sda = machine.Pin(0)
            scl = machine.Pin(1)
            self.bus = machine.I2C(0,sda=sda, scl=scl, freq=400000)
            #print(self.bus.scan())
            self.addr = addr
            self.blen = blen
            self.send_command(0x33) # Must initialize to 8-line mode at first
            time.sleep(0.005)
            self.send_command(0x32) # Then initialize to 4-line mode
            time.sleep(0.005)
            self.send_command(0x28) # 2 Lines & 5*7 dots
            time.sleep(0.005)
            self.send_command(0x0C) # Enable display without cursor
            time.sleep(0.005)
            self.send_command(0x01) # Clear Screen
            self.bus.writeto(self.addr, bytearray([0x08]))
        
        def write_word(self, data):
            temp = data
            if self.blen == 1:
                temp |= 0x08
            else:
                temp &= 0xF7
            self.bus.writeto(self.addr, bytearray([temp]))
        
        def send_command(self, cmd):
            # Send bit7-4 firstly
            buf = cmd & 0xF0
            buf |= 0x04               # RS = 0, RW = 0, EN = 1
            self.write_word(buf)
            time.sleep(0.002)
            buf &= 0xFB               # Make EN = 0
            self.write_word(buf)

            # Send bit3-0 secondly
            buf = (cmd & 0x0F) << 4
            buf |= 0x04               # RS = 0, RW = 0, EN = 1
            self.write_word(buf)
            time.sleep(0.002)
            buf &= 0xFB               # Make EN = 0
            self.write_word(buf)
        
        def send_data(self, data):
            # Send bit7-4 firstly
            buf = data & 0xF0
            buf |= 0x05               # RS = 1, RW = 0, EN = 1
            self.write_word(buf)
            time.sleep(0.002)
            buf &= 0xFB               # Make EN = 0
            self.write_word(buf)

            # Send bit3-0 secondly
            buf = (data & 0x0F) << 4
            buf |= 0x05               # RS = 1, RW = 0, EN = 1
            self.write_word(buf)
            time.sleep(0.002)
            buf &= 0xFB               # Make EN = 0
            self.write_word(buf)
        
        def clear(self):
            self.send_command(0x01) # Clear Screen
            
        def openlight(self):  # Enable the backlight
            self.bus.writeto(self.addr,bytearray([0x08]))
            # self.bus.close()
        
        def write(self, x, y, str):
            if x < 0:
                x = 0
            if x > 15:
                x = 15
            if y < 0:
                y = 0
            if y > 1:
                y = 1

            # Move cursor
            addr = 0x80 + 0x40 * y + x
            self.send_command(addr)

            for chr in str:
                self.send_data(ord(chr))
        
        def message(self, text):
            #print("message: %s"%text)
            for char in text:
                if char == '\n':
                    self.send_command(0xC0) # next line
                else:
                    self.send_data(ord(char))

Then, create a new file, and call the lcd1602 library stored before in this file.

.. code-block:: python

    from lcd1602 import LCD
    import utime

    lcd = LCD()
    string = " Hello!\n"
    lcd.message(string)
    utime.sleep(2)
    string = "    Sunfounder!"   
    lcd.message(string)
    utime.sleep(2)
    lcd.clear()   

After the program runs, you will be able to see two lines of text appear on the LCD in turn, and then disappear.


**How it works?**

In the lcd1602 library, we integrate the relevant functions of lcd1602 into the LCD class.

Import lcd1602 library

.. code-block:: python

    from lcd1602 import LCD    

Declare an object of the LCD class and name it lcd.

.. code-block:: python

    lcd = LCD()

This statement will display the text on the LCD. It should be noted that the argument must be a string type. If we want to pass an integer or float, we must use the forced conversion statement ``str()``.

.. code-block:: python

    lcd.message(string)


If you call this statement multiple times, lcd will superimpose the texts. This requires the use of the following statement to clear the display.

.. code-block:: python

    lcd.clear()



.. **What more?**

.. We can combine thermistor and I2C LCD1602 to make a room temperature meter.

.. .. image:: img/wiring_lcd_2.png

.. .. code-block:: python

..     from lcd1602 import LCD
..     import machine
..     import utime
..     import math

..     thermistor = machine.ADC(28)  
..     lcd = LCD()

..     while True:
..         temperature_value = thermistor.read_u16()
..         Vr = 3.3 * float(temperature_value) / 65535
..         Rt = 10000 * Vr / (3.3 - Vr)
..         temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
..         Cel = temp - 273.15
..         #Fah = Cel * 1.8 + 32
..         #print ('Celsius: %.2f C  Fahrenheit: %.2f F' % (Cel, Fah))
..         #utime.sleep_ms(200)
        
..         string = " Temperature is \n    " + str('{:.2f}'.format(Cel))+ " C"
..         lcd.message(string)
..         utime.sleep(1)
..         lcd.clear()
