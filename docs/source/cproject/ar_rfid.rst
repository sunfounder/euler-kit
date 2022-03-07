Radio Frequency Identification
==============================

Radio Frequency Identification (RFID) refers to technologies that involve using wireless communication between an object (or tag) and an interrogating device (or reader) to automatically track and identify such objects. The tag transmission range is limited to several meters from the reader. A clear line of sight between the reader and tag is not necessarily required.

Most tags contain at least one integrated circuit (IC) and an antenna. 
The microchip stores information and is responsible for managing the radio frequency (RF) communication with the reader. Passive tags do not have an independent energy source and depend on an external electromagnetic signal, provided by the reader, to power their operations. 
Active tags contain an independent energy source, such as a battery. 
Thus, they may have increased processing, transmission capabilities and range.

* :ref:`cpn_mfrc522`


**Wiring**

|sch_rfid|

|wiring_rfid|

**Code**


The libraries ``MFRC522.h`` needs adding manually. 
Add Method: Refer to :ref:`apx_add_lib`.

主函数分为两个。 一个是 ``write`` ，运行后你将可以在串口monitor中输入message，以 ``#`` 结束，随后将卡片(或者key)靠近MFRC522模块，将message写入卡片中。

:raw-code:

另一个是 ``read`` ，运行后，你将能读取到卡片(或者key)中储存的message。

:raw-code:

**How it works?**

.. code-block:: arduino

    #include <MFRC522.h>

    #define RST_PIN         0
    #define SS_PIN          5

    MFRC522 mfrc522(SS_PIN, RST_PIN);

First, instantiate ``MFRC522()`` class.

为了简单使用， ``MFRC522`` 的库被进一步封装出以下函数。

* ``void simple_mfrc522_init()`` : 启动SPI通信，初始化mfrc522模块。
* ``void simple_mfrc522_get_card()`` : 暂停程序，直到检测到卡片(或者key)，打印卡片UID和PICC type。
* ``void simple_mfrc522_write(String text)`` : 为卡片(或者key)写入字符串。
* ``void simple_mfrc522_write(byte* buffer)`` : 为卡片(或者key)写入信息，这些信息通常来自串口。
* ``void simple_mfrc522_write(byte section, String text)`` : 为特定扇区写入字符串。section设为0，写入1-2扇区；section设为1，写入3-4扇区。
* ``void simple_mfrc522_write(byte section, byte* buffer)`` : 为特定扇区写入信息，这些信息通常来自串口。section设为0，写入1-2扇区；section设为1，写入3-4扇区。
* ``String simple_mfrc522_read()`` : 读取卡片(或者key)中的信息，返回字符串。
* ``String simple_mfrc522_read(byte section)`` : 读取特定扇区中的信息，返回字符串。section设为0，写入1-2扇区；section设为1，写入3-4扇区。


在 **white** 示例中，用到了 ``Serial.readBytesUntil()`` 函数，这是一个常用的串口输入方法。

* `Serial.readBytesUntil <https://www.arduino.cc/reference/en/language/functions/communication/serial/readbytesuntil/>`_