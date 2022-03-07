.. _cpn_stepper:

Stepper Motor
========================

There are two types of steppers, unipolars and bipolars, and it is very
important to know which type you are working with. In this experiment,
we will use a unipolar stepper.

The stepper motor is a four-phase one, which uses a unipolarity DC power
supply. As long as you electrify all phase windings of the motor by an
appropriate timing sequence, you can make it rotate step by step. The
schematic diagram of a four-phase reactive stepper motor:

|img_stepper| 


In the figure, in the middle of the motor is a rotor - a gear-shaped
permanent magnet. Around the rotor, 0 to 5 are teeth. Then more outside,
there are 8 magnetic poles, with each two opposite ones connected by
coil winding. So they form four pairs from A to D, which is called a
phase. It has four lead wires to be connected with switches SA, SB, SC,
and SD. Therefore, the four phases are in parallel in the circuit, and
the two magnetic poles in one phase are in series.

**Here's how a 4-phase stepper motor works:**

When switch SB is power on, switch SA, SC, and SD is power off, and
B-phase magnetic poles align with tooth 0 and 3 of the rotor. At the
same time, tooth 1 and 4 generate staggered teeth with C- and D-phase
poles. Tooth 2 and 5 generate staggered teeth with D- and A-phase poles.
When switch SC is power on, switch SB, SA, and SD is power off, the
rotor rotates under magnetic field of C-phase winding and that between
tooth 1 and 4. Then tooth 1 and 4 align with the magnetic poles of
C-phase winding. While tooth 0 and 3 generate staggered teeth with A-
and B-phase poles, and tooth 2 and 5 generate staggered teeth with the
magnetic poles of A- and D-phase poles. The similar situation goes on
and on. Energize the A, B, C and D phases in turn, and the rotor will
rotate in the order of A, B, C and D.

|img_stepper_timing|


The four-phase stepper motor has three operating modes: single
four-step, double four-step, and eight-step. The step angle for the
single four-step and double four-step are the same, but the driving
torque for the single four-step is smaller. The step angle of the
eight-step is half that of the single four-step and double four-step.
Thus, the eight-step operating mode can keep high driving torque and
improve control accuracy.

The stator of Stepper Motor we use has 32 magnetic poles, so a circle
needs 32 steps. The output shaft of the Stepper Motor is connected with
a reduction gear set, and the reduction ratio is 1/64. So the final
output shaft rotates a circle requiring a 32*64=2048 step.
