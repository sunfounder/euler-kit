.. _py_motor:

Small Fan
=========


Now we use the L293D to drive the DC motor to make it rotate clockwise and counterclockwise. 
Since the DC motor requires a relatively large current, for safety reasons, 
here we use a power module to supply power to the motor.

.. 现在我们使用 L293D 驱动直流电机，使其顺时针和逆时针旋转。 
.. 由于直流电机需要较大的电流，为了安全起见，这里我们使用电源模块为电机供电。

* :ref:`cpn_motor`
* :ref:`cpn_l293d`
* :ref:`cpn_power_module`

**Wiring**

|sch_motor|

|wiring_motor|

**Code**

.. code-block:: python

    import machine
    import utime

    motor1A = machine.Pin(14, machine.Pin.OUT)
    motor2A = machine.Pin(15, machine.Pin.OUT)

    def clockwise():
        motor1A.high()
        motor2A.low()

    def anticlockwise():
        motor1A.low()
        motor2A.high()

    def stopMotor():
        motor1A.low()
        motor2A.low()

    while True:
        clockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)
        anticlockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)



程序运行后，电机将会有规律的来回旋转。
如电流过大，Pico将可能与电脑断开连接，此时只需按下按键（让Pico的 **RUN** 引脚接收低电平）即可复位。