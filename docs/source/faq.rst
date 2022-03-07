FAQ
=========

Q1: NO MicroPython(Raspberry Pi Pico) Interpreter Option on Thonny IDE?
--------------------------------------------------------------------------

|faq_interepter_thonny|


* Check that your Pico is plugged into your computer via a USB cable.
* Check that you have installed MicroPython for Pico (:ref:`Installing MicroPython`).
* The Raspberry Pi Pico interpreter is only available in version 3.3.3 or higher version of Thonny. If you are running an older version, please update (:ref:`Thonny Python IDE`).
* Plug in/out the micro USB cable sveral times.

Q2: Cannot open Pico code or save code to Pico via Thonny IDE?
------------------------------------------------------------------------

|faq_save_to_pico|

* Check that your Pico is plugged into your computer via a USB cable.
* Check that you have selected the Interpreter as **MicroPython (Raspberry Pi Pico)**.

Q3: Can Raspberry Pi Pico be used on Thonny and Arduino at the same time?
--------------------------------------------------------------------------------

NO, you need to do some different operations.

* If you used it on Arduino first, and now you want to use it on Thonny IDE, you need to :ref:`Installing MicroPython` on it.
* If you used it on Thonny first， and now you want to use it on Arduino IDE, you need to :ref:`Setup the Raspberry Pi Pico`.

Q4: Code upload failed in Arduino IDE?
-----------------------------------------
* Check that your Pico is correctly recognised by the Arduino IDE, the port should be COMXX (Raspberry Pi Pico), for instructions please refer to :ref:`Setup the Raspberry Pi Pico`.
* Check that the Board(Raspberry Pi Pico) or port（COMXX (Raspberry Pi Pico)）is selected correctly.
* If your code is OK and you have selected the correct board and port, but the upload is still not successful. At this point you can click on the **Upload** icon again, when the progress below shows "Upload...", unplug the USB cable, then press and hold the **BOOTSEL** button to plug it in and the code will be uploaded successfully.
