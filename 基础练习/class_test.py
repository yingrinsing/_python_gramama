#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""

# ===============================================================================
# 
# ===============================================================================


class Foo:
    # 【类属性】定义在 __init__ 外部的变量
    cls_attr = "我是类属性"

    def __init__(self):
        # 【实例属性】定义在__init__内部的带有self.的变量。没有self.是局部变量
        self.self_attr = "我是实例属性"

    @classmethod
    def cls_func(cls):
        print("我是类方法")
        print("在类方法内部调用类属性", cls.cls_attr)
        print("修改类方法")
        cls.cls_attr = "他是类属性"
        print("在类方法内部调用类属性", cls.cls_attr)

    def self_func(self):
        print("我是实例方法")
        print("在实例方法内部调用类属性", self.cls_attr)
        print("在实例方法内部调用实例属性", self.self_attr)


class Game:
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("查看帮助文档")

    @classmethod
    def show_top_score(cls):
        print("游戏最高分是%d" %cls.top_score)

    def start_game(self, score):
        print("%s开始玩游戏" % (self.player_name))
        Game.top_score = score if score > Game.top_score else score

    def get_list(self, *listA):
        listB = []
        for i in listA:
            print(i)
        # listA = [i*2 for i in listA]
        # return listB


if __name__ == '__main__':
    # foo1 = Foo()
    # foo2 = Foo()
    # # 通过类对象和实例对象的内存id可以说明每次实例化类对象，都会分配新的内存地址
    # print(id(Foo))
    # print(id(foo1))
    # print(id(foo2))
    # print("-" * 30)
    #
    # # 通过实例方法的内存id，能说明实例化会将实例属性和方法均复制一份保存到新的内存地址中
    # print(id(foo1.self_func))
    # print(id(foo2.self_func))
    # print("-" * 30)
    #
    # # 通过对比类对象和__class__属性的内存id，能说明实例对象的__class__指向的确实是实例对象的源类对象
    # print(id(Foo))
    # print(id(foo1.__class__))
    # print(id(foo2.__class__))
    #
    # print(id(Foo.cls_attr))
    # print(id(foo1.cls_attr))
    #
    # print("-" * 30)
    # foo1.cls_func()
    # print(foo2.cls_attr)
    # print(foo1.cls_attr)

    game1 = Game("张三")
    game1.start_game(92)
    game2 = Game("李四")
    game2.start_game(50)
    game3 = Game("王五")
    game3.start_game(100)
    Game.show_top_score()
    listA = [1,2,4,5]
    print(game1.get_list(listA))
    print(listA)