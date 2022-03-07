
8x8 Pixel Graphics
=======================

LED 矩阵是一个低分辨率的dot-matrix display。它使用的阵列的发光二极管作为像素用于图案显示。

它们的亮度充足，使它们可以在户外阳光下清晰可见，你可以在一些商店，广告牌，标志，以及可变信息显示屏(如公交车辆上的)上看到它们的身影。。

在这个套件中使用的是一个8x8的点阵，拥有16个引脚。它们的阳极按行连接，阴极按列连接(在电路层面)，共同控制这64颗LED。
如要点亮第一颗LED，应为Row1提供高电平，为Col1提供低电平。点亮第二颗LED，则应为Row1提供高电平，为Col2提供低电平，以此类推。
通过控制通过每对行和列的电流，可以单独控制每个LED，从而显示字符或图片。

* :ref:`cpn_788bs`
* :ref:`cpn_74hc595`

**Schematic**

|sch_ledmatrix|

**Wiring**

Build the circuit. Since the wiring is complicated, let's
make it step by step.

**Step 1:**  First, insert the pico, the LED dot matrix
and two 74HC595 chips into breadboard. Connect the 3.3V and GND of the
pico to holes on the two sides of the board, then hook up pin16 and
10 of the two 74HC595 chips to VCC, pin 13 and pin 8 to GND.

.. note::
   In the Fritzing image above, the side with label is at the bottom.

|wiring_ledmatrix_4|

**Step 2:** Connect pin 11 of the two 74HC595 together, and then to
GP20; then pin 12 of the two chips, and to GP19; next, pin 14 of the
74HC595 on the left side to GP18 and pin 9 to pin 14 of the second
74HC595.

|wiring_ledmatrix_3|

**Step 3:** The 74HC595 on the right side is to control columns of the
LED dot matrix. See the table below for the mapping. Therefore, Q0-Q7
pins of the 74HC595 are mapped with pin 13, 3, 4, 10, 6, 11, 15, and 16
respectively.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **13** | **3**  | **4**  | **10** | **6**  | **11** | **15** | **16** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_2|

**Step 4:** Now connect the ROWs of the LED dot matrix. The 74HC595 on
the left controls ROW of the LED dot matrix. See the table below for the
mapping. We can see, Q0-Q7 of the 74HC595 on the left are mapped with
pin 9, 14, 8, 12, 1, 7, 2, and 5 respectively.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **9**  | **14** | **8**  | **12** | **1**  | **7**  | **2**  | **5**  |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_1|

**Code**

.. code-block:: python

    import machine
    import time

    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)


    glyph = [0xFF,0xBB,0xD7,0xEF,0xD7,0xBB,0xFF,0xFF]

    # Shift the data to 74HC595
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

    while True:
        for i in range(0,8):
            hc595_in(glyph[i])
            hc595_in(0x80>>i)
            hc595_out()

程序运行后，你将能看到LED点阵上显示一个 **x** 图形。


**How it works?**

在这里我们使用两个74HC595来分别为点阵的行和列提供信号。
提供信号的方法与前几个篇章的 ``hc595_shift(dat)`` 是一致的，区别在于此处需要一次写入16-bit binary number.
于是我们将 ``hc595_shift(dat)`` 拆分成了 ``hc595_in(dat)`` 和 ``hc595_out()`` 两个函数。

.. code-block:: python

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

随后，在主循环中调入两次 ``hc595_in(dat)`` ，写入两个8-bit binary number后再调用 ``hc595_out()`` ，这样就能显示一张图案了。

但是，由于点阵中的LED们使用了公共极，同时控制多行/多列会相互干扰（如同时点亮(1,1)和(2,2)，(1,2)和(2,1)会不可避免的被一起点亮）。
因此，需要一次只激活一列(或者一行)，循环8次，用残像原理让人眼合并8张图案，这样才能让得到一副含有8x8信息量的图案。

.. code-block:: python

    while True:
        for i in range(0,8):
            hc595_in(glyph[i])
            hc595_in(0x80>>i)
            hc595_out()

在这个示例中，主函数嵌套了一个for循环，当 ``i`` 为1时，只激活首行(控制行的芯片获取到数值 ``0x80`` )，写入第一行的图像。 
``i``为2时，激活第二行(控制行的芯片获取到数值 ``0x40`` )，写入第二行的图像。以此类推，完成8次输出。

顺带一提，与四位数码管一样，它也要保持刷新率，以防止被人眼看到闪烁，因此主循环中应当尽量避免使用额外的 ``sleep()`` 。

**What more?**

尝试把 ``glyph`` 换成以下数组，看看会出现什么图像吧！

.. code-block:: python

    glyph1 = [0xFF,0xEF,0xC7,0xAB,0xEF,0xEF,0xEF,0xFF]
    glyph2 = [0xFF,0xEF,0xEF,0xEF,0xAB,0xC7,0xEF,0xFF]
    glyph3 = [0xFF,0xEF,0xDF,0x81,0xDF,0xEF,0xFF,0xFF]
    glyph4 = [0xFF,0xF7,0xFB,0x81,0xFB,0xF7,0xFF,0xFF]
    glyph5 = [0xFF,0xBB,0xD7,0xEF,0xD7,0xBB,0xFF,0xFF]
    glyph6 = [0xFF,0xFF,0xF7,0xEB,0xDF,0xBF,0xFF,0xFF]

或者，你也可以尝试绘制属于自己的图形。