
IR Remote Control
================================

在消费电子产品中，遥控器可用于操作电视机、DVD播放机等设备。
在某些情况下，遥控器允许人们操作他们无法触及的设备，例如中央空调。

IR Receiver is a component with photocell that is tuned to receive to infrared light. 
It is almost always used for remote control detection - every TV and DVD player has one of these in the front to receive for the IR signal from the clicker. 
Inside the remote control is a matching IR LED, which emits IR pulses to tell the TV to turn on, off or change channels.

* :ref:`cpn_irrecv`


**Wiring**

|sch_irrecv|

|wiring_irrecv|


**Code**

你需要将  ``ir_rx`` 文件夹存入pico，里面的文件与IR接收器的使用关系密切。

然后，运行主程序。

.. code-block:: python

    import time
    from machine import Pin, freq
    from ir_rx.print_error import print_error
    from ir_rx.nec import NEC_8

    pin_ir = Pin(17, Pin.IN)

    def decodeKeyValue(data):
        if data == 0x16:
            return "0"
        if data == 0x0C:
            return "1"
        if data == 0x18:
            return "2"
        if data == 0x5E:
            return "3"
        if data == 0x08:
            return "4"
        if data == 0x1C:
            return "5"
        if data == 0x5A:
            return "6"
        if data == 0x42:
            return "7"
        if data == 0x52:
            return "8"
        if data == 0x4A:
            return "9"
        if data == 0x09:
            return "+"
        if data == 0x15:
            return "-"
        if data == 0x7:
            return "EQ"
        if data == 0x0D:
            return "U/SD"
        if data == 0x19:
            return "CYCLE"
        if data == 0x44:
            return "PLAY/PAUSE"
        if data == 0x43:
            return "FORWARD"
        if data == 0x40:
            return "BACKWARD"
        if data == 0x45:
            return "POWER"
        if data == 0x47:
            return "MUTE"
        if data == 0x46:
            return "MODE" 
        return "ERROR"

    # User callback
    def callback(data, addr, ctrl):
        if data < 0:  # NEC protocol sends repeat codes.
            pass
        else:
            print(decodeKeyValue(data))

    ir = NEC_8(pin_ir, callback)  # Instantiate receiver
    ir.error_function(print_error)  # Show debug information

    try:
        while True:
            pass
    except KeyboardInterrupt:
        ir.close()


初次时候的遥控器背面有个塑料片，需取下以通电
程序运行后，当你按下遥控器，Shell将打印出你按下的按键。

**How it works?**

这个程序看着略显复杂，但其实只需以下几行就实现了红外接收器的基本功能了。

.. code-block:: python

    import time
    from machine import Pin, freq
    from ir_rx.nec import NEC_8

    pin_ir = Pin(17, Pin.IN)

    # User callback
    def callback(data, addr, ctrl):
        if data < 0:  # NEC protocol sends repeat codes.
            pass
        else:
            print(decodeKeyValue(data))

    ir = NEC_8(pin_ir, callback)  # Instantiate receiver

这里会实例化一个 ``ir`` 对象，该对象会随时读取红外接收器获取到的信号。

并将结果记录到 callback 函数的 ``data`` 中。

* `Callback Function - Wikipedia <https://en.wikipedia.org/wiki/Callback_(computer_programming)>`_

如果IR接收器接收到重复值（如按着某个按键不松开），那么，data < 0，这些数据需要被过滤。

否则 data 将会是可以用的数值，但是却是一些难以言喻的编码， ``decodeKeyValue(data)`` 函数便是用于解码的。

.. code-block:: python

    def decodeKeyValue(data):
        if data == 0x16:
            return "0"
        if data == 0x0C:
            return "1"
        if data == 0x18:
            return "2"
        if data == 0x5E:
            return "3"
        if data == 0x08:
            return "4"
        if data == 0x1C:
            return "5"
        if data == 0x5A:
            return "6"
        if data == 0x42:
            return "7"
        if data == 0x52:
            return "8"
        if data == 0x4A:
            return "9"
        if data == 0x09:
            return "+"
        if data == 0x15:
            return "-"
        if data == 0x7:
            return "EQ"
        if data == 0x0D:
            return "U/SD"
        if data == 0x19:
            return "CYCLE"
        if data == 0x44:
            return "PLAY/PAUSE"
        if data == 0x43:
            return "FORWARD"
        if data == 0x40:
            return "BACKWARD"
        if data == 0x45:
            return "POWER"
        if data == 0x47:
            return "MUTE"
        if data == 0x46:
            return "MODE" 
        return "ERROR"

如果我们按下按键 **1** ，红外接收器输出的是 ``0x0C`` 这样的数值，需要解码后才能对应上具体的按键。

接下来是一些 debug 方面的功能。它们很重要，但是却与需要实现的效果无关，我们只管放在程序中即可。

.. code-block:: python

    from ir_rx.print_error import print_error

    ir.error_function(print_error)  # Show debug information

最后，我们用一个空循环作为主程序。并使用 try-except 来让程序退出时，终结 ``ir`` 对象。

.. code-block:: python

    try:
        while True:
            pass
    except KeyboardInterrupt:
        ir.close()



* `Try Statement - Python Docs <https://docs.python.org/3/reference/compound_stmts.html?#the-try-statement>`_