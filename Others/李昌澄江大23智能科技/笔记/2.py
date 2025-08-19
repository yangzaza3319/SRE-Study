def func1():
    print("in func1")

# # 新的需求，能够打印如下内容...
# # hello world
# # in func1
# # hello python
# # 实现

def func2(func):
    def inner():
        print("hello world")
        func()
        print("hello python")
    return inner

func1 = func2(func1)
func1()

# Output:
# hello world
# in func1
# hello pythons

# def demo(args, *kwargs, **kwargws):
#     print(args)
#     print(kwargs)
#     print(kwargws)

# demo(1, 2, a=3, b=4, c=5)



import time
from functools import wraps

# 装饰器 1：打印执行时间
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} 执行时间: {execution_time:.4f}秒")
        return result
    return wrapper

# 装饰器 2：打印函数参数
def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__} 函数，参数: {args}, 关键字参数: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@timing_decorator
@logging_decorator
def add(x, y):
    """返回两个数的和"""
    time.sleep(1)  # 模拟耗时操作
    return x + y

# 测试
# result = add(5, 3)
# print(f"加法结果: {result}")
"""
Output:
调用 add 函数，参数: (5, 3), 关键字参数: {}
add 执行时间: 1.0001秒
加法结果: 8
"""


# def outer(func):
#     def inner(*args,**kwargs):
#         '''执行函数之前要做的'''
#         re = func(*args,**kwargs)
#         '''执行函数之后要做的'''
#         return re
#     return inner


# # 下面是加上wraps的固定结构
# from functools import wraps

# def outer(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         '''执行函数之前要做的'''
#         re = func(*args,**kwargs)
#         '''执行函数之后要做的'''
#         return re
#     return inner

"""
很显然
完蛋了
"""

#dir() 输出对象所有信息
# iter() 返回一个迭代器对象
#len() 返回对象长度
#max() 返回最大值

#help() 输出对象的帮助信息
#id() 输出对象的内存地址

"""
Python 中的可迭代对象
可迭代对象是指可以被迭代的对象,通常是实现了__iter__()方法的对象。
set tuple list dict str
"""

"""Python 中，迭代器是一种用于遍历集合（如列表、元组、字典等）中元素的对象。

可迭代对象通过__iter__方法向我们提供一个迭代器,
我们在迭代一个可迭代对象的时候，实际上就是先获取该对象提供的一个迭代器，
然后通过这个迭代器来依次获取对象中的每一个数据。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

可迭代对象通过iter()方法返回一个迭代器对象，
迭代器对象通过next()方法访问集合中的下一个元素。"""

"""生成器的本质
生成器是一个特殊的迭代器，它是通过函数来创建的。
生成器函数是一个包含yield语句的函数
当调用生成器函数时，它不会立即执行，而是返回一个生成器对象。
这个生成器对象可以被迭代,每次迭代时,函数会从上次停止的地方继续执行,直到遇到下一个yield语句。"""


"""生成器函数
第一次初始化时返回生成器
send()可往生成器函数内部发送数据同时执行next()方法

第一次使用生成器的时候 是用next获取下一个值
最后一个yield不能接受外部的值
"""
# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1
# # 使用生成器  
# gen = countdown(5)
# for num in gen:
#     print(num)



# def produce():
#     # 生产包子
#     for i in range(1,100):
#         yield f'生产了第{i}笼包子'

# produce_g = produce()
# print(produce_g.__next__())
# print(produce_g.__next__())
# print(produce_g.__next__())

# # 顾客下单了，需要5笼包子
# for i in range(5):
#     print(produce_g.__next__())

# Output:
"""
生产了第1笼包子
生产了第2笼包子
生产了第3笼包子
生产了第4笼包子
生产了第5笼包子
生产了第6笼包子
生产了第7笼包子
生产了第8笼包子
"""

# def generator():
#     print("开始执行生成器")
#     yield 1
#     print("继续执行生成器")
#     yield 2
#     print("继续执行生成器")
#     yield 3
#     # total = 5
#     # while  n <= 10:
#     #     yield total
#     #     total += 1
    
# debug = generator()
# print(debug)
# print(next(debug))
# print(next(debug))
# print(next(debug))


# print(type(debug))

