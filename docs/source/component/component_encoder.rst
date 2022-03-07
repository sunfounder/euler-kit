.. _cpn_encoder:

Rotary Encoder 
======================

There are mainly two types of rotary encoders: absolute and incremental (relative) encoders. An incremental one is used in this kit.

Most rotary encoders have 5 pins with three functions of turning left & right and pressing down. Pin 1 and pin 2 are switch wiring terminals used to press. Pin 4 is generally connected to ground. Pin 3 and pin 5 are first connected to a pull-up resistor and then to VCC and they can generate two-phase square waves whose phase difference is 90°. Usually these waves are called channel A and channel B as shown below:

|img_encoder|

As shown on the right, when channel A changes from high level to low level, if channel B is high level, it indicates the rotary encoder spins clockwise (CW); if at that moment channel B is low level, it means spins counterclockwise (CCW). So if we read the value of channel B when channel A is low level, we can know in which direction the rotary encoder rotates.

|img_encoder_timing|