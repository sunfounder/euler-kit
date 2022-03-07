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

你需要将  ``mfrc522`` 文件夹存入pico，里面的文件与RFID的使用关系密切。

主函数分为两个。 一个是 ``write`` ，运行后你将可以在Shell中输入message，随后将卡片(或者key)靠近MFRC522模块，将message写入卡片中。

.. code-block:: python

    from mfrc522 import SimpleMFRC522

    reader = SimpleMFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=5,rst=0)

    def write():
        to_write = input("Please enter the message: ")
        print("Writing...Please place the card...")
        id, text = reader.write(to_write)
        print("ID: %s\nText: %s" % (id,text))

    write()

另一个是 ``read`` ，运行后，你将能读取到卡片(或者key)中储存的message。

.. code-block:: python

    from mfrc522 import SimpleMFRC522

    reader = SimpleMFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=5,rst=0)

    def read():
        print("Reading...Please place the card...")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))

    read()

**How it works?**


.. code-block:: python

    from mfrc522 import SimpleMFRC522

    reader = SimpleMFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=5,rst=0)

Instantiate ``SimpleMFRC522()`` class.

.. code-block:: python

    id, text = reader.read()

This function is used to read card data. If the reading is successful, id and text will be returned.

.. code-block:: python

    id, text = reader.write("text")

This function is used to write information to the card, press **Enter** key to finish writing. 
``text`` is the information to be written to the card.