Custom Tone
==========================================


We have used active buzzer in the previous project, this time we will use passive buzzer.

Like the active buzzer, the passive buzzer also uses the phenomenon of electromagnetic induction to work. 
The difference is that a passive buzzer does not have oscillating source, so it will not beep if DC signals are used.
But this allows the passive buzzer to adjust its own oscillation frequency and can emit different notes such as "doh, re, mi, fa, sol, la, ti".

Let the passive buzzer emit a melody!

* :ref:`Buzzer`

**Wiring**

|img_buzzer|

Two buzzers are included in the kit, we use the one with exposed PCB behind.

The buzzer needs a transistor to work, and here we use S8050.

|sch_buzzer|

|wiring_buzzer|

1. Connect 3V3 and GND of Pico to the power bus of the breadboard.
#. Connect the positive pin of the buzzer to the positive power bus.
#. Connect the cathode pin of the buzzer to the **collector** lead of the transistor.
#. Connect the **base** lead of the transistor to the GP15 pin through a 1kΩ resistor.
#. Connect the **emitter** lead of the transistor to the negative power bus.


**Code**

.. :raw-code:


**How it works?**

If the passive buzzer given a digital signal, it can only keep pushing the diaphragm without producing sound.

Therefore, we use the ``tone()`` function to generate the PWM signal to make the passive buzzer sound.

This function has three parameters:

* **pin**, the GPIO pin that controls the buzzer.
* **frequency**, the pitch of the buzzer is determined by the frequency, the higher the frequency, the higher the pitch.
* **Duration**, the duration of the tone.


* `tone <https://www.arduino.cc/reference/en/language/functions/advanced-io/tone/>`_

**What more?**

We can simulate the specific tone according to the fundamental frequency of the piano, so as to play a complete piece of music.

* `Piano key frequencies - Wikipedia <https://en.wikipedia.org/wiki/Piano_key_frequencies>`_


.. :raw-code: