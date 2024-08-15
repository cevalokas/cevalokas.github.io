---
layout: post
title: 设计模式-行为型模式
date: 2021-8-11
tags: 设计模式
---
# 责任链模式：

使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。将这些对象连成一条链并沿着这条链传递该请求，直到有一个对象处理它为止。
**角色：

- 抽象处理者；
- 具体处理者；
- 客户端。
  使用场景：有多个对象可以处理一个请求，哪个对象处理由运行时决定；在不明确接收者的情况下，向多个对象中的一个提交一个请求。
  **优点
- 降低耦合度，一个对象无需知道是其它哪一个对象处理其请求。

```python
# 抽象的处理者
class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass

# 具体的处理者
class GeneralManager(Handler):
    def handle_leave(self, day):
        if day <= 30:
            print('总经理准假%d' % day)
        else:
            print('可以辞职了！')

# 具体的处理者
class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day <= 7:
            print('项目主管准假%d' % day)
        else:
            print('部门经理职权不足')
            self.next.handle_leave(day)

# 具体的处理者
class ProjectDirector(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 3:
            print('项目主管准假%d' % day)
        else:
            print('项目主管职权不足')
            self.next.handle_leave(day)
```

# 观察者模式

被称为“发布-订阅”模式。
它用来定义对象间一种一对多的依赖关系，当一个对象的状态发生变化时，所有依赖它的对象都得到通知并被自动更新。
**角色：

- 抽象主题；
- 具体主题（发布者）；
- 抽象观察者；
- 具体观察者（订阅者）。
  使用场景：当一个抽象模型有两个方面，其中一个方面依赖另一个方面。将这两者封装在独立对象中以使它们可以各自独立地改变和复用；当对一个对象的改变需要同时改变其它对象，而不知道具体有多少对象待改变；当一个对象必须通知其它对象，而它又不能假定其它对象是谁。
  **优点：
- 目标和观察者之间的抽象耦合最小；
- 支持广播通信。

```python
class AlarmSensor:

    def run(self):

        print("Alarm Ring...")

class WaterSprinker:

    def run(self):

        print("Spray Water...")

class EmergencyDialer:

    def run(self):

        print("Dial 119...")


  

class Observer:

    def update(self):

        pass

class AlarmSensor(Observer):

    def update(self,action):

        print("Alarm Got: %s" % action)

        self.runAlarm()

    def runAlarm(self):

        print("Alarm Ring...")

class WaterSprinker(Observer):

    def update(self,action):

        print("Sprinker Got: %s" % action)

        self.runSprinker()

    def runSprinker(self):

        print("Spray Water...")

class EmergencyDialer(Observer):

    def update(self,action):

        print("Dialer Got: %s"%action)

        self.runDialer()

    def runDialer(self):

        print("Dial 119...")

  

"""

观察者中定义了update接口，如果被观察者状态比较多，或者每个具体的观察者方法比较多，可以通过update传参数进行更丰富的控制。

下面构造被观察者。

"""

  

class Observed:

    observers=[]

    action=""

    def addObserver(self,observer):

        self.observers.append(observer)

    def notifyAll(self):

        for obs in self.observers:

            obs.update(self.action)

class smokeSensor(Observed):

    def setAction(self,action):

        self.action=action

    def isFire(self):

        return True

  

"""

被观察者中首先将观察对象加入到观察者数组中，若发生情况，则通过notifyAll通知各观察者。

业务代码如下：

"""

  

if __name__=="__main__":

    alarm=AlarmSensor()

    sprinker=WaterSprinker()

    dialer=EmergencyDialer()

  

    smoke_sensor=smokeSensor()

    smoke_sensor.addObserver(alarm)

    smoke_sensor.addObserver(sprinker)

    smoke_sensor.addObserver(dialer)

  

    if smoke_sensor.isFire():

        smoke_sensor.setAction("On Fire!")

        smoke_sensor.notifyAll()
```

# 策略模式

定义一个个算法，把它们封装起来，并且使它们可以相互替换。
使得算法可独立于使用它的客户而变化。
**角色：

- 抽象策略；
- 具体策略；
- 上下文。
  **优点：
- 定义了一些列可重用的算法和行为；
- 消除了一些条件语句；\
- 可以提供相同行为的不同实现；
  **缺点：
- 客户必须了解不同的策略。

# 模板方法模式

定义一个操作中的算法骨架，将一些步骤延迟到子类中。
模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。
**角色：

- 抽象类（定义抽象类（钩子操作），实现一个模板方法作为算法的骨架）；
- 具体类。（实现原子操作）。
  适用的场景：一次性实现一个算法的不变部分，各个子类中的公共行为应该被提取出来并集中到一个公共父类中以避免代码重复；控制子类扩展。

```python
class StockQueryDevice():

    stock_code="0"

    stock_price=0.0

    def login(self,usr,pwd):

        pass

    def setCode(self,code):

        self.stock_code=code

    def queryPrice(self):

        pass

    def showPrice(self):

        pass
        

    def operateQuery(self, usr, pwd, code):

        if not self.login(usr, pwd):

            return False

        self.setCode(code)

        self.queryPrice()

        self.showPrice()

        return True

  

class WebAStockQueryDevice(StockQueryDevice):

    def login(self,usr,pwd):

        if usr=="myStockA" and pwd=="myPwdA":

            print("Web A:Login OK... user:%s pwd:%s"%(usr,pwd))

            return True

        else:

            print("Web A:Login ERROR... user:%s pwd:%s"%(usr,pwd))

            return False

    def queryPrice(self):

        print("Web A Querying...code:%s "%self.stock_code)

        self.stock_price=20.00

    def showPrice(self):

        print("Web A Stock Price...code:%s price:%s"%(self.stock_code,self.stock_price))

class WebBStockQueryDevice(StockQueryDevice):

    def login(self,usr,pwd):

        if usr=="myStockB" and pwd=="myPwdB":

            print("Web B:Login OK... user:%s pwd:%s"%(usr,pwd))

            return True

        else:

            print("Web B:Login ERROR... user:%s pwd:%s"%(usr,pwd))

            return False

    def queryPrice(self):

        print("Web B Querying...code:%s "%self.stock_code)

        self.stock_price=30.00

    def showPrice(self):

        print("Web B Stock Price...code:%s price:%s"%(self.stock_code,self.stock_price))



if  __name__=="__main__":

    web_a_query_dev=WebAStockQueryDevice()

    web_a_query_dev.operateQuery("myStockA","myPwdA","12345")

```
