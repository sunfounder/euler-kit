.. _cpn_diode:

Diode
=================


Diode是一种具有两个电极的电子元器件。它只允许电流由单一方向流过，这通常称之为“Rectifying”功能。
因此，二极管可以想成电子版的逆止阀。


The two terminals of a diode are polarized, with the positive end called anode and the negative end called cathode. 
The cathode is usually made of silver or has a color band. 
Controlling the direction of current flow is one of the key features of diodes — the current in a diode flows from anode to cathode. The behavior of a diode is similar to the behavior of a check valve. One of the most important characteristics of a diode is the non-linear current voltage. If higher voltage is connected to the anode, then current flows from anode to cathode, and the process is known as forward bias. However, if the higher voltage is connected to the cathode, then the diode does not conduct electricity, and the process is called reverse bias.

由于二极管具有单向导电的特性，几乎所有复杂一些的电子电路中都会使用到它。它是诞生最早的半导体器件之一，其应用也非常广泛。

然而实际上二极管并不会表现出如此完美的开与关的方向性，而是较为复杂的非线性电子特征——这是由特定类型的二极管技术决定的。

晶体二极管是一个由p型半导体和n型半导体形成的p-n结，在其界面处两侧形成了空间电荷层，并且建有自建电场，当不存在外加电压时，因为p-n结两边载流子浓度差引起的扩散电流和自建电场引起的漂移电流相等而处于电平衡状态。 当产生正向电压偏置时，外界电场与自建电场的互相抑消作用使载流子的扩散电流增加引起了正向电流（也就是导电的原因）。 当产生反向电压偏置时，外界电场与自建电场进一步加强，形成在一定反向电压范围中与反向偏置电压值无关的反向饱和电流I0（这也就是不导电的原因）。
当外加的反向电压高到一定程度时，p-n结空间电荷层中的电场强度达到临界值产生载流子的倍增过程，产生大量电子空穴对，产生了数值很大的反向击穿电流，称为二极管的击穿现象。

1、正向性
外加正向电压时，在正向特性的起始部分，正向电压很小，不足以克服p-n结内电场的阻挡作用，正向电流几乎为零，这一段称为死区。
这个不能使二极管导通的正向电压称为死区电压。当正向电压大于死区电压以后，p-n结内电场被克服，二极管正向导通，电流随电压增大而迅速上升。
在正常使用的电流范围内，导通时二极管的端电压几乎维持不变，这个电压称为二极管的正向电压。

2、反向性
外加反向电压，且不超过一定范围时，通过二极管的电流是少数载流子漂移运动所形成反向电流。
由于反向电流很小，二极管处于截止状态。这个反向电流又称为反向饱和电流或漏电流，二极管的反向饱和电流受温度影响很大。

3、击穿
外加反向电压超过某一数值时，反向电流会突然增大，这种现象称为电击穿。
引起电击穿的临界电压称为二极管反向击穿电压。电击穿时二极管失去单向导电性。
因而使用时应避免二极管外加的反向电压过高。

早期的二极管包含 "Cat's Whisker" Crystals 以及 Vacuum tubes (also called "Thermionic Valves")。现今最普遍的二极管大多是使用半导体材料如硅或锗。

* `P–N junction - Wikipedia <https://en.wikipedia.org/wiki/P-n_junction>`_
 
* `Diode - Wikipedia <https://en.wikipedia.org/wiki/Diode>`_


