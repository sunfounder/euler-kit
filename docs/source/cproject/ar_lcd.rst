.. _ar_lcd:

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

The libraries ``Wire.h`` and ``LiquidCrystal_I2C.h`` are used in these codes, 
``Wire.h`` is built in Arduino, but ``LiquidCrystal_I2C.h`` needs adding manually. 
Add Method: Refer to :ref:`apx_add_lib`.

:raw-code:

**How it works?**

By calling the library ``LiquidCrystal_I2C.h``, you can easily drive the LCD. 

.. code-block:: arduino

    #include "LiquidCrystal_I2C.h"

**Library Functions：**

.. code-block:: arduino

    LiquidCrystal_I2C(uint8_t lcd_Addr,uint8_t lcd_cols,uint8_t lcd_rows)

Creates a new instance of the LiquidCrystal_I2C class that represents a
particular LCD attached to your Arduino board.

**lcd_AddR**: The address of the LCD defaults to 0x27.

**lcd_cols**: The LCD1602 has 16 columns.

**lcd_rows**: The LCD1602 has 2 rows.


.. code-block:: arduino

    void init()

Initialize the lcd.

.. code-block:: arduino

    void backlight()

Turn the (optional) backlight on.

.. code-block:: arduino

    void nobacklight()

Turn the (optional) backlight off.

.. code-block:: arduino

    void display()

Turn the LCD display on.

.. code-block:: arduino

    void nodisplay()

Turn the LCD display off quickly.

.. code-block:: arduino

    void clear()

Clear display, set cursor position to zero.

.. code-block:: arduino

    void setCursor(uint8_t col,uint8_t row)

Set the cursor position to col,row.

.. code-block:: arduino

    void print(data,BASE)

Prints text to the LCD.

**data**: The data to print (char, byte, int, long, or string).

**BASE (optional)**: The base in which to print numbers: BIN for binary (base 2), DEC for decimal (base 10), OCT for octal (base 8), HEX for hexadecimal (base 16).




**What more？**


Upload the codes to the Pico, the content that you input in the serial monitor will be printed on the LCD.

:raw-code:

In addition to reading data from the electronic components, the Pico 
can read the data input in the serial port monitor, and you can
use ``Serial.read()`` as the controller of the circuit experiment. 

Run the serial communication in ``setup()`` and set the data rate to 9600.

.. code-block:: arduino

    Serial.begin(9600);

The state of serial port monitor is judged in ``loop()``, and the information processing will be carried out only when the data are received.

.. code-block:: arduino

    if (Serial.available() > 0){}

Clear the screen.

.. code-block:: arduino

    lcd.clear();

Reads the input value in the serial port monitor and stores it to the variable incomingByte.

.. code-block:: arduino

    char incomingByte = Serial.read();

Display each character to the LCD and skip the line-feed character.

.. code-block:: arduino

    while (Serial.available() > 0) {
        char incomingByte=Serial.read();
        if(incomingByte==10){break;}// skip the line-feed character
        lcd.print(incomingByte);// display each character to the LCD  
    } 


* `Serial Read <https://www.arduino.cc/reference/en/language/functions/communication/serial/read/>`_
