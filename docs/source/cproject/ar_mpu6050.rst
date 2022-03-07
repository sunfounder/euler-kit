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

The libraries ``Adafruit_MPU6050.h`` needs adding manually. 
Add Method: Refer to :ref:`apx_add_lib`.

:raw-code:

运行程序后，你能看到三轴加速度计值和三轴陀螺仪值在循环输出。
此时你将MPU6050随意旋转，这些值也会出现相应的变化。
为了更容易查看数值变化，你可以注释掉其中一组print，专心查看另一组数据。

**How it works?**

实例化一个MPU6050对象。

.. code-block:: arduino

    #include <Adafruit_MPU6050.h>
    #include <Wire.h>

    Adafruit_MPU6050 mpu;


初始化MPU6050，并设置其精度。

.. code-block:: arduino

    void setup(void) {
        Serial.begin(115200);
        while (!Serial)
            delay(10); // will pause Zero, Leonardo, etc until serial console opens

        Serial.println("Adafruit MPU6050 test!");

        // Try to initialize!
        if (!mpu.begin()) {
            Serial.println("Failed to find MPU6050 chip");
            while (1) {
            delay(10);
            }
        }
        Serial.println("MPU6050 Found!");

        // Set range
        mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
        mpu.setGyroRange(MPU6050_RANGE_500_DEG);
        mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

        Serial.println("");
        delay(100);
    }

Get new sensor events with the readings.

.. code-block:: arduino

    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp);

随后，你将能在 ``a.acceleration.x``, ``a.acceleration.y``, ``a.acceleration.z``, 
``g.gyro.x``, ``g.gyro.y``, ``g.gyro.z`` 这几个数据中得到实时的加速度和角速度值。

.. code-block:: arduino

    Serial.print("Acceleration X: ");
    Serial.print(a.acceleration.x);
    Serial.print(", Y: ");
    Serial.print(a.acceleration.y);
    Serial.print(", Z: ");
    Serial.print(a.acceleration.z);
    Serial.println(" m/s^2");

    Serial.print("Rotation X: ");
    Serial.print(g.gyro.x);
    Serial.print(", Y: ");
    Serial.print(g.gyro.y);
    Serial.print(", Z: ");
    Serial.print(g.gyro.z);
    Serial.println(" rad/s");