"""
python推导式 列表推导式、字典推导式、集合推导式、生成器推导式
new_list = [expression for item in iterable if condition]

new_set = {expression for item in iterable if condition}

new_dict = {key_expression: value_expression for item in iterable if condition}

new_gen = (expression for item in iterable if condition)

gen_expr = (x ** 2 for x in range(5))
print(gen_expr)  

# Output: 
<generator object <genexpr> at 0x...>
"""

# fruits = [['peach','Lemon','Pear','avocado','cantaloupe','Banana','Grape'],
#           ['raisins','plum','apricot','nectarine','orange','papaya']]

# print([name for lst in fruits for name in lst if name.count('a') >= 2])

# result = []
# for lst in fruits:
#     for name in lst:
#         if name.count('a') >= 2:
#             result.append(name)
# print(result)

# Output:
# ['avocado', 'cantaloupe', 'Banana', 'papaya']

# list = [1,2,3,4,5,6,7,8,9]
# # list = [i for i in range(1,10)]
# # list = [i for i in range(1,10) if i % 2 == 0]
# print(list)
# print(set(list))

# new_dict = {i: i ** 2 for i in range(1, 10) if i> 5}
# print(new_dict)

# name = 'Eagleslab'
# new_dict = {i: ord(i) for i in name}
# print(new_dict)

# new_dict = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# for k in new_dict.keys():
#     print(k, new_dict[k])
#     new_dict[[k]] = k
#     print(k, new_dict[k])

# new_dict = {dict[k]: k for k in new_dict}
# print(k, new_dict[k])

# old_dict = {'a': 1, 'b': 2, 'c': 3}
# new_dict = {v: k for k, v in old_dict.items()}
# print(new_dict)

# print(old_dict.items())

# print('\n'.join(['\t'.join([f'{i}x{j}={i * j}' for i in range(1,j+1)]) for j in range(1, 10)]))


# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{i}x{j}={i*j}', end='\t')
#     print()

# ret = eval('2 + 2')
# print(ret)

# n = 20
# ret = eval('n + 23')
# print(ret)

# eval('print("Hello world")')

# print(id(123))

# print(help(dir))
# 查看当前对象的所有属性和方法（包括内置属性和方法）（不包括私有属性和方法）(__开头和__结尾的属性和方法）
# print(dir())
# iter() & next() & range()

# print(divmod(7,2))  # (3, 1)

# abs：函数返回数字的绝对值。
# divmod：计算除数与被除数的结果，返回一个包含商和余数的元组(a // b, a % b)。
# round：保留浮点数的小数位数，默认保留整数。
# pow：函数是计算x的y次方，如果z在存在，则再对结果进行取模，其结果等效于pow(x,y) %z）
# print(abs(-5))  # 5

# print(divmod(7,2))  # (3, 1)

# print(round(7/3,2))  # 2.33
# print(round(7/3))  # 2
# print(round(3.32567,3))  # 3.326

# print(pow(2,3))  # 8
# print(pow(2,3,3))  # 2

# sum：对可迭代对象进行求和计算（可设置初始值）。
# min：返回可迭代对象的最小值（可加key，key为函数名，通过函数的规则，返回最小值）。
# max：返回可迭代对象的最大值（可加key，key为函数名，通过函数的规则，返回最大值）。

# print(sum([1,2,3,4,5]))  # 15
# print(sum([1,2,3,4,5],10))  # 25

# print(min([1,2,3,4,5]))  # 1
# print(min([1,2,3,4,5],key=lambda x: x))  # 1
# print(min([1,2,3,4,5],key=lambda x: -x))  # 5
# print(max([1,2,3,4,5]))  # 5
# print(max([1,2,3,4,5],key=lambda x: x))  # 5
# print(max([1,2,3,4,5],key=lambda x: -x))  # 1
# print(min('hello world'))  # ' '
# print(max('hello world'))  # 'w'

# ret = min([1,2,3,-10],key=abs)
# print(ret)

# # str()  将对象转换为字符串
# format = 'hello {}'
# print(format.format('world'))  # hello world

# # format = 'hello {0} {1}'
# # print(format.format('world','python'))  # hello world python
# # format = 'hello {0} {1} {0}'# 字符串可以提供的参数,指定对齐方式，<是左对齐， >是右对齐，^是居中对齐
# print(format('test','<20'))
# print(format('test','>20'))
# print(format('test','^20'))

