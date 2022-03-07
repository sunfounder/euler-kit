.. _cpn_uln2003:

ULN2003
=======


**ULN2003**

To apply the motor in the circuit, a driver board needs to be used. 
Stepper Motor Driver-ULN2003 is a 7-channel inverter circuit. That is, 
when the input pin is at high level, the output pin of ULN2003 is at low level, 
and vice versa. If we supply high level to IN1, and low level to IN2, IN3 and IN4, 
then the output end OUT1 is at low level, and all the other output ends are at high level.
 The internal structure of the chip is shown as below.

|img_uln2003_sche|


The stepper motor driver constituted by ULN2003 chip and 4 LEDs is shown
as follows. On the board, IN1,IN2,IN3 and IN4 work as input and the four
LEDs, A, B, C, D are the indicators of input pin. In addition,
OUT1,OUT2, OUT3 and OUT4 are connected to SA, SB, SC and SD on the
stepper motor driver. When the value of IN1 is set to a high level, A
lights up; switch SA is power on, and the stepper motor rotates one
step. The similar case repeats on and on. Therefore, just give the
stepper motor a specific timing sequence, it will rotate step by step.
The ULN2003 here is used to provide particular timing sequences for the
stepper motor.

|img_uln2003|