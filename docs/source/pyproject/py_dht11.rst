Temperature - Humidity
=========================


湿度和温度是从物理量本身到实际人们的生活密切相关的。
人的环境温度和湿度会直接影响人的体温调节功能和热传导效果。
它会进一步影响思维活动和精神状态，从而影响我们学习和工作的效率。

温度是国际单位制中的7个基本物理量之一，用来衡量物体的冷热程度。
摄氏度是目前世界上使用较为广泛的一种温标，用符号“℃”表示。
它是18世纪瑞典天文学家Anders Celsius提出来的。
它定义了在标准大气压下，冰水混合物的温度为0℃，水的沸点为100℃，其间分为100等份，每一份为1℃。
自从国际单位制中开尔文标准化后，它随后被重新定义为开尔文标度上的等效固定点，因此1摄氏度的温度增量与1摄氏度的增量相同1 开尔文，尽管它们的不同之处在于恰好 273.15 的附加偏移。
美国通常使用华氏温标，水在华氏温度下结冰32 °F并沸腾于在海平面大气压下为212 °F。

湿度是空气中存在的水蒸气的浓度。
生活中常用的空气相对湿度，用%RH表示。相对湿度与温度密切相关。
对于一定体积的密封气体，温度越高，相对湿度越低，温度越低，相对湿度越高。

|img_Dht11|

这个套件中提供了一款基本的数字温度和湿度传感器 —— DHT11。
它使用电容式湿度传感器和热敏电阻来测量周围的空气，并在数据引脚上吐出数字信号（不需要模拟输入引脚）。

* :ref:`cpn_dht11`

**Wiring**

|sch_dht11|

|wiring_dht11|

**Code**

你需要先把 ``dht.py`` 存入pico作为库使用。 

然后，运行主程序。

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

代码运行后，你将看到持续Shell持续打印出温度和湿度，随着程序运行稳定，这两个值会愈发的准确。

**How it works?**

在dht库中，我们将相关功能集成到了 DHT11 类中。

.. code-block:: python

    from mpr121 import MPR121

初始化DHT11对象。这个设备只需要一个数字输入即可使用。

.. code-block:: python

    pin = Pin(16, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)

使用 ``sensor.measure()`` 读取当前的温度和湿度，这些数据会被储存到 ``sensor.temperature``, ``sensor.humidity`` 中。
随后将它们打印出来。
最后DHT11 sampling rate is 1HZ, 在loop中需要一个 ``time.sleep(1)``。

.. code-block:: python

    while True:
        sensor.measure()
        print("Temperature: {}, Humidity: {}".format(sensor.temperature, sensor.humidity))
        time.sleep(1)