# # 整形数值可以提供的参数有 'b' 'c' 'd' 'o' 'x' 'X' 'n' None
# print(format(192,'b'))  # 转换为二进制
# print(format(97,'c'))   # 转换unicode成字符
# print(format(11,'d'))   # 转换成10进制
# print(format(11,'o'))   # 转换为8进制
# print(format(11,'x'))   # 转换为16进制，小写字母表示
# print(format(11,'X'))   # 转换为16进制，大写字母表示
# print(format(11,'n'))   # 和d一样
# print(format(11))       # 和d一样

# # 浮点数可以提供的参数有 'e' 'E' 'f' 'F' 'g' 'G' 'n' '%' None
# print(format(314159265,'e'))    # 科学计数法，默认保留6位小数
# print(format(314159265,'0.2e')) # 科学计数法，保留2位小数
# print(format(314159265,'0.2E')) # 科学计数法，保留2位小数,大写E
# print(format(3.14159265,'f'))   # 小数点计数法，默认保留6位小数
# print(format(3.14159265,'0.10f'))    # 小数点计数法，保留10位小数
# print(format(3.14e+10000,'F'))    # 小数点计数法，无穷大转换成大小字母

# # g的格式化比较特殊，假设p为格式中指定的保留小数位数，先尝试采用科学计数法格式化，得到幂指数exp，如果-4<=exp<p，则采用小数计数法，并保留p-1-exp位小数，否则按小数计数法计数，并按p-1保留小数位数
# print(format(0.00003141566,'.1g'))
# # p=1,exp=-5 ==》 -4<=exp<p不成立，按科学计数法计数，保留0位小数点
# print(format(0.00003141566,'.2g'))
# # p=2,exp=-5 ==》 -4<=exp<p不成立，按科学计数法计数，保留1位小数点

# print(format(3.1415926777,'.1g'))
# # p=1,exp=0 ==》 -4<=exp<p成立，按小数计数法计数，保留0位小数点
# print(format(3.1415926777,'.2g'))
# # p=2,exp=0 ==》 -4<=exp<p成立，按小数计数法计数，保留1位小数点
# print(format(3141.5926777,'.2g'))
# # p=2,exp=3 ==》 -4<=exp<p不成立，按科学计数法计数，保留1位小数点

# print(format(0.00003141566,'.1n'))  # 和g相同
# print(format(0.00003141566))        # 和g相同

# repr:返回一个对象的string形式
# name = 'aaron'
# print('Hello %r'%name)

# str1 = '{"name":"aaron"}'
# print(repr(str1))
# print(str1)

# enumerate: 用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
# all：可迭代对象中，全都是True才是True
# any：可迭代对象中，有一个True 就是True
# zip：函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同。


# def func(x):
#     return x%2 == 0
# ret = filter(func,[1,2,3,4,5,6,7,8,9,10])
# print(ret)
# for i in ret:
#     print(i)

def square(x):
    return x**2

list1 = [1,2,3,4,5,6,7,8]

ret = map(square,list1)
print(ret)

for i in ret:
    print(i)


# 自定义模块就是一个包含 Python 代码的 .py 文件。你可以将函数、类、变量写入该文件中，然后在其他 Python 文件或脚本中通过 import 语句导入并使用它们。

# 创建一个 Python 文件：把你想要封装的代码写入一个 .py 文件中。

# 导入自定义模块：在另一个 Python 文件中，使用 import 语句导入这个模块。

# 模块（module） 是一个包含 Python 代码的文件，通常以 .py 结尾。模块可以包含变量、函数、类，甚至其他模块。通过模块，我们可以将代码组织成不同的文件，更好地管理和复用代码。

# 模块可以分为以下几类：

# 标准库模块：Python 自带的模块，如 math、os、sys 等。
# 第三方模块：由其他开发者编写的模块，通常可以通过 pip 安装。
# 自定义模块：用户自己编写的模块。

# 导入模块时，Python 会为该模块创建一个独立的命名空间，模块内的所有变量、函数和类都属于该命名空间，从而避免与当前代码中的名称发生冲突。

