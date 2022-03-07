.. _py_somato_controller:


7.11 Somatosensory Controller
=============================


If you watch a lot of robot movies, then you should have seen images like this.
the protagonist turning his wrist, the giant robot also followed by turning his wrist.
The protagonist shakes his fist, and the robot follows suit, which is very cool.

This technology is already very common in universities and research institutes, and the arrival of 5G will greatly expand the scope of application of such technology.
For example, the "surgical robot da Vinci" remote surgery medical is a typical application.

Such a robotic system is usually divided into a human motion capture module and a robotic arm actuation module (some application scenarios also add a data communication module).

Here we use MPU6050 to implement human motion capture (e.g., mount it on a glove) and servo to represent robotic arm actuation to make a simple somatosensory control system.


**Schematic**


|sch_somato|

MPU6050 will get the acceleration value in each direction and calculate the attitude angle.

As the attitude angle changes, the program will also control the servo to make the corresponding deflection angle.

**Wiring**

|wiring_somatosensory_controller| 


**Code**


.. note::

    * Open the ``7.11_somatosensory_controller.py`` file under the path of ``euler-kit/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.
    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner.
    * Here you need to use the ``imu.py`` and ``vector3d.py``, please check if it has been uploaded to Pico, for a detailed tutorial refer to :ref:`add_libraries_py`.


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


Once the program is running, when you tilt the MPU6050 left and right (or turn your wrist left and right if it is mounted on a glove), the servo will turn left and right at the same time.