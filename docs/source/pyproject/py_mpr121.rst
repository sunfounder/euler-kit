Electrode Keyboard
====================

当您想在项目中添加大量触摸开关时，MPR121 是一个不错的选择。它的电极可以用导体进行延伸，
如果把电极连接到香蕉上，就可以把香蕉变成一个触摸开关。

* :ref:`cpn_mpr121`


**Wiring**


|sch_mpr121|

|wiring_mpr121|

**Code**


你需要先把 ``mpr121.py`` 存入pico作为库使用。 

然后，运行主程序。

.. code-block:: python

    from mpr121 import MPR121
    from machine import Pin, I2C
    import time

    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

    # check all keys
    while True:
        value = mpr.get_all_states()
        if len(value) != 0:
            print(value)
        time.sleep_ms(100)

After the program runs, 你可以用手触碰MPR121上的十二个电极，被触碰的电极将会被打印出来。

你可以将电极延申，连接其他导体如水果、导线、金属箔等，这会使你有更多的方式来触发这些电极。

**How it works?**

在mpr121库中，我们将相关功能集成到了MPR121类中。

.. code-block:: python

    from mpr121 import MPR121

MPR121是一个I2C模块，需要定义一组I2C引脚，
用于初始化MPR121对象。此时该模块的电极们的状态会被记录为初始值。如延长电极，需要重新运行示例来重置初始值。

.. code-block:: python

    from machine import Pin, I2C
    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

* `Inter-Integrated Circuit - Wikipedia <https://en.wikipedia.org/wiki/I2C>`_

随后使用 ``mpr.get_all_states()`` 来读取电极是否被触发即可。假如0号和1号电极被触发，值 ``[1, 0]`` 将会产生。

.. code-block:: python

    while True:
        value = mpr.get_all_states()
        if len(value) != 0:
            print(value)
        time.sleep_ms(100)

你也可以使用 ``mpr.is_touched(electrode)`` 来检测特定的电极。当被触发时，返回 ``True`` ，否则返回 ``False`` 。

.. code-block:: python

    while True:
        value = mpr.is_touched(0)
        print(value)
        time.sleep_ms(100)