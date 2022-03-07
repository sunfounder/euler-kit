.. _cpn_irrecv:

Infrared-Receiver
=================

|img_irrecv|

An infrared-receiver is a component which receives infrared signals and can independently receive infrared ray and output signals compatible with TTL level. 
It’s similar with a normal plastic-packaged transistor in size and is suitable for all kinds of infrared remote control and infrared transmission.

IR Receiver is a component with photocell that is tuned to receive to infrared light. 
It is almost always used for remote control detection - every TV and DVD player has one of these in the front to receive for the IR signal from the clicker. 
Inside the remote control is a matching IR LED, which emits IR pulses to tell the TV to turn on, off or change channels.

IR 接收器会寻找以30 kHz到56 kHz脉动的红外光（在 980 纳米范围内）。
IR 遥控器以不同的开关模式为遥控器上的每个按钮发送 38 kHz 红外光的短脉冲。
当 IR 接收器检测到这些脉冲串时，它会向 Propeller I/O 引脚发送 0，如果没有，则发送 1。

红外接收器对来自其他光源（包括直射阳光）的干扰很敏感。一些荧光灯具也可以发出 38 kHz 的红外光。

