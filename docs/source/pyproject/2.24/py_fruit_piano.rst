Fruit Piano
===========

人体是导电的。一块水果也会导电，基本上其他任何有机的东西也是如此。
我们可以利用这一特性来创建一个有趣的小项目：水果钢琴。
更准确的说，我们将水果变成键盘，只需轻轻触摸不同的水果即可播放音乐，就像施了魔法一样。

**Schematic**

|wiring_fruit_piano| 

电路搭建完成后，你还需要用多根杜邦线来连接MPR121上的电极与水果（如插至香蕉柄中），这样才能让水果变成琴键。

当程序开始运行，MPR121会初始化，各个电极会根据当前的电荷得到一个数值，当导体(如人体)触碰到电极，电荷将会发生转移，重新达到平衡。
此时电极得到的数值和初始化时得到的数值有差异，从而告诉主控板该电极被触碰了。
这个过程中需要注意的是，要确保初始化时，各个电极的接线稳定，使其电荷处于平衡状态。
如接入到水果上，导线与水果之间会随着桌子晃动而松动，那么电荷就会持续转移，从而让主控板误以为其一直处于激发状态。



**Wiring**


|wiring_fruit_piano| 


**Code**

.. code-block:: python

    from mpr121 import MPR121
    from machine import Pin, I2C
    import time
    import urandom

    # mpr121
    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)


    # buzzer
    NOTE_A3 = 220
    NOTE_B3 = 247
    NOTE_C4 = 262
    NOTE_D4 = 294
    NOTE_E4 = 330
    NOTE_F4 = 349
    NOTE_G4 = 392
    NOTE_A4 = 440
    NOTE_B4 = 494
    NOTE_C5 = 523
    NOTE_D5 = 587
    NOTE_E5 = 659

    buzzer = machine.PWM(machine.Pin(15))
    note = [NOTE_A3,NOTE_B3,NOTE_C4,NOTE_D4,NOTE_E4,NOTE_F4,NOTE_G4,NOTE_A4,NOTE_B4,NOTE_C5,NOTE_D5,NOTE_E5]

    def tone(pin,frequency):
        pin.freq(frequency)
        pin.duty_u16(30000)

    def noTone(pin):
        pin.duty_u16(0)


    # rgb led
    red = machine.PWM(machine.Pin(13))
    green = machine.PWM(machine.Pin(12))
    blue = machine.PWM(machine.Pin(11))
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


    def lightup():
        red.duty_u16(int(urandom.uniform(0, 65535)))
        green.duty_u16(int(urandom.uniform(0, 65535)))
        blue.duty_u16(int(urandom.uniform(0, 65535)))


    def dark():
        red.duty_u16(0)
        green.duty_u16(0)
        blue.duty_u16(0)    

    # main project
    lastState=mpr.get_all_states()
    touchMills=time.ticks_ms()
    beat=500

    while True:
        currentState=mpr.get_all_states()
        if currentState != lastState:
            for i in range(12):
                if i in list(currentState) and not i in list(lastState):
                    tone(buzzer,note[i])
                    lightup()
                    touchMills=time.ticks_ms()
        if time.ticks_diff(time.ticks_ms(),touchMills)>=beat or len(currentState) == 0:
            noTone(buzzer)
            dark()
        lastState = currentState

程序运行前，请勿触碰水果，避免初始化时获取到非正确的基准。
程序运行后，轻轻触碰水果，蜂鸣器会发出对应的音调，RGB灯也会随机闪烁一次。