# 网络分布式 第六次作业

[TOC]

## P31

由公式
$$
EstimatedRTT=(1-\alpha)\cdot EstimatedRTT + \alpha\cdot SampleRTT \\
DevRTT =(1-\beta)\cdot DevRTT+\beta\cdot \left|SampleRTT - EstimatedRTT\right| \\
TimeoutInterval=EstimatedRTT + 4 \cdot DevRTT
$$
可得
$$
SampleRTT = 106 \\
EstimatedRTT = ( 1 - 0.125 ) * 100 + 0.125 \cdot 106 = 100.75 ms \\
DevRTT = ( 1 -  0.25 ) \cdot 5 + 0.25 \cdot \left| 106 - 100.75 \right| = 5.25 ms \\
TimeoutInterval = 100.75 + 4 \cdot 5 = 121.75 ms \\
$$
$$
SampleRTT = 120 \\
EstimatedRTT = ( 1 - 0.125 ) * 100.75 + 0.125 \cdot 120 = 103.16 ms \\
DevRTT = ( 1 -  0.25 ) \cdot 5.25 + 0.25 \cdot \left| 120 - 103.16 \right| = 8.75 ms \\
TimeoutInterval = 103.16 + 4 \cdot 9 = 138.16 ms \\
$$
$$
SampleRTT = 140 \\
EstimatedRTT = ( 1 - 0.125 ) * 103.16 + 0.125 \cdot 140 = 107.76 ms \\
DevRTT = ( 1 -  0.25 ) \cdot 8.75 + 0.25 \cdot \left| 140 - 107.76 \right| = 15.77 ms \\
TimeoutInterval = 107.76 + 4 \cdot 16 = 170.86 ms \\
$$
$$
SampleRTT = 90 \\
EstimatedRTT = ( 1 - 0.125 ) * 107.76 + 0.125 \cdot 90 = 105.54 ms \\
DevRTT = ( 1 -  0.25 ) \cdot 15.77 + 0.25 \cdot \left| 90 - 105.54 \right| = 16.27 ms \\
TimeoutInterval = 105.54 + 4 \cdot 16 = 170.62 ms \\
$$
$$
SampleRTT = 115 \\
EstimatedRTT = ( 1 - 0.125 ) * 105.54 + 0.125 \cdot 115 = 106.72 ms \\
DevRTT = ( 1 -  0.25 ) \cdot 16.27 + 0.25 \cdot \left| 115 - 106.72 \right| = 14.57 ms \\
TimeoutInterval = 106.72 + 4 \cdot 15 = 164.99 ms \\
$$

## P32

### a.

$$
EstimatedRTT_4=0.1 \times SampleRTT_1 +(1-0.1)\times \left\{0.1\times SampleRTT_2+\\
(1-0.1)\times \left[0.1\times SampleRTT_3+(1-0.1)\times SampleRTT_4\right]\right\} \\
=0.1\times SampleRTT_1+0.9\times0.1SampleRTT_2+0.9^2\times0.1SampleRTT_3+0.9^3SampleRTT_4
$$

### b.

$$
EstimatedRTT^{(n)}=x\sum_{i=1}^{n-1}(1-x)^{i-1}SampleRTT_i+(1-x)^{n-1}SampleRTT_n
$$

### c.

$$
EstimatedRTT^{(\infty)}=\frac{x}{1-x}\sum_{i=1}^{n-1}(1-x)^{i}SampleRTT_i=\frac{1}{9}\sum_{i=1}^{\infty}\cdot9^iSampleRTT_i
$$

由式子可知，样本的权重呈指数形式锐减

## P40

### a.

[1,6]和[23,26]

### b.

[6,16]和[17,22]

### c.

三个冗余 ACK

### d.

超时

### e.

32

### f.

42/2 = 21

### g.

29/2=14

### h.

报文段1在第一个传输轮回中发送；报文段2-3在第2个传输轮回中发送；报文段4-7在第3传输轮回中发送；报文段8-15在第4个传输轮回中发送；报文段16-31在第5个传输轮回中发送；报文段32-63在第6个传输轮回中发送；报文段64-96在第7次传输轮回中发送。因此，在第7发送循环中发送第70个报文段。

### i.

ssthresh = 4，cwnd = ssthresh + 3 = 7

### j.

在第16个传输轮回中，ssthresh = cwnd/2 = 21，cwnd = 1

之后进入慢启动状态，因而在第19个传输轮回中，ssthreash = 21，cwnd = 4

### k.

第17个传输轮回：1个分组

第18个传输轮回：2个分组

第19个传输轮回：4个分组

第20个传输轮回：8个分组

第21个传输轮回：16个分组

第20个传输轮回：21个分组

总共1+2+4+8+16+21=52个分组