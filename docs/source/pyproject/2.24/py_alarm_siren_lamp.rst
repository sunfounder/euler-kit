Alarm Siren Lamp
================



在生活中(或者在电影中)，你能经常看到警号灯。
它一般用于维护交通，起警示作用，是保护人民生命财产安全的重要道具，常出没在警车﹑工程车、消防车﹑急救车上。
如果你看到它的灯光或者听到它的声音，那你就要当心了，这意味着你（或者周围的人）可能处于危险状态。

在这里我们用LED和蜂鸣器制造一个小型的警号灯，并用一个滑动开关来启动它。


**Schematic**

|sch_alarm_siren_lamp|

GP17串联一个10kΩ电阻后，连接到slider switch的中央lead，这使得slider往左右拨动后，能输出高电平或者低电平。
从而作为开关，切换LED和无源蜂鸣器的工作与停止。

当GP15输出高电平时，S8050（NPN晶体管）导通，无源蜂鸣器开始发声。
通过编程使得无源蜂鸣器的频率逐渐变高，以此发出带变调效果的鸣笛声。
GP16连接到LED，同样由程序控制，使其周期性的改变亮度，模拟出警铃的效果。


**Wiring**

|wiring_alarm_siren_lamp|


**Code**

.. code-block:: python

    import machine
    import time


    buzzer = machine.PWM(machine.Pin(15))
    led = machine.PWM(machine.Pin(16))
    led.freq(1000)

    switch = machine.Pin(17,machine.Pin.IN)

    def noTone(pin):
        pin.duty_u16(0)


    def tone(pin,frequency):
        pin.freq(frequency)
        pin.duty_u16(30000)

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def toggle(pin):
        global bell_flag
        bell_flag = not bell_flag
        print(bell_flag)
        if bell_flag:
            switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=toggle)
        else:
            switch.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle)


    bell_flag = False
    switch.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle)



    while True:
        if bell_flag == True:
            for i in range(0,100,2):
                led.duty_u16(int(interval_mapping(i,0,100,0,65535)))
                tone(buzzer,int(interval_mapping(i,0,100,130,800)))
                time.sleep_ms(10)
        else:
            noTone(buzzer)
            led.duty_u16(0)

程序运行后，将拨动开关拨到左侧，蜂鸣器会发出渐变的警示音，LED也会相应的改变亮度；将拨动开关拨到右侧，蜂鸣器和LED会停止工作。