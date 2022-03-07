RFID Music Player
=================


RFID只能用来做门禁卡吗？让我们打开脑洞，玩出不一样的花样！
来做一个别开生面的音乐播放器吧！

通过之前的项目，我们知道 ``rfid_write.py`` 文件可以为 ID Card 写入一定量的信息（48个字母），
这些信息不仅仅可以是密钥和身份信息，还可以是乐谱。

运行 ``rfid_write.py`` 文件后，写入 ``EEFGGFEDCCDEEDD EEFGGFEDCCDEDCC`` ，
再将ID Card靠近MFRC522模块，一段 Ode an Joy 的乐谱就储存在里面了。

随后运行 ``rfid_music_player.py`` 文件，读取刚刚存入乐谱的ID Card，蜂鸣器将会播放这段音乐。

你可以在网上寻找到更多的乐谱，甚至可以自己编写一段音乐，将它们存入ID Card中，分享给朋友听吧！

**Wiring**

|sch_room_temp|

|wiring_room_temp|


**Code**

.. code-block:: python


    from mfrc522 import SimpleMFRC522
    import machine
    import time
    from ws2812 import WS2812
    import urandom

    # ws2812
    ws = WS2812(machine.Pin(16),8)

    # mfrc522
    reader = SimpleMFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=5,rst=0)

    # buzzer
    NOTE_C4 = 262
    NOTE_D4 = 294
    NOTE_E4 = 330
    NOTE_F4 = 349
    NOTE_G4 = 392
    NOTE_A4 = 440
    NOTE_B4 = 494
    NOTE_C5 = 523

    buzzer = machine.PWM(machine.Pin(15))
    note=[NOTE_C4,NOTE_D4,NOTE_E4,NOTE_F4,NOTE_G4,NOTE_A4,NOTE_B4,NOTE_C5]

    def tone(pin,frequency,duration):
        pin.freq(frequency)
        pin.duty_u16(30000)
        time.sleep_ms(duration)
        pin.duty_u16(0)


    # lightup
    def lumi(index):
        for i in range(8):
            ws[i] = 0x000000
        ws[index] = int(urandom.uniform(0, 0xFFFFFF))  
        ws.write() 

    # encode text to index
    words=["C","D","E","F","G","A","B","N"]
    def take_text(text):
        string=text.replace(' ','').upper()
        while len(string)>0:
            index=words.index(string[0])
            tone(buzzer,note[index],250)
            lumi(index)
            new_str=""
            for i in range(0, len(string)):
                if i != 0:
                    new_str = new_str + string[i]
            string=new_str

    # read card
    def read():
        print("Reading...Please place the card...")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
        take_text(text)
        
    read()

在运行该示例前，要先运行 ``rfid_write.py`` 文件，
写入一段乐谱。如写入一段Ode an Joy： ``EEFGGFEDCCDEEDD EEFGGFEDCCDEDCC`` 。
随后放置一张ID Card到MFRC522模块处，将这段乐谱写入ID Card。


完成上述步骤后，运行本示例文件，再一次将ID Card靠近MFRC522模块，蜂鸣器将会播放存入ID Card中的音乐。
同时RGB灯条也会在相应的位置点亮随机颜色的灯光。