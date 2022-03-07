Electronic Circuit
==================


电力为您日常使用的许多东西提供动力，例如您家中的灯，以及您正在阅读本文的计算机。

使用电力需要您制作一个电路。电路是由金属导线和电气、电子部件组成的导电回路。

所有电路都需要从某个地方获取电力。
您家中的许多电器（例如电视、电灯）都通过墙上的插座供电，
这些插座连接到从发电厂向您的房屋供电的电线；
许多较小的便携式电路（例如电子玩具和手机）由存储电能的电池供电。
电池有两端，一个称为正极，并标有加号 (+)。
另一种称为负极，符号是减号（-），但这个符号通常不印在电池上。

为了使电流流动，需要有一条将电池的正极连接到负极的导电路径，这称为闭路。（如果断开，则称为开路。）
电流会流过灯等用电器，使它们工作（如亮起来）。

|bc1|


而在此套件中，Pico拥有一些电源输出引脚（正极），一些接地引脚（负极），
只要为Pico接入电源即可让这些引脚充当电源的正负极。

|bc2| 

使用电力可以为您制作具有光、声和运动的作品。
以LED为例，让LED的长引脚接到正极，短引脚接到负极，就可以点亮它了。
但是，如果你这么做，LED会非常快的坏掉，你需要在这个电路内加入一个220Ω电阻（注意看电阻上的标签）来保护它。

它们所构成的电路如下所示：

|bc2.5| 

这个时候你或许会产生疑问：我要怎么搭建这个电路呢？用手扶着导线，还是用胶带粘住引脚和导线呢？

这时候，无焊面包板毫无疑问会成为你最强大的伙伴。



Hello, Breadboard!
------------------


The breadboard is a rectangular plastic plate with a bunch of small holes in it. 
These holes allow us to easily insert electronic components and build electronic circuits. 
The breadboard does not permanently fix the electronic components, 
which makes it easy for us to repair the circuit and start over when we make a mistake.

.. note::
    We can use the breadboard without using special tools. But many electronic components are very small. A pair of tweezers can help us pick up small parts better.

There are many detailed breadboard knowledge on the Internet, let us use it wisely.

* `How to Use a Breadboard - Science Buddies <https://www.sciencebuddies.org/science-fair-projects/references/how-to-use-a-breadboard#pth-smd>`_

* `What is a BREADBOARD? - Makezine <https://cdn.makezine.com/uploads/2012/10/breadboardworkshop.pdf>`_


For breadboards, what you need to know clearly is:

#. Each group of half rows inside the breadboard (such as column A-E in row 1 or column F-J in row 3) is connected. This means that when an electrical signal flows in from A1, it can flow from B1, C1, D1, E1, but not from F1 or A2.

#. Both sides of the breadboard are usually used as power buses, and the holes in each column (about 50 holes) are connected. Generally speaking, the hole near the red wire is used to connect the positive power supply, and the hole near the blue wire is used to connect the negative power supply.

#. When building a circuit, the current flows from the positive pole and must first flow through the consumer before it can flow into the negative pole. Otherwise, a short circuit may occur.

现在，我们已经直到如何使用面包板了。让我们来尝试搭建简单电路吧！


|bc3| 


Let us follow the direction of the current to build the circuit!

1. Here we use the 3V3 pin of the Pico board to make the LED work, and the circuit starts from here. Connect it to the red power bus with a male-to-male (M2M) jumper wire.
#. The current needs to pass through a 220 ohm resistor (used to protect the LED). Insert one end (either end) of the resistor into the red power bus, and insert the other end into the free row of the breadboard (row 24 in my circuit).

    .. note::
        The color ring of the 220 ohm resistor is red, red, black, black and brown.

#. Pick up the LED, you will see that one of its leads is longer than the other. Insert the longer lead into the same row as the end of the resistor, and connect the shorter lead across the middle gap of the breadboard to the same row.
    
    .. note::
        The longer lead is known as the anode, and represents the positive side of the circuit; the shorter lead is the cathode, and represents the negative side. 

        The anode needs to be connected to the GPIO pin through a resistor; the cathode needs to be connected to the GND pin.

#. Insert the male-to-male (M2M) jumper wire into the same row as the LED short pin, and then connect it to the negative power bus of the breadboard.
#. Use a jumper to connect the negative power bus to the GND pin of Pico.


当心短路
--------


当两个不应连接的组件“意外”连接时，就可能会发生短路。
在这个套件中，电阻器，三极管，电容，LED 等器件的金属引脚很长；这些引脚可能会相互碰撞并导致短路。
根据电路的不同，有时短路只是阻止电路正常运行。
但是，有时短路会“烧毁”组件并造成永久性损坏，特别是电源和接地总线之间的短路，会导致电路变得非常热，烧毁元器件甚至熔化面包板上的塑料！

**因此，请始终确保面包板上，所有电子器件的引脚不会相互接触。**

电路的方向
------------


电路是有方向的，对于某些电子元件，方向很重要。
某些器件具有极性，这意味着它们具有必须正确连接的正极和负极。如果用错误的方向搭建电路将会使电路无法正常运行。

|bc3| 

在我们之前搭建的这个简单电路里，你可以尝试将LED反接，你会发现LED不再工作。

而对于一些器件，则是没有方向的，如这个电路中的电阻器，你可以尝试将其反接，并不会影响LED的正常工作。

如您在一些器件/模块中看到“+”、“-”、“GND”、“VCC”等标签或者拥有长短不一的引脚，它们大多需要顺着特定的方向接入电路。


电路的保护
--------------

通过物体（例如电线）的电流称为电流 (I)，它以安培 (A) 为单位。
电流流动背后的驱动力（电压）称为电压，以伏特 (V) 为单位。
限制电流流动的材料的特性称为电阻（R），电阻的单位是欧姆（Ω）。

电流、电压和电阻之间的关系用欧姆定律表示（前提是温度保持恒定）。
这表明在电路中流动的电流与施加的电压成正比，与电路的电阻成反比。即电流 (I) = 电压 (V) / 电阻 (R)。

* `Ohm's law - Wikipedia <https://en.wikipedia.org/wiki/Ohm%27s_law>`_

关于欧姆定律我们可以做一个简单的实验。

|bc3| 

在这个电路中，我们将连接3V3的导线换到5V（即VBUS，Pico的第40个引脚），你会发现LED较之前变得更亮。
将电阻从220Ω改为1000Ω（color ring: brown, black, black, brown and brown）,你会发现LED较之前变得更暗，更换为越大的电阻，LED会越暗。

.. note::
    电阻器的介绍和电阻值的计算方法请看 :ref:`cpn_res` 。

任何用电设备都会需要在规定的功率下使用，这意味着您在自建电路中需要注意电源电压和电阻器的运用。
一些封装好的模块通常只需要注意接入合适的电压即可（通常是3.3V或者5V），如超声波传感器等。
一些器件则需要添加合适的电阻器等设备来保护电路。
如LED可以使用的典型最大电流约为25mA，根据欧姆定律可以得知，如果我们使用5V电源，并且外接电阻小于200Ω，便会烧毁LED。





