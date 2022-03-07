6-axis Motion Tracking
======================


The MPU-6050 is a 6-axis(combines 3-axis Gyroscope, 3-axis Accelerometer) motion tracking devices.


静止在地球表面上的加速度计将测量由地球重力引起的加速度，直接向上，g ≈ 9.81 m/s^2。
相比之下，自由落体中的加速度计（以大约 9.81 m/s^2 的加速度落向地球中心）将测量为零。

加速度计在工业和科学中有很多用途。
高度灵敏的加速度计用于飞机和导弹的惯性导航系统。
旋转机器中的振动由加速度计监测。
它们用于平板电脑和数码相机让屏幕上的图像始终垂直显示。
在无人机中，加速度计有助于稳定飞行。

陀螺仪是用于测量或维护设备的orientation 和 angular velocity。

陀螺仪的应用包括惯性导航系统（例如在哈勃望远镜中，或在水下潜艇的钢壳内）、
汽车防侧翻和安全气囊系统、摄影设备的图像稳定系统、智能设备的运动感应系统、无人机的姿态稳定系统等等。

* :ref:`cpn_mpu6050`

**Wiring**

|sch_mpu6050|

|wiring_mpu6050|

**Code**

你需要先把 ``imu.py`` 和 ``vector3d.py`` 存入pico作为库使用。 

然后，运行主程序。

.. code-block:: python

    from imu import MPU6050
    from machine import I2C, Pin
    import time

    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

    while True:
        print("x: %s, y: %s, z: %s"%(mpu.accel.x, mpu.accel.y, mpu.accel.z))
        time.sleep(0.1)
        print("A: %s, B: %s, Y: %s"%(mpu.gyro.x, mpu.gyro.y, mpu.gyro.z))
        time.sleep(0.1)

运行程序后，你能看到三轴加速度计值和三轴陀螺仪值在循环输出。
此时你将MPU6050随意旋转，这些值也会出现相应的变化。
为了更容易查看数值变化，你可以注释掉其中一句print，专心查看另一组数据。

**How it works?**

在imu库中，我们将相关功能集成到了MPU6050类中。
MPU6050是一个I2C模块，需要定义一组I2C引脚，用于初始化。

.. code-block:: python

    from imu import MPU6050
    from machine import I2C, Pin

    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

随后，你将能在 ``mpu.accel.x``, ``mpu.accel.y``, ``mpu.accel.z``, ``mpu.gyro.x``, ``mpu.gyro.y``, ``mpu.gyro.z`` 这几个数据中得到实时的加速度和角速度值。

.. code-block:: python

    while True:
        print("x: %s, y: %s, z: %s"%(mpu.accel.x, mpu.accel.y, mpu.accel.z))
        time.sleep(0.1)
        print("A: %s, B: %s, Y: %s"%(mpu.gyro.x, mpu.gyro.y, mpu.gyro.z))
        time.sleep(0.1)