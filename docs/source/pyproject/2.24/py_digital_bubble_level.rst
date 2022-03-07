Digital Bubble Level
============================

`Bubble Level <https://en.wikipedia.org/wiki/Spirit_level>`_ 通常用于建筑、木工和摄影，
以确定您正在处理的物体是否水平。
如果使用得当，气泡水平仪可以帮助您制作完美平整的家具，
在墙上挂画或其他物品时帮助您，水平台球桌，水平乒乓球桌，
设置照片三脚架，水平拖车或露营车等等。它是任何家庭或公寓的必备设备。

在这里我们用MPU6050和8x8 led matrix制作一个Digital Bubble Level，
当你偏转MPU6050的时候，LED matrix上的 bubble 也会偏移位置。

**Schematic**

|sch_digital_bubble_level| 

MPU6050会获取各个方向的加速度值，并且计算出姿态角。

程序为两个74HC595芯片写入了一组数据，从而在点阵上绘制出一个2x2的Dot。

随着姿态角的改变，程序发送给芯片的数据也会不同，Dot的位置被改变，这样就形成了水平仪的效果。



**Wiring**


|wiring_digital_bubble_level| 


**Code**

.. code-block:: python

    import machine
    from machine import I2C, Pin
    import time
    import math
    from imu import MPU6050


    ### mpu6050
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

    # get rotary angle
    def dist(a,b):
        return math.sqrt((a*a)+(b*b))

    def get_y_rotation(x,y,z):
        radians = math.atan2(x, dist(y,z))
        return -math.degrees(radians)

    def get_x_rotation(x,y,z):
        radians = math.atan2(y, dist(x,z))
        return math.degrees(radians)

    def get_angle():
        y_angle=get_y_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z) 
        x_angle=get_x_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z) 
        return x_angle,y_angle

    ### led matrix display
    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)

    def hc595_in(dat):
        for bit in range(7,-1, -1):
            srclk.low()
            time.sleep_us(30)
            sdi.value(1 & (dat >> bit))
            time.sleep_us(30)
            srclk.high()

    def hc595_out():
        rclk.high()
        time.sleep_us(200)
        rclk.low()

    def display(glyph):
        for i in range(0,8):
            hc595_in(glyph[i])
            hc595_in(0x80>>i)
            hc595_out()

    # data transformation
    def matrix_2_glyph(matrix):
        glyph= [0 for i in range(8)] # glyph code for display()
        for i in range(8):
            for j in range(8):
                glyph[i]+=matrix[i][j]<<j
        return glyph

    def clamp_number(val, min, max):
        return min if val < min else max if val > max else val

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Calculate the position of the bubble
    sensitivity=4          # The higher the number, the more sensitive
    matrix_range=7         # The size of the matrix is 8, so the coordinate range is 0~7
    point_range=matrix_range-1     # The x, y value of the bubble's marker point (upper left point) should be between 0-6
    def bubble_position():
        x,y=get_angle()
        x=int(clamp_number(interval_mapping(x,-90,90,0-sensitivity,point_range+sensitivity),0,point_range))
        y=int(clamp_number(interval_mapping(y,-90,90,point_range+sensitivity,0-sensitivity),0,point_range))
        return [x,y]

    # Drop the bubble into empty matrix
    def drop_bubble(matrix,bubble):
        matrix[bubble[0]][bubble[1]]=0
        matrix[bubble[0]+1][bubble[1]]=0
        matrix[bubble[0]][bubble[1]+1]=0
        matrix[bubble[0]+1][bubble[1]+1]=0
        return matrix

    while True:
        matrix= [[1 for i in range(8)] for j in range(8)]  # empty matrix
        bubble=bubble_position() # bubble coordinate
        matrix=drop_bubble(matrix,bubble) # drop the bubble into empty matrix
        display(matrix_2_glyph(matrix)) # show matrix

在你运行程序后，将面包板放置在水平的桌面，
你会看到一个光球出现在LED matrix的正中央（如果不在中央，则可能是MPU6050没放平，请稍作调整），
随后你偏转面包板，光球会往你偏转的方向移动。