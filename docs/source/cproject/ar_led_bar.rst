Display the Level
=================


让我们来使用LED Bar Graph！ 这是一个常见的硬件显示器，可用来显示电量或者音量等级。它由一系列排成一排的LED组成。

|img_led_bar|


**Wiring**

|sch_ledbar|

|wiring_ledbar|

**Code**

.. code-block:: C

    void setup() {
        for(int i=6;i<=15;i++)
        {
            pinMode(i,OUTPUT);
        }
    }

    void loop() {
        for(int i=6;i<=15;i++)
        {
            digitalWrite(i,HIGH);
            delay(500);
            digitalWrite(i,LOW);
            delay(500);    
        }
    }

When the program is running, you 会看到LED Bar Graph上的灯依次闪烁。

**How it works?**

LED Bar上的十个LED各自需要用一个引脚来控制，这也意味着我们定义这十个引脚。
The codes in ``setup()`` use the for loop to initialize pins 6~15 to output mode in turn.

.. code-block:: C

    for(int i=6;i<=15;i++)
    {
        pinMode(i,OUTPUT);
    }   

The for loop is used in ``loop()`` to make the LED flash(turn on 0.5s, then turn off 0.5s) in sequence.

.. code-block:: C

    for(int i=6;i<=15;i++)
    {
        digitalWrite(i,HIGH);
        delay(500);
        digitalWrite(i,LOW);
        delay(500);    
    }