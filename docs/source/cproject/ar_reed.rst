Feel the Magnetism
==================

The most common type of reed switch contains a pair of magnetizable, flexible, metal reeds whose end portions are separated by a small gap when the switch is open. 

A magnetic field from an electromagnet or a permanent magnet will cause the reeds to attract each other, thus completing an electrical circuit.
The spring force of the reeds causes them to separate, and open the circuit, when the magnetic field ceases.

A common example of a reed switch application is to detect the opening of a door or windows, for a security alarm.

* :ref:`cpn_reed`



**Wiring**

|sch_reed|

|wiring_reed|

**Code**

When a magnet approaches, the circuit will be closed. Just like the button in the :ref:`ar_button` chapter.

.. :raw-code:

**What more?**

This time, we tried a flexible way of using switches: interrupt requests, or IRQs.:  interrupt requests, or IRQs.

For example, you are reading a book page by page, as if a program is executing a thread. At this time, someone came to you to ask a question and interrupted your reading. Then the person is executing the interrupt request: asking you to stop what you are doing, answer his questions, and then let you return to reading the book after the end.

The interrupt request also works in the same way, it allows certain operations to interrupt the main program. 

.. :raw-code:



这里定义了一个回调函数 ``detected()``，称为中断处理程序。它会在触发中断请求时执行。
然后，在 ``setup`` 设置一个中断请求，它包含两部分：mode和ISR。

在本程序中， ``mode`` 是 ``RISING``，表示管脚的值由低电平上升到高电平（即按下按钮）。

``ISR`` 是 ``detected`` ，我们定义的回调函数。

* `attachInterrupt() - Arduino Reference <https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/>`_