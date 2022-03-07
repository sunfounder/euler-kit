Passager Counter
================

客流量是大型商场、购物中心、连锁店、机场、车站、博物馆、
展览馆等公共场所在管理和决策方面不可缺少的数据。

如在机场和车站等，为了人员的安全保障和顺畅流通，需要严格控制人数，避免超出承载能力。
对于购物中心和连锁店等，还可以更进一步得知哪个时间段的游客较多，每个用户能产生多少订单等等，
从而分析出人们的消费习惯，获取更多的营业额。

综上所述，一个passager counter可以帮助人们了解这些公共场所的运行状况，进行有效的组织运营工作！

在这里我们用一个PIR sensor制作一个简易的passager counter，并用四位数码管显示人流量。


**Schematic**

|wiring_passager_coumter| 

PIR会在有人经过的时候发出一个长约2.8s的高电平信号。
主控板每接到一次上升沿信号，将会把计数增加一。

**Wiring**


|wiring_passager_coumter| 


**Code**

.. code-block:: python

    import machine
    import time


    pir_sensor = machine.Pin(16, machine.Pin.IN)

    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)

    placePin = []
    pin = [10,13,12,11]
    for i in range(4):
        placePin.append(None)
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

    count = 0


    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)
        placePin[digit].value(0)

    def clearDisplay():
        hc595_shift(0x00)

    def hc595_shift(dat):
        rclk.low()
        time.sleep_us(200)
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_us(200)
            value = 1 & (dat >> bit)
            sdi.value(value)
            time.sleep_us(200)
            srclk.high()
            time.sleep_us(200)
        time.sleep_us(200)
        rclk.high()

    def motion_detected(pin):
        global count
        count = count+1

    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

    while True:
        #print(count)
        
        pickDigit(0)
        hc595_shift(SEGCODE[count%10])

        pickDigit(1)
        hc595_shift(SEGCODE[count%100//10])
        
        pickDigit(2)
        hc595_shift(SEGCODE[count%1000//100])
        
        pickDigit(3)
        hc595_shift(SEGCODE[count%10000//1000])    


