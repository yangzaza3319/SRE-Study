#1.修饰器案例切入
def func1():
    print("在func1()中")

""" 
需求：打印下列内容
hello world
in function1
hello python
"""

# 案例实现
def func2(func):
    def inner():
        print("hello world")
        func()
        print("hello python")
    return inner
func1 = func2(func1)
func1()


#2. 测试某个函数的执行时间（常规方式）
import time

def func1():
    print('in func1')

def timer(func):
    def inner():
        start = time.time()
        func()
        print(time.time() - start)
    return inner

func1 = timer(func1)  # 将dunc1()函数作为参数传出去
func1()


#3.测试某个函数的执行时间（语法糖）
import time

def timer(func):
    def innner():
        start = time.time()
        func()
        print(time.time() -start)
    return innner
@timer
def func2():
    time.sleep(1)
    print('in func2')
func2()

"""
调试结果
显式执行func2()函数
    ——>输出
    in func2
    1.0043830871582031
"""
"""
当我们在某个函数上方使用@my_decorator 的时候，python会自动将下面定义的函数作为参数传递给@my_decorator，即func1 = timer(func1)
"""

#4.装饰带单个参数的函数
import time

def timer(func):
    def inner(a):
        start = time.time()
        func(a)
        print(time.time() - start)
    return inner

@timer
def func3(a):
    time.sleep(1)
    print(a)
func3("hello_world")

"""
输出
hello_world
1.0029830932617188
"""

# 5 装饰带多个位置参数的函数
# 利用多个参数进行传参
def my_decorator(func):
    def wrapper(*args,**kwargs):
        print(f"调用{func.__name__}函数返回：位置参数：{args}，关键字参数：{kwargs}") # 打印调用的函数、传入的参数（此处没有用到关键字参数，所以打印的kwargs参数为空）
        result = func(*args,**kwargs)                                       # 调用原始函数并获取结果
        print(f"{func.__name__}函数返回：{result}")                           # 打印返回结果
        return result
    return wrapper

@my_decorator
def add(x,y):
    return x + y

result = add(3,4)
print(f"最终结果：{result}")
"""
    输出结果
调用add函数返回：参数：(3, 4)，关键字参数：{}
add函数返回：7
最终结果：7
"""

# 6 wraps装饰器

## 回顾开始的案例
import time
def func1():
    print('in func1')

def timer(func):
    def inner():
        start = time.time()
        func()
        print(time.time() - start)
    return inner
func1 = timer(func1) # 将函数本身作为参数传递进去
func1()
### 问题1——>最后执行的`func1`函数和最初的`func1`是否为同一个函数
#问题1 解法：打印函数名

import time
def func1():
    print('in func1')

def timer(func):
    def inner():
        start = time.time()
        func()
        print(time.time() - start)
    return inner
func1 = timer(func1)
print(func1.__name__)
"""
输出
inner
"""

# 使用wraps装饰器装饰
from functools import wraps
import time

def fun1():
    print('in func1')

def timer(func):
    @wraps(func)
    def innner():
        start = time.time()
        func()
        print(time.time() - start)
    return innner
func1 = timer(func1)
print(func1.__name__)