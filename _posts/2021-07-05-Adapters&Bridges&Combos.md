---
layout: post
title: 设计模式-适配器&桥&组合
date: 2021-07-05
tags: 设计模式
---
# 适配器模式

适配器使得原本由于接口不兼容而不能一起工作的那些类可以一起工作，将一个类的接口转换成客户希望的另外一个接口。
实现适配器的两种方式：

- 类适配器——多继承；

```python
# 类适配器模式使用示例：
from abc import ABCMeta, abstractmethod

# 目标接口
class Payment(object, metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

class Alipay(Payment):
    def pay(self, money):
        print('支付了%d' % money)

# 待适配的类
class BankPay():
    def cost(self, money):
        print('银联支付了%d' % money)

# 类适配器
class PaymentAdapter(Payment, BankPay):
    """
    把不兼容cost转换成pay
    """

    def pay(self, money):
        self.cost(money)

p = PaymentAdapter()
p.pay(100)
"""
银联支付了100
"""
```

- 对象适配器——组合（组合就是一个类中放入另一类的对象）。

```python
class A:
	pass

class B:
	def __init__():
		self.a = A()
```

```python
# 类适配器模式使用示例：
from abc import ABCMeta, abstractmethod

# 目标接口
class Payment(object, metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

class Alipay(Payment):
    def pay(self, money):
        print('支付了%d' % money)

# 待适配的类
class BankPay():
    def cost(self, money):
        print('银联支付了%d' % money)

# 待适配的类
class ApplePay():
    def cost(self, money):
        print('苹果支付了%d' % money)

# 对象适配器
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)

p = PaymentAdapter(ApplePay())
p.pay(100)
p = PaymentAdapter(BankPay())
p.pay(100)
"""
苹果支付了100
银联支付了100
"""
```

适配器模式有三种角色：

1. 目标接口；
2. 待适配的类；
3. 适配器。
   适用场景是：
   想使用一个已存在的类，而它的接口不符合你的要求。想使用一些已经存在的类，但是不可能对每一个都进行子类化以匹配它们的接口。对象适配器可以适配它的父类接口。

# 桥

将一个事物的两个维度分离，使其都可以独立地变化。当事物有两个维度的表现，两个维度都可能扩展时使用。

```python
from abc import ABCMeta, abstractmethod

# 抽象
class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass

# 实现
class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass

# 细化抽象
class Rectangle(Shape):
    name = '长方形'

    def draw(self):
        self.color.paint(self)

# 细化实现
class Red(Color):
    def paint(self, shape):
        print('画红色的%s' % shape.name)

rectangle = Rectangle(Red())
rectangle.draw()
circle = Circle(Green())
circle.draw()
```

# 组合模式

将对象组合成树形结构以表示“部分-整体”的层次结构(特别是结构是递归的)，组合模式使得用户对单个对象和组合对象的使用具有一致性。
**优点：**

- 定义了包含基本对象和组合对象的层次结构；
- 简化客户端代码，客户端可以一致地使用组合对象和单个对象；
- 更加容易增加新类型的组件。

```python
from abc import ABCMeta, abstractmethod

# 抽象组件
class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass

# 叶子组件
class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '点(%s,%s)' % (self.x, self.y)

    def draw(self):
        print(self)

# 叶子组件
class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return '线段[(%s,%s)]' % (self.p1, self.p2)

    def draw(self):
        print(self)

# 复合组件
class Picture(Graphic):
    def __init__(self, iterable):
        self.children = []
        for g in iterable:
            self.add(g)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        for g in self.children:
            g.draw()

# 简单图形
print('------简单图形------')
p = Point(1, 2)
l1 = Line(Point(1, 2), Point(3, 4))
l2 = Line(Point(5, 6), Point(7, 8))
print(p)
print(l1)
print(l2)
print('------复合图形(p,l1,l2)------')
# 复合图形
pic = Picture([p, l1, l2])
pic.draw()
```
