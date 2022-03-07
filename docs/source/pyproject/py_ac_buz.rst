Beep
==================


有源蜂鸣器是一个典型的数字输出设备，它的使用方法就像点亮LED一样简单！

* :ref:`Buzzer`


**Schematic**


**Wiring**

Two types of buzzers are included in the kit. 
We need to use active buzzer. 
Turn them around, the sealed back (not the exposed PCB) is the one we want.

|img_buzzer|

The buzzer needs to use a transistor when working, here we use S8050.


|sch_buzzer|
|wiring_buzzer|


**Code**


.. code-block:: python

    import machine
    import utime

    buzzer = machine.Pin(15, machine.Pin.OUT)
    while True:
        for i in range(4):
            buzzer.value(1)
            utime.sleep(0.3)
            buzzer.value(0)
            utime.sleep(0.3)
        utime.sleep(1)

代码运行后，你将每隔一秒听到一次鸣笛。
