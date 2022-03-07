Display the Level
=================


让我们来使用LED Bar Graph！ 这是一个常见的硬件显示器，可用来显示电量或者音量等级。它由一系列排成一排的LED组成。

|img_led_bar|

**Wiring**

|sch_ledbar|

|wiring_ledbar|

**Code**

.. code-block:: python

    import machine
    import utime

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

    while True:
        for i in range(10):
            led[i].toggle()
            utime.sleep(0.2)

When the program is running, you 会看到LED Bar Graph上的灯依次点亮，随后依次熄灭。

**How it works?**

LED Bar上的十个LED各自需要用一个引脚来控制，这也意味着我们定义这十个引脚。
如果我们为它们一一定义，这未免过于麻烦。因此，在这里我们使用list。

.. note::
    列表是Python中最基本的数据结构，用于在单个变量中存储多个项目，并使用方括号创建。

.. code-block:: python

    pin = [6,7,8,9,10,11,12,13,14,15]    

这行代码定义了一个列表 ``pin`` ，在它内部储存了 ``6,7,8,9,10,11,12,13,14,15`` 这十个元素。
列表会为内部的每一个元素设置一个引索。第一个引索是0，第二个是1，以此类推。
以这个列表为例子， ``pin[0]`` 为 ``6`` ， ``pin[4]`` 为 ``10`` 。

接下来声明一个空的列表 ``led`` ，它将用来定义十个LED对象。

.. code-block:: python

    led = []    

此时如果直接对该数组进行操作，如打印 ``led[0]`` 会无效，因为该列表的长度为0，而引索0所寻找的是第一个的项目，它并不存在。我们需要用为它添加新项目。

.. code-block:: python

    led.append(None)

这个 ``append()`` 方法可以在列表的末尾添加新项目，现在列表 ``led`` 拥有了它的第一个项目，长度为1， ``led[0]`` 也成为了有效元素，即便它目前的值为 ``None`` (代表空值)。

接下来我们将 ``led[0]`` ，定义为第一个LED对象，也就是6号引脚的所连接的LED。

.. code-block:: python

    led[0] = machine.Pin(6, machine.Pin.OUT)

这样，就完成了第一个LED对象的定义。

我们提前将那十个引脚号建立成一个列表 ``pin`` ，在这里我们可以用它来代入这行，这是为了使我们更容易进行批量操作。

.. code-block:: python

    led[0] = machine.Pin(pin[0], machine.Pin.OUT)

使用一个 ``for loop`` ，让10个引脚都按上面几个步骤执行一次，最终生成了下面的代码。

.. code-block:: python

    import machine

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

* :ref:`Lists`
* :ref:`For Loops`

再使用一个for loop，让LED Bar上的十个LED逐个切换状态。

.. code-block:: python

    for i in range(10):
        led[i].toggle()
        utime.sleep(0.2)

最后，将上面这一小段代码放入while loop，这样，代码就完成了。

.. code-block:: python

    import machine
    import utime

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

    while True:
        for i in range(10):
            led[i].toggle()
            utime.sleep(0.2)


