---
layout: post
title: 树莓派GPIO
date: 2023-9-01
tags: 机器人
---

0.1 树莓派GPIO编号方式
功能物理引脚
从左到右，从上到下：左边奇数，右边偶数：1-40

![alt text](/images/asdafag.png)

BCM
编号侧重CPU寄存器，根据BCM2835的GPIO寄存器编号。

wiringPi
编号侧重实现逻辑，把扩展GPIO端口从0开始编号，这种编号方便编程。如图 WiringPi一栏。

![alt text](/images/zxcasdfasd.png)

操作GPIO时一定先要清楚使用那一套编号。

1. 准备
1.1 硬件
树莓派（我测试了Pi 3B+和Pi Zero W）
LED（3mm或5mm）
1KΩ电阻
杜邦线
电脑（我用Windows 7）
1.2 GPIO接口

![alt text](/images/sasdqwe.png)

1.3 接线
首先我们把LED和树莓派连接。LED的正极串联一个1KΩ电阻接树莓派的GPIO18(pin12)，负极接地。


这个图是用Fritzing画的。

2. 测试
2.1 连接电脑和Pi Zero W
用putty连接电脑和Pi Zero W，看本文最后的参考文档。Host Name填raspberrypi.local，端口22，用户名pi，密码raspberry。

注意：boot分区有一个名为ssh的空文本文件，这个ssh文件容易丢失，如果ssh不能登录了，先检查ssh是否丢失。

2.2 用Shell命令直接控制GPIO
使GPIO18从内核空间暴露到用户空间中

```pi@raspberrypi:~ $ sudo echo 18 > /sys/class/gpio/export```

> 是IO重定向符号，IO重定向是指改变linux标准输入和输出的默认设备，指向一个用户定义的设备。echo 18 > 
> export就是把18写入到export文件中。

执行该操作之后，/sys/class/gpio目录下会增加一个gpio18文件夹。

查看GPIO18引脚（在Liunx中设备都以文件的形式，引脚也是设备）
```pi@raspberrypi:~ $ cd /sys/class/gpio/gpio18```

```pi@raspberrypi:/sys/class/gpio/gpio18 $ ls```


设置GPIO18为输出模式
```pi@raspberrypi:/sys/class/gpio/gpio18 $ sudo echo out > direction```

向value文件中输入1，GPIO输出高电平，LED点亮
```pi@raspberrypi:/sys/class/gpio/gpio18 $ sudo echo 1 > value```

向value文件中输入0，GPIO输出低电平，LED熄灭
```pi@raspberrypi:/sys/class/gpio/gpio18 $ sudo echo 0 > value```

返回家目录
```pi@raspberrypi:/sys/class/gpio $ cd ~```

注销GPIO18接口
```pi@raspberrypi:~ $ sudo echo 18 > /sys/class/gpio/unexport```

2.3 用Shell脚本控制GPIO
新建一个名为ledonoff.sh的脚本。
```pi@raspberrypi:~ $ sudo nano ledonoff.sh```

脚本写下面的内容：
```
echo $1 > /sys/class/gpio/export

echo out > /sys/class/gpio/gpio$1/direction

echo 1 > /sys/class/gpio/gpio$1/value

sleep 5 #延时5秒

echo 0 > /sys/class/gpio/gpio$1/value

echo $1 > /sys/class/gpio/unexport
```
说明：shell脚本可传入参数，例如$1代表第1个参数，$2代表第2个参数，以此类推。

为ledonoff.sh添加可执行权限
pi@raspberrypi:~ $ sudo chmod +x ledonoff.sh

运行脚本
pi@raspberrypi:~ $ sudo ./ledonoff.sh 18

运行结果：LED点亮，持续5秒钟关闭。

2.4 用Python通过PRI.GPIO命令控制GPIO
用Python控制GPIO，最便捷的方法就是使用python类库，比如树莓派系统本身集成的RPi.GPIO。


导入python类库RPi.GPIO，命名为别名为GPIO
```>>> import RPi.GPIO as GPIO```

引入之后，就可以使用 GPIO 模块的函数了。

设置BOARD编码方式，基于BCM
树莓派3 GPIO分为如下的三种编码方式：物理引脚BOARD编码，BCM编码，以及 wiringPi 编码。

```>>> GPIO.setmode(GPIO.BCM)```

输出模式
```>>> GPIO.setup(18,GPIO.OUT)```

GPIO17输出高电平，LED点亮
```>>> GPIO.output(18,GPIO.HIGH)```

GPIO17输出低电平，LED熄灭
```>>> GPIO.output(18,GPIO.LOW)```

用完后进行清理
```>>> GPIO.cleanup()```

退出python交互界面
```>>> Ctrl+D```

2.5 用Python脚本控制GPIO
新建一个名为blinky.py的脚本。
```pi@raspberrypi:~ $ sudo nano blinky.py```

脚本写下面的内容：
```
import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.OUT)

while True:

GPIO.output(18,GPIO.HIGH)

time.sleep(1)

GPIO.output(18,GPIO.LOW)

time.sleep(1)



GPIO.cleanup()
```
说明：while True下面的循环体要缩进，用空格或Tab（但不能混用）键缩进就行。

为blinky.py添加可执行权限
```pi@raspberrypi:~ $ sudo chmod +x blinky.py```

