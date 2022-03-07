.. _cpn_max7219:

LED Matrix Module
==============================

The 64 LEDs are driven by 16 output pins of the IC MAX7219. 

These integrated circuits from Maxim are for driving either 64 individual LED’s, or up to 8 digits of 7-segment displays. 
The drivers implement a SPI compatible slave interface that can be controlled from the MCU using only 3 of the digital output pins.

The maximum number of LEDs light up at the same time is actually eight. 
The LEDs are arranged as 8×8 set of rows and columns. 
So the MAX7219 activates each column for a very short period of time and at the same time it also drives each row. 
So by rapidly switching through the columns and rows the human eye will only notice a continuous light.

|img_max7219|


