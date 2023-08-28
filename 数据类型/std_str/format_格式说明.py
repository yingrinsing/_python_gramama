#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016-7-6

@author: laok@laok.studio.com
@email:  1306743659@qq.com
@copyright: Apache License, Version 2.0
"""

#===============================================================================
# 通过{}和:来代替%
#===============================================================================
"""
类和类型可以定义一个__format__()方法来控制怎样格式化自己。它会接受一个格式化指示符作为参数：
def __format__(self, format_spec):...
"""
    #format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
    #fill        ::=  <any character>
    #align       ::=  "<" | ">" | "=" | "^"
    #sign        ::=  "+" | "-" | " "
    #width       ::=  integer
    #precision   ::=  integer
    #type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
        #'b' - 二进制。将数字以2为基数进行输出。
        #'c' - 字符。在打印之前将整数转换成对应的Unicode字符串。
        #'d' - 十进制整数。将数字以10为基数进行输出。
        #'o' - 八进制。将数字以8为基数进行输出。
        #'x' - 十六进制。将数字以16为基数进行输出，9以上的位数用小写字母。
        #'e' - 幂符号。用科学计数法打印数字。用'e'表示幂。
        #'g' - 一般格式。将数值以fixed-point格式输出。当数值特别大的时候，用幂形式打印。
        #'n' - 数字。当值为整数时和'd'相同，值为浮点数时和'g'相同。不同的是它会根据区域设置插入数字分隔符。
        #'%' - 百分数。将数值乘以100然后以fixed-point('f')格式打印，值后面会有一个百分号。
    #填充与对齐
        #^、<、>分别是居中、左对齐、右对齐，后面带宽度; =（只用于数字）在小数点后进行补齐
        #:号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充
    #精度与类型f
        #精度常跟类型f一起使用
    #进制
        #b、d、o、x分别是二进制、十进制、八进制、十六进制。
    #用，号还能用来做金额的千位分隔符

def align_lktest():
    print '{:>8}'.format('189')
    #'   189'
    print '{:0>8}'.format('189')
    #'00000189'
    print '{:a>8}'.format('189')
    #'aaaaa189'

def precision_lktest():
    print '{:.2f}'.format(321.33345)
    #'321.33'

def radix_lktest():
    print '{:b}'.format(17)
    #'10001'
    print '{:d}'.format(17)
    #'17'
    print '{:o}'.format(17)
    #'21'
    print '{:x}'.format(17)
    #'11'
def comma_lktest():    
    print '{:,}'.format(1234567890)
    #'1,234,567,890'

#通过位置
def by_place_lktest():
    print '{0},{1}'.format('kzc',18) 
    #'kzc,18'
    print '{},{}'.format('kzc',18) 
    #'kzc,18'
    print '{1},{0},{1}'.format('kzc',18) 
    #'18,kzc,18'

#通过关键字参数
def by_keyword_lktest():
    print '{name},{age}'.format(age=18,name='kzc') 
    #'kzc,18'

#通过对象属性
class Person: 
    def __init__(self,name,age): 
        self.name,self.age = name,age 
    def __str__(self): 
        return 'This guy is {self.name},is {self.age} old'.format(self=self)
  
def by_obj_attr_lktest():
    print Person('kzc',18)
    #'This guy is kzc,is 18 old'

#通过下标
def by_index_lktest():
    p=['kzc',18]
    print '{0[0]},{0[1]}'.format(p)
    #'kzc,18'


def fromat_place_lktest():
    #使用'{}'占位符
    print('I\'m {},{}'.format('Hongten','Welcome to my space!'))
    print('#' * 40)
    #也可以使用'{0}','{1}'形式的占位符
    print('{0},I\'m {1},my E-mail is {2}'.format('Hello','Hongten','hongtenzone@foxmail.com'))
    #可以改变占位符的位置
    print('{1},I\'m {0},my E-mail is {2}'.format('Hongten','Hello','hongtenzone@foxmail.com'))
    print('#' * 40)
    #使用'{name}'形式的占位符
    print('Hi,{name},{message}'.format(name = 'Tom',message = 'How old are you?'))
    print('#' * 40)
    #混合使用'{0}','{name}'形式
    print('{0},I\'m {1},{message}'.format('Hello','Hongten',message = 'This is a test message!'))
    print('#' * 40)
    
    #下面进行格式控制
    import math
    print('The value of PI is approximately {}.'.format(math.pi))
    print('The value of PI is approximately {!r}.'.format(math.pi))
    print('The value of PI is approximately {0:.3f}.'.format(math.pi))
    #字典访问1
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    for name, phone in table.items():
        print('{0:10} ==> {1:10d}'.format(name, phone))
    #字典访问2
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table))
    

def format_detail_lktest():
    print '1:\t|{0:>10},'.format('wangyu')
    print '2:\t|{0:4.2f}'.format(1.1415926)
    print '3:\t|',format(1.1415926,'<10.2f')
    print '4:\t|{0:<10},{1:<15}'.format('wangyu',1.1415926)
    print '5:\t|User ID: {uid} Last seen: {last_login}'.format(uid='root',last_login = '5 Mar 2008 07:20') 
    print '6:\t|{0:b}'.format(3)
    print '7:\t|{0:c}'.format(3)
    print '8:\t|{0:d}'.format(3)
    print '9:\t|{0:o}'.format(3)
    print '10:\t|{0:x}'.format(3)
    print '11:\t|{0:e}'.format(3.75)
    print '12:\t|{0:g}'.format(3.75)
    print '13:\t|{0:n}'.format(3.75) #浮点数
    print '14:\t|{0:n}'.format(3)    #整数
    print '15:\t|{0:%}'.format(3.75)
     
    #输入形式的控制format
    a = int(raw_input('a:'))
    b = int(raw_input('b:'))
    print '16:\t|%*.*f' % (a, b, 1.1415926)
     
    print '17:\t|{array[2]}'.format(array=range(10))
    print '18:\t|{attr.__class__}'.format(attr=0)
    print '19:\t|{digit:*^ 10.5f}'.format(digit=1.0/3)

#魔法参数
def format_magic_lktest():
    args=['lu','hi','e']
    kwargs = {'name1': 'Kevin', 'name2': 'Tom'}
    print 'hello {name1} {0} i am {name2} {1}{2}'.format(*args, **kwargs)

if __name__ == '__main__':
    #laok.lktest_run('')#catch_except = True
    #format_magic_lktest()
    format_detail_lktest()