运行Python脚本
```pi@raspberrypi:~ $ sudo python blinky.py```

LED闪烁。

停止运行
用 Ctrl+C 来中断循环。

1. 借助wiringPi GPIO用C语言控制GPIO
树莓派内核中已经编译自带了gpio的驱动，我们常通过一些第三方写好的库函数来完成具体的操作，比较常见的操作库函数有：

Python GPIO
Python GPIO已经集成到了树莓派内核，为树莓派官方资料中推荐且容易上手。python GPIO是一个小型的python库，可以帮助用户完成raspberry相关IO口操作，但是python GPIO库还没有支持SPI、I2C或者1-wire等总线接口。

常见C语言库有：

wiringPi (http://wiringpi.com/)
wiringPi适合那些具有C语言基础，在接触树莓派之前已经接触过单片机或者嵌入式开发的人群。wiringPi的API函数和arduino非常相似，这也使得它广受欢迎。作者给出了大量的说明和示例代码，这些示例代码也包括UART设备，I2C设备和SPI设备等。

BCM2835 C Library (http://www.airspayce.com/mikem/bcm2835/)
BCM2835 C Library可以理解为使用C语言实现的相关底层驱动，BCM2835 C Library的驱动库包括GPIO. SPI和UART等，可以通过学习BCM2835 C Library熟悉BCM2835相关的寄存器操作。如果有机会开发树莓派上的linux驱动，或自主开发python或PHP扩展驱动，可以从BCM2835 C Library找到不少的“灵感”。

3.1 WiringPi GPIO安装
WiringPi是应用于树莓派平台的GPIO控制库函数，WiringPi遵守GUN Lv3。wiringPi使用C或者C++开发并且可以被其他语言包转，例如python、ruby或者PHP等。

wiringPi包括一套gpio控制命令，使用gpio命令可以控制树莓派GPIO管脚。用户可以利用gpio命令通过shell脚本控制或查询GPIO管脚。

wiringPi安装
更新列表：

```pi@raspberrypi:~ $ sudo apt-get update```

更新软件：

```pi@raspberrypi:~ $ sudo apt-get upgrade```

安装：

```pi@raspberrypi:~ $ sudo apt-get install wiringpi```

测试
wiringPi包括一套gpio命令，使用gpio命令可以控制树莓派上的各种接口，通过以下指令可以测试wiringPi是否安装成功。

```pi@raspberrypi:~ $ gpio -v```


查看GPIO图
```pi@raspberrypi:~ $ gpio readall```


3.2 编写代码
新建一个名为led_blink.c的源程序
```pi@raspberrypi:~ $ sudo nano led_blink.c```

内容如下
```
#include <wiringPi.h>

int main(void) {

wiringPiSetup();

pinMode (1, OUTPUT);

for(;;) {

digitalWrite(1, HIGH);delay (500);

digitalWrite(1, LOW);delay (500) ;

}

}
```

说明：看看上一小节的图，BCM编号的GPIO17引脚在wiringPi编号中是1。

3.3 编译运行
编译
```pi@raspberrypi:~ $ gcc led_blink.c -o led_blink -l wiringPi```

-l wiringPi表示动态加载wiringPi共享库。

运行
```pi@raspberrypi:~ $ sudo ./led_blink```

用 Ctrl+C 来中断循环。

4. 借助BCM2835 C Library用C语言控制GPIO
4.1 下载安装
先看看最新版本：http://www.airspayce.com/mikem/bcm2835


下载bcm2835-1.56.tar.gz
```pi@raspberrypi:~ $ wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.56.tar.gz```

解压缩
```pi@raspberrypi:~ $ tar xvzf bcm2835-1.56.tar.gz```

配置编译
进入压缩之后的目录:

```pi@raspberrypi:~ $ cd bcm2835-1.56```

执行配置命令：

```
pi@raspberrypi:~/bcm2835-1.56 $ ./configure

pi@raspberrypi:~/bcm2835-1.56 $ make
```

执行检查
```pi@raspberrypi:~/bcm2835-1.56 $ sudo make check```

安装bcm2835库:
```pi@raspberrypi:~/bcm2835-1.56 $ sudo make install```

4.2 编写代码
新建一个名为blink_led.c的源程序

```
pi@raspberrypi:~/bcm2835-1.56 $ cd ~

pi@raspberrypi:~ $ sudo nano blink_led.c
```
内容如下
```
#include <bcm2835.h>

#define PIN RPI_GPIO_P1_12

int main(int argc, char **argv) {

if (!bcm2835_init())

return 1;



bcm2835_gpio_fsel(PIN, BCM2835_GPIO_FSEL_OUTP);



while (1) {

bcm2835_gpio_write(PIN, HIGH);

bcm2835_delay(500);

bcm2835_gpio_write(PIN, LOW);

bcm2835_delay(500);

}

bcm2835_close();

return 0;

}
```
说明：GPIO的编号方式不同，采用PCB板的物理接口编号，led连在树莓派Zero W板子的12引脚上。

4.3 编译运行
编译
```pi@raspberrypi:~ $ gcc blink_led.c -o blink_led -l bcm2835```

-l bcm2835表示动态加载bcm2835共享库

运行
```sudo ./blink_led```

用 Ctrl+C 来中断循环。