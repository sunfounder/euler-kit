Toggle the Joystick
====================

如果你经常玩电子游戏，那么你应当对Joystick十分熟悉。
它通常用于移动游戏角色，旋转画面等等。

Joystick让计算机读取我们的操作行为的原理十分简单。
它可以看作由两个相互垂直的电位器构成，
这两个电位器一个测量操纵杆的垂直方向的模拟值，一个测量水平方向的模拟值，从而得出一个平面直角坐标系中的值(x,y)。

The joystick of this kit also has a digital input, which is activated when the joystick is pressed.

* :ref:`cpn_joystick`


**Wiring**


|sch_joystick|

|wiring_joystick|

.. note:: sw引脚需要接一个上拉电阻，否则z轴无法顺利使用。


**Code**

.. code-block:: python

    import machine
    import utime

    x_joystick = machine.ADC(27)
    y_joystick = machine.ADC(26)
    z_switch = machine.Pin(22,machine.Pin.IN)

    while True:
        x_value = x_joystick.read_u16()
        y_value = y_joystick.read_u16()
        z_value = z_switch.value()
        print(x_value,y_value,z_value)
        utime.sleep_ms(200)    

程序运行后，Shell会打印出joystick的x,y,z三个值。
X 轴和 Y 轴的值为模拟值，在0~65535范围内变化。
Z轴则是数字值，状态为1或0。