.. _py_dht11:

6.2 Temperature - Humidity
=======================================


Humidity and temperature are closely related from the physical quantity itself to the actual people's life.
The temperature and humidity of human environment will directly affect the thermoregulatory function and heat transfer effect of human body.
It will further affect the thinking activity and mental state, thus affecting the efficiency of our study and work.

Temperature is one of the seven basic physical quantities in the International System of Units, which is used to measure the degree of hot and cold of an object.
Celsius is one of the more widely used temperature scales in the world, expressed by the symbol "℃".

Humidity is the concentration of water vapor present in the air.
The relative humidity of air is commonly used in life and is expressed in %RH. Relative humidity is closely related to temperature.
For a certain volume of sealed gas, the higher the temperature, the lower the relative humidity, and the lower the temperature, the higher the relative humidity.

|img_Dht11|

A basic digital temperature and humidity sensor, the **DHT11**, is provided in this kit.
It uses a capacitive humidity sensor and thermistor to measure the surrounding air and outputs a digital signal on the data pins (no analog input pins are required).

* :ref:`cpn_dht11`

**Schematic**

|sch_dht11|


**Wiring**


|wiring_dht11|

**Code**

.. note::

    * Open the ``6.2_temperature_humidity.py`` file under the path of ``euler-kit/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`. 
    
    * Here you need to use the library called ``dht.py``, please check if it has been uploaded to Pico, for a detailed tutorial refer to :ref:`add_libraries_py`.

.. code-block:: python

    from machine import Pin, I2C
    import utime as time
    from dht import DHT11

    pin = Pin(16, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)

    while True:
        sensor.measure()
        print("Temperature: {}, Humidity: {}".format(sensor.temperature, sensor.humidity))
        time.sleep(1)

After the code is run, you will see the Shell continuously print out the temperature and humidity, and as the program runs steadily, these two values will become more and more accurate.

**How it works?**

In the dht library, we have integrated the relevant functionality into the ``DHT11`` class.

.. code-block:: python

    from mpr121 import MPR121

Initialize the ``DHT11`` object. This device only needs a digital input to be used.

.. code-block:: python

    pin = Pin(16, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)

Use ``sensor.measure()`` to read the current temperature and humidity, which will be stored in ``sensor.temperature``, ``sensor.humidity``.
They are then printed out.
Finally the DHT11 sampling rate is 1HZ, a ``time.sleep(1)`` is needed in the loop.

.. code-block:: python

    while True:
        sensor.measure()
        print("Temperature: {}, Humidity: {}".format(sensor.temperature, sensor.humidity))
        time.sleep(1)
