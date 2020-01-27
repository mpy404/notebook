# !/usr/bin/python3
# -*- coding: utf-8 -*-

# 导入模块
import module

module.print_dicts("m", "py", a="a", b="b")

# 从模块中导入某个函数
from module import print_dicts, print_list

a = [1, 2, 3, 4, 5]
print_list(a)

# 使用as更改模块名字
import module as dicts

dicts.print_dicts("Mpy", "MPY", a="a", b="b")

# 使用as更换函数名字
from module import print_list as list

b = ["a", "b", "c", "d"]
list(b)
