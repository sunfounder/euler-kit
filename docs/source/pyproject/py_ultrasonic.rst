Measuring Distance
==================

超声波传感器的工作原理是声纳和雷达系统，用于确定与物体的距离。

* :ref:`cpn_ultrasonic`

**Wiring**

|sch_ultrasonic|

|wiring_ultrasonic|

**Code**

.. code-block:: python

    import machine
    import time

    TRIG = machine.Pin(17,machine.Pin.OUT)
    ECHO = machine.Pin(16,machine.Pin.IN)

    def distance():
        TRIG.low()
        time.sleep_us(2)
        TRIG.high()
        time.sleep_us(10)
        TRIG.low()
        while not ECHO.value():
            pass
        time1 = time.ticks_us()
        while ECHO.value():
            pass
        time2 = time.ticks_us()
        during = time.ticks_diff(time2,time1)
        return during * 340 / 2 / 10000

    while True:
        dis = distance()
        print ('Distance: %.2f' % dis)
        time.sleep_ms(300)

程序运行后，Shell将打印出超声波传感器距离前方障碍物的距离。

**How it works?**

超声波传感器产生高频声波（超声波）。当这种超声波击中物体时，它反射为回波，由接收器检测到，通过测量回波到达接收器所需的时间，就可以计算出距离了。
根据这个原理，可以得出函数 ``distance()`` 。

.. code-block:: python

    def distance():
        TRIG.low()
        time.sleep_us(2)
        TRIG.high()
        time.sleep_us(10)
        TRIG.low()
        while not ECHO.value():
            pass
        time1 = time.ticks_us()
        while ECHO.value():
            pass
        time2 = time.ticks_us()
        during = time.ticks_diff(time2,time1)
        return during * 340 / 2 / 10000

其中，前面几行用于发射一道10us的超声波。

.. code-block:: python

    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()

然后，将程序暂停，待超声波发射完毕后，记录当前时间。

.. code-block:: python

        while not ECHO.value():
            pass
        time1 = time.ticks_us()

随后，将程序再次暂停，待接收到回波后，再一次记录当前时间。

.. code-block:: python

        while ECHO.value():
            pass
        time2 = time.ticks_us()

最后，根据两次记录的时间差，用音速(340m/s)乘以时间得到超声波的路程（即超声波从传感器到障碍物之间的一次来回），是距离的两倍)。
将单位换算为厘米，得到我们需要的返回值。

.. code-block:: python

        during = time.ticks_diff(time2,time1)
        return during * 340 / 2 / 10000

需要注意的是，超声波传感器在工作时会将程序暂停，这在编写复杂的项目时，可能会导致一些卡顿的情况。

