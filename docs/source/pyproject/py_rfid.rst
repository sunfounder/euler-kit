.. _py_rfid:


6.5 Radio Frequency Identification
================================================

Radio Frequency Identification (RFID) refers to technologies that involve using wireless communication between an object (or tag) and an interrogating device (or reader) to automatically track and identify such objects. The tag transmission range is limited to several meters from the reader. A clear line of sight between the reader and tag is not necessarily required.

Most tags contain at least one integrated circuit (IC) and an antenna. 
The microchip stores information and is responsible for managing the radio frequency (RF) communication with the reader. Passive tags do not have an independent energy source and depend on an external electromagnetic signal, provided by the reader, to power their operations. 
Active tags contain an independent energy source, such as a battery. 
Thus, they may have increased processing, transmission capabilities and range.

* :ref:`cpn_mfrc522`


**Schematic**

|sch_rfid|

**Wiring**



|wiring_rfid|

**Code**

Here you need to use the libraries in ``mfrc522`` folder, please check if it has been uploaded to Pico, for a detailed tutorial refer to :ref:`add_libraries_py`.

The main function is divided into two:

* ``6.5_rfid_write.py``: Used to write information to the card (or key).
* ``6.5_rfid_read.py``: used to read the information in the card (or key)


Open the ``6.5_rfid_write.py`` file under the path of ``euler-kit/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

After running you will be able to type message in the shell and then put the card (or key) close to the MFRC522 module to write the message in.

.. code-block:: python

    from mfrc522 import SimpleMFRC522

    reader = SimpleMFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=5,rst=0)

    def write():
        to_write = input("Please enter the message: ")
        print("Writing...Please place the card...")
        id, text = reader.write(to_write)
        print("ID: %s\nText: %s" % (id,text))

    write()

Open the ``6.5_rfid_read.py`` file under the path of ``euler-kit/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

After running, you will be able to read the message stored in the card (or key).

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