
.. _download_upload:

1.4 Download and Upload the Code
===============================================

**Download the Code**

Download the relevant code from the link below.


* :download:`SunFounder Euler Kit Example <https://github.com/sunfounder/euler-kit/archive/refs/heads/main.zip>`

* Or check out the code at `Euler Kit - GitHub <https://github.com/sunfounder/euler-kit>`_

.. _add_libraries_py:

Upload the Libraries to Pico
----------------------------------

In some projects, you will need additional libraries. So here we upload these libraries to Raspberry Pi Pico first, and then we can run the code directly later.

Click **View** -> **Files** in the top navigation bar of Thonny IDE.

|mps_th_files|

Go to the folder where you downloaded the `code package <https://github.com/sunfounder/euler-kit/archive/refs/heads/main.zip>`_ before, and then go to the ``micropython/`` folder.

|mps_th_path|

Select "MicroPython (Raspberry Pi Pico)" from the interpreter selection button in the bottom right corner, but make sure that your Raspberry Pi Pico is connected to your computer via a Micro USB cable.

|mps_interpreter|

The drive **Raspberry Pi Pico/** will appear, and the next step is to upload all the code and library files to it.

|mps_th_pico|

Each project has its own **.py** file with serial numbers. To avoid increasing Pico's usage, only select ``.py`` files and folders without serial numbers.

It will take a while for the file to upload after clicking **Upload to**.

|mps_th_upload|

Now you will see the files you just uploaded inside your drive ``Raspberry Pi Pico``.

|mps_th_done|
