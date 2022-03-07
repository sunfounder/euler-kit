Feel the Light
================

光敏电阻是一个典型的模拟输入的设备，它的使用方法与电位器十分相似，输出的模拟值取决于光的亮度。
换而言之。你可以用它来检测是否天亮了。

* :ref:`cpn_light`

**Wiring**

|sch_photoresistor|

|wiring_photoresistor|

**code**

.. code-block:: python

    import machine
    import utime

    photoresistor = machine.ADC(28)

    while True:
        light_value  = photoresistor.read_u16()
        print(light_value)
        utime.sleep_ms(10)

程序运行后，Shell会打印出photoresistor的值，如果你用手遮住它，读值将迅速变化。

