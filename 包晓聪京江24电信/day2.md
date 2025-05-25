1python装饰器：

在一个源代码的基础上想要添加一个代码且不动源代码的基础上

```python
def func1():
    print("in func1")

# 新的需求，能够打印如下内容...
# hello world
# in func1
# hello python

# 实现
def func2(func):
    def inner():
        print("hello world")
        func()
        print("hello python")
    return inner

func1 = func2(func1)
func1()
```

语法糖：可以将func1=func2（func1）化作@定义的函数名放在语句首位 

wraps装饰器：保留被装饰的函数的元函数 方便之后调用函数

```python
from functools import wraps
import time

def func1():
    print('in func1')

def timer(func):
    @wraps(func)
    def inner():
        start = time.time()
        func()
        print(time.time() - start)
    return inner

func1 = timer(func1)    # 将函数本身做为参数传递进去
print(func1.__name__)   # 查看函数的名称
```

2迭代器和生成器：

可以使用for循环的循环取值的为可迭代

迭代器：

+ <font style="color:rgb(51, 51, 51);">实现</font><font style="color:rgb(51, 51, 51);"> </font>`<font style="background-color:rgb(247, 247, 247);">__iter__()</font>`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">方法，返回一个可迭代对象</font>
+ <font style="color:rgb(51, 51, 51);">实现 </font>`<font style="background-color:rgb(247, 247, 247);">__getitem__()</font>`<font style="color:rgb(51, 51, 51);"> 方法，支持从索引0开始的顺序访问</font>
+ <font style="color:rgb(51, 51, 51);">迭代器是一种用于遍历可迭代对象的对象。它可以记录遍历的位置，</font>

<font style="color:rgb(51, 51, 51);">可迭代对象可以通过</font><font style="color:rgb(51, 51, 51);"> </font>`<font style="background-color:rgb(247, 247, 247);">__iter__</font>`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">方法返回一个迭代器，我们在迭代一个可迭代对象的时候，实际上就是先获取该对象提供的一个迭代器，然后通过这个迭代器来依次获取对象中的每一个数据。</font>

<font style="color:rgb(51, 51, 51);">上面讲到迭代是访问集合元素的一种方式。而迭代器是一个可以记住遍历的位置的对象。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束，迭代器只能往前不会后退。</font>

```python
l = [1, 2, 3, 4]
t = (1, 2, 3, 4)
d = {1: 2, 3: 4}
s = {1, 2, 3, 4}

print(dir(l))
print(dir(t))
print(dir(d))
print(dir(s))
```

生成器为一种特殊的迭代器

<font style="color:rgb(51, 51, 51);">生成器也是一个函数，但与普通函数不同的是，它使用</font><font style="color:rgb(51, 51, 51);"> </font>`<font style="background-color:rgb(247, 247, 247);">yield</font>`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">关键字来返回值。每次调用生成器函数时，它会从上次</font><font style="color:rgb(51, 51, 51);"> </font>`<font style="background-color:rgb(247, 247, 247);">yield</font>`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">的地方继续执行，直到遇到下一个</font><font style="color:rgb(51, 51, 51);"> </font>`<font style="background-color:rgb(247, 247, 247);">yield</font>`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">或函数结束。</font>

<font style="color:rgb(51, 51, 51);">调用生成器函数不会得到返回的具体的值，而是得到一个迭代器。每一次获取这个迭代器值，就能推动函数的执行，获取新的返回值。直到函数执行结束。</font>

```python
def numbers(n):
    """生成从 1 到 n 的自然数"""
    for i in range(1,n+1):
        yield i

for i in numbers(10):
    print(i)
```

send：形式；g.send()#可以给上一个yield传递一个值

作用：

可以控制数据的产生，避免一下子产生大量数据

高效利用内存资源

我们需要多少数据，就调用生成器生成多少数据即可

3python推导式：

```python
# 生成0~10的一个列表
l = [i for i in range(11)]
print(l)                # 输出: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 生成平方数的列表
squares = [x ** 2 for x in range(10)]
print(squares)          # 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 生成偶数的列表
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)      # 输出: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

集合推导式

字典推导式：运用字典推导式将元素定义为一个key 可以用字典推导式形成一个字典

4内置函数和匿名函数

<font style="color:rgb(51, 51, 51);">截止到python版本3.9.22，python一共为我们提供了</font>**<font style="color:rgb(51, 51, 51);">69个内置函数。</font>**

[<font style="color:rgb(65, 131, 196);">https://docs.python.org/zh-cn/3.9/library/functions.html</font>](https://docs.python.org/zh-cn/3.9/library/functions.html)