"""
1. 使用 import 语句导入模块
import math 
2. 使用 from ... import 语句导入模块中的特定函数或变量
from math import sqrt, pi
3. 使用 as 关键字为模块或函数起别名
import math as m
from math import sqrt as square_root
4. 使用 import ... as ... 语句为模块起别名
import math as m
5. 使用 from ... import * 导入模块中的所有函数和变量（不推荐使用）
6. 使用 __name__ 属性判断模块是否被直接运行       
7. 使用 __all__ 属性定义模块中可以被导入的名称
8. 使用 __init__.py 文件将多个模块组织成一个包
9. 使用 importlib 模块动态导入模块
10. 使用 sys.modules 查看已导入的模块
11. 使用 reload() 函数重新加载模块
12. 使用 dir() 函数查看模块中的所有属性和方法
13. 使用 help() 函数查看模块的帮助文档
14. 使用 __doc__ 属性查看模块的文档字符串
15. 使用 __file__ 属性查看模块的文件路径
16. 使用 __package__ 属性查看模块的包名
17. 使用 __spec__ 属性查看模块的规格
18. 使用 __cached__ 属性查看模块的缓存路径
19. 使用 __loader__ 属性查看模块的加载器
20. 使用 __path__ 属性查看模块的路径
21. 使用 __name__ 属性查看模块的名称
22. 使用 __package__ 属性查看模块的包名
23. 使用 __spec__ 属性查看模块的规格
24. 使用 __cached__ 属性查看模块的缓存路径
25. 使用 __loader__ 属性查看模块的加载器
26. 使用 __path__ 属性查看模块的路径
27. 使用 __name__ 属性查看模块的名称
28. 使用 __package__ 属性查看模块的包名
29. 使用 __spec__ 属性查看模块的规格
30. 使用 __cached__ 属性查看模块的缓存路径
31. 使用 __loader__ 属性查看模块的加载器
32. 使用 __path__ 属性查看模块的路径
33. 使用 __name__ 属性查看模块的名称
34. 使用 __package__ 属性查看模块的包名
35. 使用 __spec__ 属性查看模块的规格

注意：如果my_module.py中的名字前加`_`,即`_`money，则from my_module import *,则`_`money不能被导入
编写好的一个python文件可以有两种用途：

脚本，一个文件就是整个程序，用来被执行

模块，文件中存放着一堆功能，用来被导入使用
python为我们内置了全局变量__name__，

当文件被当做脚本执行时：__name__ 等于'__main__'

当文件被当做模块导入时：__name__等于模块名

作用：用来控制.py文件在不同的应用场景下执行不同的逻辑（或者是在模块文件中测试代码）

if __name__ == '__main__':

模块的搜索路径
1. 当前目录
2. PYTHONPATH 环境变量：包含一系列目录名
3. 标准库：python 安装时自带的
4. sitepackages目录：第三方库的默认安装目录，通过pip安装

模块的查找顺序是：内存中已经加载的模块->自建模块->sys.path路径中包含的模块

在第一次导入某个模块时（比如my_module），会先检查该模块是否已经被加载到内存中（当前执行文件的名称空间对应的内存），如果有则直接引用 ps：python解释器在启动时会自动加载一些模块到内存中，可以使用sys.modules查看
如果没有，解释器则会查找同名的内建模块
如果还没有找到就从sys.path给出的目录列表中依次寻找my_module.py文件。
"""

# 不建议在代码中直接修改sys.path，最好通过环境变量PYTHONPATH来设置模块搜索路径
# 搜索路径的优先级按照sys.path中的顺序来查找,越靠前优先级越高
# 在导入模块时一旦在某个路径下找到了对应的模块，就会停止继续搜索

"""
包：包就是一个包含有__init__.py文件的文件夹，所以其实我们创建包的目的就是为了用文件夹将文件/模块组织起来

需要强调的是：

在python3中，即使包下没有__init__.py文件，import 包仍然不会报错，而在python2中，包下一定要有该文件，否则import 包报错

创建包的目的不是为了运行，而是被导入使用，记住，包只是模块的一种形式而已，包的本质就是一种模块
"""

# __all__：用于定义模块中可以被导入的名称
# __name__：用于判断模块是否被直接运行
# __file__：用于查看模块的文件路径
"""
glance/                   #Top-level package
├── __init__.py      #Initialize the glance package
├── api                  #Subpackage for api
│   ├── __init__.py
│   ├── policy.py
│   └── versions.py
├── cmd                #Subpackage for cmd
│   ├── __init__.py
│   └── manage.py
└── db                  #Subpackage for db
    ├── __init__.py
    └── models.py
"""
# __init__.py  
# __all__ = ['api', 'cmd', 'db']  # 定义可以被导入的名称
# __name__ = 'glance'  # 定义模块名称
# __file__ = 'glance/__init__.py'  # 定义模块文件路径