Somatosensory Controller
=============================


如果你经常观看机器人电影，那你应当见过这样的画面：
主角转动手腕，巨大的机器人也跟着转动手腕；
主角握拳，机器人也跟着握拳，非常酷炫。

这种技术在高校和研究所等场所已经用的很普遍，而5G的到来更是会极大地拓展这类技术的应用范围。
比如“手术机器人达芬奇”的远程手术医疗便是一个典型的应用。

这样的机器人系统通常分为人体动作捕捉模块和机械臂执行模块（一些应用场景还会加上数据通信模块）。
在这里我们用MPU6050实现人体动作捕捉(比如，将它安装在手套上)，
用servo代表机械臂的执行，
制作一个简单的somatosensory control system.


**Schematic**


|sch_somatosensory_controller| 

MPU6050会获取各个方向的加速度值，并且计算出姿态角。

随着姿态角的变化，程序也会控制舵机做出相应的偏转角度。

**Wiring**

|wiring_somatosensory_controller| 


**Code**

.. code-block:: python


    from imu import MPU6050
    from machine import I2C, Pin
    import time
    import math

    # mpu6050
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

    # servo
    servo = machine.PWM(machine.Pin(16))
    servo.freq(50)


    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min



    # get rotary angle
    def dist(a,b):
        return math.sqrt((a*a)+(b*b))

    def get_y_rotation(x,y,z):
        radians = math.atan2(x, dist(y,z))
        return -math.degrees(radians)

    def get_x_rotation(x,y,z):
        radians = math.atan2(y, dist(x,z))
        return math.degrees(radians)

    # servo work
    def servo_write(pin,angle):
        pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)
        duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))
        pin.duty_u16(duty)

    times=25
    while True:
        total=0 
        for i in range(times):
            angle=get_y_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z) #get rotation value
            total+=angle
        average_angle=int(total/times) # make the value smooth
        servo_write(servo,interval_mapping(average_angle,-90,90,0,180))


程序运行后，当你左右倾斜MPU6050（如果它安装在手套上，则是左右转动手腕），舵机将会将角度偏转到对应的位置。