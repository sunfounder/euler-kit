.. _setup_pico_micropython:

1.2 Set up Your Pico
------------------------------


1. Hold down the **BOOTSEL** button and connect the Pico to your computer with a Micro USB cable.
#. Once your Pico is mounted as a Mass Storage Device called RPI-RP2, release the BOOTSEL button.

    |mps_bootsel_onboard|

#. When you open the drive, you'll see two files: **INDEX.HTM** and **INFO_UF2.TXT**. Open INDEX.HTM in your browser by double-clicking it.

    * **INDEX.HTM** : This is a welcome page that tells you everything about your Pico.
    * **INFO_UF2.TXT** : Contains the version of the bootloader it's currently running.

        |mps_index_htm|

#. When the browser opens, click **MicroPython**.

    |mps_welcome_pico|

#. Please scroll down to the "Drag-and-Drop MicroPython" section and then click the "Micropython UF2" link to download MicroPython firmware.

    |mps_download_uf2|

#. Go to the **Downloads** folder and find the file you just downloaded - it should be called 'rp2_pico_xxxx.uf2', then drag it to the **RPI-RP2** storage drive. The Pico will reboot and disappear from the File Manager.

    |mps_move_uf2|

.. note::

    Please ignore the warning that a **drive was removed without being ejected**, that's supposed to happen!
    
    As soon as you dragged the MicroPython firmware file onto your Pico, the firmware was flashed into its internal storage.
    The Pico then switches out of the special mode you put it in with the 'BOOTSEL' button, flashes the new firmware, and then loads it (meaning your Pico is now running MicroPython).

Congratulations: your Raspberry Pi Pico is now ready to run MicroPython!
