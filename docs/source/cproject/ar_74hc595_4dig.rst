Time Counter
================================


4-Digit 7-segment display consists of four 7- segment displays working
together.

The 4-digtal 7-segment display works independently. It uses the
principle of human visual persistence to quickly display the characters
of each 7-segment in a loop to form continuous strings.

For example, when "1234" is displayed on the display, "1" is displayed
on the first 7-segment, and "234" is not displayed. After a period of
time, the second 7-segment shows "2", the 1st 3th 4th of 7-segment does
not show, and so on, the four digital display show in turn. This process
is very short (typically 5ms), and because of the optical afterglow
effect and the principle of visual residue, we can see four characters
at the same time.


**Wiring**


|sch_4dig|

|wiring_4dig|

**Code**

:raw-code:

程序运行后，你将能看到四位数码管变成了一个计数器，每秒数字增加1。

**How it works?**

为每一个七段数码管写入信号的方式与 :ref:`ar_7seg` 是一样的，使用 ``shiftOut()`` 函数。
四位数码管的核心要点，就是有选择性的激活各个七段数码管。与之相关的代码如下：

.. code-block:: arduino

    const int placePin[4] = {13,12,11,10}; 

    void setup ()
    {
        for (int i = 0; i<4;i++){
            pinMode(placePin[i],OUTPUT);
        }
    }

    void loop()
    { 
        pickDigit(0);
        hc595_shift(count%10/1);
        
        pickDigit(1);
        hc595_shift(count%100/10);
        
        pickDigit(2);
        hc595_shift(count%1000/100);
        
        pickDigit(3);
        hc595_shift(count%10000/1000);
    }

    void pickDigit(int digit){
        for(int i = 0; i < 4; i++){
            digitalWrite(placePin[i],HIGH);
        }
        digitalWrite(placePin[digit],LOW);
    }

在这里，用了4个引脚(GP10，GP11，GP12，GP13)来单独控制四位数码管的各个位。
当这些引脚状态为 ``LOW`` 时，相应的数码管激活；状态为 ``HIGH`` 时，则相反。

在这里 ``pickDigit(digit)`` 函数的作用就是unable所有四个数码管后，单独启用特定的某个数码管。
随后，用 ``hc595_shift()`` 为数码管写入对应的 8 bits code即可。

四位数码管需要持续性的轮流激活各个数码管，从而让我们能看到它显示四位数字，这就意味着主程序中不能轻易添加会影响时序的代码。
然而我们又需要在这个这个示例中添加计时功能，如果增加一个 ``delay(1000)``，
我们就会识破它四个数码管同时工作的假象，暴露出一次只有一个数码管发光的事实。
那么，使用 ``millis()`` 函数，就是一个绝佳的方法。

.. code-block:: arduino

    void setup ()
    {
        timerStart = millis();
    }

    void loop()
    {
        unsigned int count = (millis()-timerStart)/1000;
    }

``millis()`` 函数可以获取开始运行当前程序以来经过的毫秒数，
我们把首次获取的时间值记录为 ``timerStart`` ，
随后在需要获取时间时，重新调用 ``millis()`` 函数，
把值减去  ``timerStart`` ，就能得到程序运行了多久。

最后，把这个时间值转化并输出到四位数码管就可以了。

* `millis() <https://www.arduino.cc/reference/en/language/functions/time/millis/>`_