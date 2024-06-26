---
layout: post
title: 面向对象
date: 2021-06-01
tags: 设计模式
---
# 接口：

**接口是若干抽象方法的集合**。接口的作用：

1. 限制实现接口的类必须按照接口给定的调用方式实现这些方法；
2. 对高层模块隐藏了类的内部实现。
   具有抽象方法的类就是接口类。

# 面向对象设计原则：

###### 1. 开放封闭原则

一个软件实体如类、模块和函数应该对扩展开放，对修改关闭。即软件实体应该在不修改原代码的情况下进行修改。

###### 2. 里氏替换原则

所有引用父类的地方必须能透明地使用其子类地方必须能透明地使用其子类的对象

###### 3. 依赖倒置原则

高层模块不应该依赖底层模块，二者都应该依赖抽象。抽象不应该依赖细节，细节应该应该依赖抽象。**要针对接口编程，而不是针对实现编程**。

###### 4. 接口隔离原则

使用多个专门的接口，而不使用单一的总结口，高层的代码不应该依赖那些它不需要的接口。

###### 5. 单一职责原则

不要存在多于一个导致类变更的原因，一个类只负责一项职责，一个类只做一件事。**把面向过程的代码放到类中，虽然用到了类，但不是面向对象。**
