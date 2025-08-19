# Python函数式编程

## 函数定义

在 Python 中，函数的定义使用 `def` 关键字，后面跟函数名和参数列表。函数体由缩进的代码块组成。

**语法**：

```python
def function_name(parameters):
    """函数的文档字符串（可选）"""
    # 函数体
    # 执行任务的代码
```

## 函数调用

调用函数时，需要使用函数名后跟括号，并传入必要的参数。

## 函数返回值

函数可以使用 `return` 语句拥有返回值。如果没有 `return`，函数默认返回 `None`。

**return 关键字的作用**：

- return 是一个关键字， return 后面的值叫“返回值”
- 不写 return 的情况下，会默认返回一个 None
- 一旦遇到 return，结束整个函数
- 返回多个值会被组织成元组被返回，也可以用多个值来接收
- 使用多个值接收(值的数量必须跟返回值数量对应)

**示例**：

```python
# 1. 无返回值的函数（默认返回None）
def greet():
    print("Hello!")

result = greet()
print(f"无返回值函数的返回值: {result}")  # 输出: None

# 2. 单返回值的函数
def calculate_square(number):
    return number ** 2

square = calculate_square(5)
print(f"5的平方是: {square}")  # 输出: 25

# 3. 多返回值的函数
def get_user_info():
    name = "张三"
    age = 25
    city = "北京"
    return name, age, city

# 使用多个变量接收返回值
user_name, user_age, user_city = get_user_info()
print(f"用户信息: {user_name}, {user_age}岁, 来自{user_city}")

# 使用单个变量接收（返回值会被组织成元组）
user_info = get_user_info()
print(f"用户信息（元组）: {user_info}")

# 4. 条件返回的函数
def check_number(num):
    if num > 0:
        return "正数"
    elif num < 0:
        return "负数"
    else:
        return "零"

print(check_number(10))   # 输出: 正数
print(check_number(-5))   # 输出: 负数
print(check_number(0))    # 输出: 零
```

##  函数参数

在 Python 中，函数的参数是用于向函数传递输入数据的变量。通过参数，函数可以根据不同的输入执行不同的操作。Python 支持多种类型的参数，每种参数类型都有其特定的用途和特点。

### 形参

在函数定义时用来占位置的字符，可以是任何字符，用来表示函数需要有一个参数传递进来……

- 形参是在函数定义时指定的参数。它们用于接收函数调用时传递的值。
- 形参在函数体内作为变量存在，作用域仅限于函数内部。

### 实参

在函数调用的时候实际传递进去的参数，是一个具体的值，参与函数内部的处理……

- 实参是在函数调用时传入的实际值。实参可以是常量、变量、表达式或其他函数的返回值。
- 实参的值被传递给形参。

### 位置参数

位置参数是最常用的参数类型，调用时根据位置传递给函数。参数的数量和顺序必须与函数定义时一致。

### 默认参数

默认参数允许为函数的参数设置默认值。调用函数时，如果没有提供该参数的值，则使用默认值。

### 关键字参数

按照形参的参数名进行精确传参，使用关键字参数的时候可以不用考虑形参的具体位置和顺序

**示例：**

```python
# 形参 & 实参
def greet01(name):
    print(f"Hello, {name}!")

greet01("EaglesLab") 
greet01("英格科技")

# 位置参数
def greet02(name, age):
    print(f"Hello, {name}! Age: {age}")

greet01("EaglesLab", 11)

# 默认参数 & 关键字参数 & 可选参数
def greet03(name, site="cloud.eagleslab.com", address="zj"):
    print(f"Site: {site}, Address: {address}")

greet03(address="nj", site="ncloud.eagleslab.com", name="EagelsLab")
```

# Python 装饰器

在 Python 中，装饰器是一个非常强大的功能，可以在不修改函数代码的情况下，动态地修改函数/方法的行为。装饰器本质上是一个函数，它接受一个函数作为参数并返回一个新的函数。

应用场景：比如插入日志，性能测试，事务处理，缓存等等场景。

##  装饰器形成的过程

如果我想测试某个函数的执行时间

```python
import time

def func1():
    print('in func1')

def timer(func):
    def inner():
        start = time.time()
        func()
        print(time.time() - start)
    return inner

func1 = timer(func1)  # 将函数本身做为参数传递进去
func1()
```

##  装饰带参数的函数

装饰一个带参数的函数与装饰一个不带参数的函数类似，但需要在装饰器中处理传递给被装饰函数的参数。

**示例：**

```python
import time

def timer(func):
    def inner(a):
        start = time.time()
        func(a)
        print(time.time() - start)
    return inner

@timer
"""
func1 = timer(func1)
"""
def func1(a):
    time.sleep(1)
    print(a)

func1('hello world')
```

##  装饰带多个参数的函数

这里我们利用了函数里面的动态参数进行传参

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # 打印传入的参数
        print(f"调用 {func.__name__} 函数，参数: {args}, 关键字参数: {kwargs}")
        # 调用原始函数并获取结果
        result = func(*args, **kwargs)
        # 打印返回结果
        print(f"{func.__name__} 函数返回: {result}")

        return result
    return wrapper

@my_decorator
def add(x, y):
    """返回两个数的和"""
    return x + y

# 测试
result = add(5, 3)
print(f"最终结果: {result}")
```

#  多个装饰器装饰一个函数

可以将多个装饰器应用于同一个函数。这种情况下，装饰器会按照从内到外的顺序依次应用。

```python
def wrapper1(func):
    def inner1():
        print('第一个装饰器，在程序运行之前')
        func()
        print('第一个装饰器，在程序运行之后')
    return inner1

def wrapper2(func):
    def inner2():
        print('第二个装饰器，在程序运行之前')
        func()
        print('第二个装饰器，在程序运行之后')
    return inner2

@wrapper1
@wrapper2
def f():
    print('Hello')

f()

"""
执行过程分析：
1. f = wrapper2(f) -> func = f, return inner2
2. f = wrapper1(f) -> func = inner2, return inner1
3. f() = inner1() -> inner2() -> f() -> inner2() -> inner1()
"""
```

