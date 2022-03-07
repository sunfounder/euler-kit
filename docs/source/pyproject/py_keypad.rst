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

.. code-block:: python

    import machine
    import time

    characters = [["1","2","3","A"],["4","5","6","B"],["7","8","9","C"],["*","0","#","D"]]

    pin = [2,3,4,5]
    row = []
    for i in range(4):
        row.append(None)
        row[i] = machine.Pin(pin[i], machine.Pin.OUT)

    pin = [6,7,8,9]
    col = []
    for i in range(4):
        col.append(None)
        col[i] = machine.Pin(pin[i], machine.Pin.IN)

    def readKey():
        key = []
        for i in range(4):
            row[i].high()
            for j in range(4):
                if(col[j].value() == 1):
                    key.append(characters[i][j])
            row[i].low()
        if key == [] :
            return None
        else:
            return key

    last_key = None
    while True:
        current_key = readKey()
        if current_key == last_key:
            continue
        last_key = current_key
        if current_key != None:
            print(current_key)
        time.sleep(0.1)

程序运行后，Shell会打印出你在Keypad上按下的按键。

**How it works**

.. code-block:: python

    import machine
    import time

    characters = [["1","2","3","A"],["4","5","6","B"],["7","8","9","C"],["*","0","#","D"]]

    pin = [2,3,4,5]
    row = []
    for i in range(4):
        row.append(None)
        row[i] = machine.Pin(pin[i], machine.Pin.OUT)

    pin = [6,7,8,9]
    col = []
    for i in range(4):
        col.append(None)
        col[i] = machine.Pin(pin[i], machine.Pin.IN)

Declare each key of the matrix keyboard to the array ``characters[]`` and define the pins on each row and column.

.. code-block:: python

    last_key = None
    while True:
        current_key = readKey()
        if current_key == last_key:
            continue
        last_key = current_key
        if current_key != None:
            print(current_key)
        time.sleep(0.1)

This is the part of the main function that reads and prints the button value.

The function ``readKey()`` will read the state of every button.

The statement ``if current_key != None`` and ``if current_key == last_key`` 
is used to judge whether a key is pressed and the state of the pressed button. 
(If you press \'3\' when you press \'1\', the judgement is tenable.)

Prints the value of the currently pressed key when the condition is tenable.

The statement ``last_key = current_key`` assigns the state of each judgment 
to an array ``last_key`` to facilitate the next round of conditional judgment.

.. code-block:: python

    def readKey():
        key = []
        for i in range(4):
            row[i].high()
            for j in range(4):
                if(col[j].value() == 1):
                    key.append(characters[i][j])
            row[i].low()
        if key == [] :
            return None
        else:
            return key

This function assigns a high level to each row in turn, and when the button in the column is pressed, 
the column in which the key is located gets a high level. 
After the two-layer loop is judged, the value of the button whose state is 1 is stored in the array ``key`` .

If you press the key \'3\':

|img_keypad_pressed|


row[0] is written in high level, and col[2] gets high level.

col[0]、col[1]、col[3] get low level.

There are four states:0, 0, 1, 0; and we write \'3\' into pressed_keys.

When row[1] , row[2] , row[3] are written into high level,
col[0] ~ col[4] get low level.

The loop stopped, there returns key = \'3\'.

If you press the buttons \'1\' and \'3\', there will return key = [\'1\',\'3\'].