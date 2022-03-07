.. _cpn_mpr121:

MPR121
===========================

|img_mpr121|

Add lots of touch sensors to your next project with this easy-to-use 12-channel capacitive touch sensor breakout board, starring the MPR121. 
This chip can handle up to 12 individual touch pads.

The MPR121 has support for only I2C, which can be implemented with nearly any microcontroller. 
You can select one of 4 addresses with the ADDR pin, for a total of 48 capacitive touch pads on one I2C 2-wire bus. 
Using this chip is a lot easier than doing the capacitive sensing with analog inputs: it handles all the filtering for you and can be configured for more/less sensitivity.

When the MPR121 senses a change, it pulls an interrupt pin LOW. The control board going to check that pin to see if it is LOW during the loop. 
To do this, this sensor also needs access to another digital pin.

**Electrodes**

Electrode is a touch sensor. Typically, electrodes can just be some piece of metal, or a wire. 
But some times depending on the length of our wire, or the material the electrode is on, it can make triggering the sensor difficult. 
For this reason, the MPR121 allows you to configure what is needed to trigger and untrigger an electrode.