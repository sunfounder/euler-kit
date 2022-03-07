.. _cpn_touch:

Touch Switch
==================================

Touch switch module works by detecting a change in capacitance due to influence of an external object. The touch plate is covered with insulating material, and the user does not come in contact with the electrical circuit.

A capacitive touch switch has different layers—top insulating face plate followed by touch plate, another insulating layer and then ground plate.

|img_touch|

In practice, a capacitive sensor can be made on a double-sided PCB by regarding one side as the touch sensor and the opposite side as ground plate of the capacitor. When power is applied across these plates, the two plates get charged. In equilibrium state, the plates have the same voltage as the power source.

The touch detector circuit has an oscillator whose frequency is dependent on capacitance of the touchpad. When a finger is moved close to the touchpad, additional capacitance causes frequency of this internal oscillator to change. The detector circuit tracks oscillator frequency at timed intervals, and when the shift crosses the threshold change, the circuit triggers a key-press event.

|img_touch_sche|
