---
layout: post
title: 设计模式-建造者&单例模式
date: 2021-07-02
tags: 设计模式
---
# 建造者模式

建造者模式是将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。
**角色：**

- 抽象创建者；
- 具体创建者；
- 指挥者；
- 产品。
  抽象工厂模式 - 着重于多个系列的产品对象；
  建造者模式     -着重分步构造一个复杂对象(控制顺序)。

```python
class Burger():

    """

    主食类，价格名字

    """

    name=""

    price=0.0

    def getPrice(self):

        return self.price

    def setPrice(self,price):

        self.price=price

    def getName(self):

        return self.name

class cheeseBurger(Burger):

    """

    奶酪汉堡

    """

    def __init__(self):

        self.name="cheese burger"

        self.price=10.0

class spicyChickenBurger(Burger):

    """

    香辣鸡汉堡

    """

    def __init__(self):

        self.name="spicy chicken burger"

        self.price=15.0class Burger():

    """

    主食类，价格名字

    """

    name=""

    price=0.0

    def getPrice(self):

        return self.price

    def setPrice(self,price):

        self.price=price

    def getName(self):

        return self.name

class cheeseBurger(Burger):

    """

    奶酪汉堡

    """

    def __init__(self):

        self.name="cheese burger"

        self.price=10.0

class spicyChickenBurger(Burger):

    """

    香辣鸡汉堡

    """

    def __init__(self):

        self.name="spicy chicken burger"

        self.price=15.0

# 其它食品类别

class order():

    """

    订单对象，一个订单中包含一份主食，一份小食，一份饮料

    """

    burger=""

    snack=""

    beverage=""

    def __init__(self,orderBuilder):

        self.burger=orderBuilder.bBurger

        self.snack=orderBuilder.bSnack

        self.beverage=orderBuilder.bBeverage

    def show(self):

        print("Burger:%s"%self.burger.getName())

        print("Snack:%s"%self.snack.getName())

        print("Beverage:%s"%self.beverage.getName())

  

# 建造者

class orderBuilder():

    """

    orderBuilder就是建造者模式中所谓的“建造者”，

    将订单的建造与表示相分离，以达到解耦的目的。

    在上面订单的构建过程中，如果将order直接通过参数定义好（其构建与表示没有分离），

    同时在多处进行订单生成，此时需要修改订单内容，

    则需要一处处去修改，业务风险也就提高了不少。

    """

    bBurger=""

    bSnack=""

    bBeverage=""

    def addBurger(self,xBurger):

        self.bBurger=xBurger

    def addSnack(self,xSnack):

        self.bSnack=xSnack

    def addBeverage(self,xBeverage):

        self.bBeverage=xBeverage

    def build(self):

        return order(self)

  

# Director类

class orderDirector():

    """

    在建造者模式中，还可以加一个Director类，用以安排已有模块的构造步骤。

    对于在建造者中有比较严格的顺序要求时，该类会有比较大的用处。

    """

    order_builder=""

    def __init__(self,order_builder):

        self.order_builder=order_builder

    def createOrder(self,burger,snack,beverage):

        self.order_builder.addBurger(burger)

        self.order_builder.addSnack(snack)

        self.order_builder.addBeverage(beverage)

        return self.order_builder.build()
```

# 单例模式

单例模式保证一个类只有一个实例，并提供一个访问它的全局访问点。
**优点：**

- 对唯一实例的受控访问（只有一个实例），单例相当于全局变量，但防止了命名空间被污染（变量命名不会有冲突）。

```python
class Singleton(object):

    __instance = None

  

    def __new__(cls, age, name):

        #如果类数字__instance没有或者没有赋值

        #那么就创建一个对象，并且赋值为这个对象的引用，保证下次调用这个方法时

        #能够知道之前已经创建过对象了，这样就保证了只有1个对象

        if not cls.__instance:

            cls.__instance = object.__new__(cls)

            # cls._instance = super().__new__(cls, *args, **kwargs) #也是常见的写法
           # 如果一个类没有明确指定父类，那么它会默认继承自 Python 中的基础类 `object`。因此，即使你没有显式地指定父类，Python 也会隐式地将其视为继承自 `object` 类。

        return cls.__instance

    def __init__(self,age,name):

        self.age = age

        self.name = name

a = Singleton(18, "wk")

b = Singleton(8, "mm")

  

print(id(a)==id(b))

print(a.age,a.name)

print(b.age,b.name)

a.size = 19 #给a指向的对象添加一个属性

print(b.size)#获取b指向的对象的age属性
```

总结下__init__()和__new__()的区别：

1. __init__()通常用于初始化一个新实例，控制这个初始化的过程，比如添加一些属性，做一些额外的操作，发生在类实例被创建完以后。它是实例级别的方法。
2. __new__()通常用于控制生成一个新实例的过程。它是类级别的方法。
3. __new__()至少有一个参数cls，代表要实例化的类，此参数在实例化时会有python编辑器自动提供。
4. __new__()必须有返回值，返回实例化出来的实例。
5. 如果将类比作制造商，__new__()方法发就是前期的原材料环节，__init__()方法就是在有了原材料的基础上，加工，初始化商品的环节。
