#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016-7-6

@author: laok@laok.studio.com
@email:  1306743659@qq.com
@copyright: Apache License, Version 2.0
"""
import laok
import sets  
#===============================================================================
# 
#===============================================================================
#格式符为真实值预留位置，并控制显示的格式。格式符可以包含有一个类型码，用以控制显示的类型，如下:
    #%s    字符串 (采用str()的显示)
    #%r    字符串 (采用repr()的显示)
    #%c    单个字符
    #%b    二进制整数
    #%d/%i/%u 十进制整数
    #%o        八进制整数
    #%x/%X    十六进制整数
    #%e/%E    指数 (基底写为e)/指数 (基底写为E)
    #%f/%F    浮点数
    #%g/%G    指数(e)或浮点数 (根据显示长度)/指数(E)或浮点数 (根据显示长度)
    #%%    字符"%"
#可以用如下的方式，对格式进行进一步的控制：
    #%[(name)][flags][width].[precision]typecode
    #(name)为命名
    #flags可以有+,-,' '或0。+表示右对齐。-表示左对齐。
        #' '为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐。0表示使用0填充。
    #width表示显示宽度
    #precision表示小数点后精度
    #'*'定义宽度或者小数点精度
    #'#'在八进制数前面显示零(0)，在十六进制前面显示“0x”或者“0X”（取决于用的是“x”还是“X”）
    #m.n  m 是显示的最小总宽度，n 是小数点后的位数（如果可用的话）


#Python用一个tuple将多个值传递给模板，每个值对应一个格式符。比如下面的例子：
def tuple_lktest():
    print("I'm %s. I'm %d year old" % ('Vamei', 99))


#我们还可以用词典来传递真实值。如下：
#可以看到，我们对两个格式符进行了命名。命名使用()括起来。每个命名对应词典的一个key。
def dict_lktest():
    print("I'm %(name)s. I'm %(age)d year old. \nagain=>I'm %(name)s. I'm %(age)d year old." % \
          {'name':'Vamei', 'age':99})


#上面的width, precision为两个整数。我们可以利用*，来动态代入这两个量。比如：
def star_lktest():
    print("%.*f" % (4, 1.2))
    #Python实际上用4来替换*。所以实际的模板为"%.4f"。
    print("%0*d" % (5, 1))
    #Python实际上用5来替换*。所以实际的模板为"%05d"。

def str_intersection():
    magic_char = sets.Set('abcde')  
    poppins_chars = sets.Set('bdxyz')  
    print ''.join(magic_char & poppins_chars)   #InterSection  
    print ''.join(magic_char | poppins_chars)   #Union  


if __name__ == '__main__':
    pass
