#!/usr/bin/env python
# # coding=utf-8
#
from numbers import Number

a = None
b = None
_E9_A1_B9_E7_9B_AE = None


def text_prompt(msg):
    try:
        return raw_input(msg)
    except NameError:
        return input(msg)


print('请输入a和b两个数字：')
a = (a if isinstance(a, Number) else 0) + float(text_prompt('a : '))
b = (b if isinstance(b, Number) else 0) + float(text_prompt('b : '))
print('a+b=')
print(a + b)
