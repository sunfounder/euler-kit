4x4 Keypad
========================

Keypad是块或与数字，符号，或字母的布置设置的按钮垫。
键盘可以在主要需要数字输入的设备上找到，
例如计算器、电视遥控器、按钮电话、自动售货机、自动取款机、
销售点设备、 密码锁和数字门锁。
许多设备的排列都遵循E.161标准。


* :ref:`cpn_keypad`
* `E.161 - Wikipedia <https://en.wikipedia.org/wiki/E.161>`_


**Wiring**

|sch_keypad|

|wiring_keypad|

**Code**

The libraries ``Keypad.h`` needs adding manually. 
Add Method: Refer to :ref:`apx_add_lib`.

:raw-code:

程序运行后，串口监视器会打印出你在Keypad上按下的按键。

**How it works**

By calling the ``Keypad.h`` library, you can easily use Keypad.

.. code-block:: arduino

    #include <Keypad.h> 

Library Functions：

.. code-block:: arduino

    Keypad(char *userKeymap, byte *row, byte *col, byte numRows, byte numCols)

Initializes the internal keymap to be equal to ``userKeymap``.

``userKeymap``: The symbols on the buttons of the keypads.

``row``, ``col``: Pin configuration.

``numRows``, ``numCols``: Keypad sizes.

.. code-block:: arduino

    char getKey()

Returns the key that is pressed, if any. This function is non-blocking.