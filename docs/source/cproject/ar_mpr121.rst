Electrode Keyboard
====================

当您想在项目中添加大量触摸开关时，MPR121 是一个不错的选择。它的电极可以用导体进行延伸，
如果把电极连接到香蕉上，就可以把香蕉变成一个触摸开关。

* :ref:`cpn_mpr121`

**Wiring**


|sch_mpr121|


|wiring_mpr121|

**Code**

The libraries ``Adafruit_MPR121.h`` needs adding manually. 
Add Method: Refer to :ref:`apx_add_lib`.

:raw-code:

After the program runs, 你可以用手触碰MPR121上的十二个电极，这些电极的触摸状态将记录在 12 位布尔类型的数组中，该数组将打印在串行监视器上。
如果触摸第一个和第十一个电极，则打印 ``100000000010``。

你可以将电极延申，连接其他导体如水果、导线、金属箔等，这会使你有更多的方式来触发这些电极。

**How it works?**

初始化MPR121对象。此时该模块的电极们的状态会被记录为初始值。
如延长电极，需要重新运行示例来重置初始值。

.. code-block:: arduino

    #include "Adafruit_MPR121.h"

    Adafruit_MPR121 cap = Adafruit_MPR121();

    void setup() {
        Serial.begin(9600);
        int check = cap.begin(0x5A);
        if (!check) {
            Serial.println("MPR121 not found, check wiring?");
            while (1);
        }
        Serial.println("MPR121 found!");
    }

获取当前电极的值，它会获取一个12位的二进制的数值。如果触摸第一个和第十一个电极，则获取到 ``100000000010``。

.. code-block:: arduino

    // Get the currently touched pads
    currtouched = cap.touched();

判断电极状态是否发生变化。

.. code-block:: arduino

    void loop() {
        currtouched = cap.touched();
        if (currtouched != lasttouched) {}

        // reset our state
        lasttouched = currtouched;
    }

如果检测到电极状态改变，则将 ``currtouched`` 的数值按位逐一存入 ``touchStates[12]`` 数组中。最后将数组打印。

.. code-block:: arduino

    if (currtouched != lasttouched) {
        for (int i = 0; i < 12; i++) {
            if (currtouched & (1 << i)) touchStates[i] = 1;
            else touchStates[i] = 0;
        }
        for (int i = 0; i < 12; i++){
            Serial.print(touchStates[i]);
        }
        Serial.println();
    }