Feel the Water Level
====================

|img_water_sensor|

Water sensor is designed for water detection, which can be widely used in sensing rainfall, water level, and even liquid leakage.

其是通过具有一系列的暴露的平行导线线迹测量其水滴/水量大小从而判断水位。轻松完成水量到模拟信号的转换，输出的模拟值可以直接被开发板读取，达到水位报警的功效。

.. warning:: 该传感器不能完全浸入水中，请只将十个Traces所在的部分与水接触。另外，在潮湿环境下通电会加快探头的腐蚀速度，削减传感器寿命，建议您仅在读取读数时供电。

* :ref:`cpn_water`

**Wiring**

|sch_water|

|wiring_water|

**Code**


.. code-block:: python

    import machine
    import utime

    sensor = machine.ADC(28)

    while True:
        value=sensor.read_u16()
        print(value)
        utime.sleep_ms(200)


程序运行后，将Water Sensor缓慢浸入水中，随着深度增加，Shell的打印值也会逐渐变大。

**What More?**

有一种将模拟输入模块当作数字模块使用的方法。

首先，在干燥环境下先测出water sensor的读值，记录它，作为阈值。
随后，完成编程，重新读取water sensor的读值。
当water sensor的读值大幅度偏离了干燥时的读值，则说明它接触到液体了。
换而言之，将这个设备置于水管附近，便能检测到水管是否发生漏液的情况。


.. code-block:: python

    import machine
    import utime

    sensor = machine.ADC(28)
    threshold = 30000 #This value needs to be modified with the environment.

    while True:
        value=sensor.read_u16()
        if value > threshold :
            print("Liquid leakage!")
        utime.sleep_ms(200)
