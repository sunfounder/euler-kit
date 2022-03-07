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

.. note:: sw引脚需要接一个上拉电阻，否则z轴无法顺利使用。


|sch_joystick|

|wiring_joystick|

**Code**

:raw-code:

程序运行后，可以打开串口监视器查看摇杆X轴和Y轴的读数，以及Z轴的按键状态。
X 轴和 Y 轴的值为模拟值，在0~1023范围内变化。
Z轴则是数字值，状态为1或0。