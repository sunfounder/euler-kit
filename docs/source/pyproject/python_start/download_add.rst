
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

In some projects, some additional libraries are needed. So here we upload these libraries to Raspberry Pi Pico first, and then we can run the code directly later.

Open Thonny IDE, in the top navigation bar, click **View** -> **Files**.

|mps_th_files|

Switch the path to the folder where you downloaded the `code package <https://github.com/sunfounder/euler-kit/archive/refs/heads/main.zip>`_ before, and then go to the ``micropython/`` folder.

|mps_th_path|

Plug the Pico into your computer with a micro USB cable and click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner.

|mps_interpreter|

Then the drive ``Raspberry Pi Pico/`` will appear, and the next thing we need to do is to upload all the code and library files to this drive.

|mps_th_pico|

The ``.py`` files with serial numbers are example code for each project. In order not to increase Pico's usage, you can only select the ``.py`` files and folders without serial numbers.

Then click **Upload to**, it will take a while to upload.

|mps_th_upload|

Now you will see the files you just uploaded inside your drive ``Raspberry Pi Pico``.

|mps_th_done|
