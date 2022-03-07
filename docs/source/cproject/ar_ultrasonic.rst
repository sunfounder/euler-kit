Measuring Distance
==================

超声波传感器的工作原理是声纳和雷达系统，用于确定与物体的距离。

* :ref:`cpn_ultrasonic`

**Wiring**

|sch_ultrasonic|

|wiring_ultrasonic|

**Code**

:raw-code:

程序运行后，串口监视器将打印出超声波传感器距离前方障碍物的距离。

**How it works?**

About the application of ultrasonic sensor, we can directly check the
subfunction.

.. code-block:: arduino

    float readSensorData(){// ...}

PING is triggered by a HIGH pulse of 2 or more microseconds. (Give a
short LOW pulse beforehand to ensure a clean HIGH pulse.)

.. code-block:: arduino

    digitalWrite(trigPin, LOW); 
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH); 
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW); 

The echo pin is used to read signal from PING, a HIGH pulse whose
duration is the time (in microseconds) from the sending of the ping to
the reception of echo of the object.

.. code-block:: arduino

    microsecond=pulseIn(echoPin, HIGH);

The speed of sound is 340 m/s or 29 microseconds per centimeter.

This gives the distance travelled by the ping, outbound and return, so
we divide by 2 to get the distance of the obstacle.

.. code-block:: arduino

    float distance = microsecond / 29.00 / 2;  


需要注意的是，超声波传感器在工作时会将程序暂停。
这在编写复杂的项目时，可能会导致一些卡顿。

