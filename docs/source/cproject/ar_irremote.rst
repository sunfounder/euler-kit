
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

The libraries ``IRsmallDecoder.h`` needs adding manually. 
Add Method: Refer to :ref:`apx_add_lib`.

:raw-code:


遥控器背面有个塑料片，需取下以通电。
程序运行后，当你按下遥控器，串口监视器将打印出你按下的按键。

**How it works?**

