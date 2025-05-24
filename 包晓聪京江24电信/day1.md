python为强类型语言

数据结构：

字符串为加了引号的字符序列

列表：相比字符串 列表为可变的可以储存不同类型元素

索引：在定义的变量后【】 【】内从0开始输出第一个字符

<font style="color:rgb(51, 51, 51);">切片是按照一定的索引规律分割列表从而组成一个新的列表，类似与我们字符串中讲到的切片</font>

```python
li = [1,2,4,5,4,2,4]
sub_li = li[2:5]
print(sub_li)

# Output:
[4, 5, 4]
```

元组：可读不可变的集合，但若集合内的元素为可变元素则集合可变

*******字典：<font style="color:rgb(51, 51, 51);">字典是 python 中唯一的映射类型，采用键值对（key-value）的形式存储数据。python 对 key 进行哈希函数运算，根据计算的结果决定 value 的存储地址，所以字典是无序存储的，且key必须是可哈希的。可哈希表示 key 必须是不可变类型，如：数字、字符串、元组。</font>

<font style="color:rgb(51, 51, 51);">键值：而且键是具有唯一性的，每个键只能出现一次，但是值没有限制，在一个字典中可以出现多个相同的值。</font>

```python
dic = {'name':'nls','age':18,'job':'teacher'}
print(dic)
print(dic['name'])
print(dic['age'])
print(dic['job'])

# Output:
{'name': 'nls', 'age': 18, 'job': 'teacher'}
nls
18
teacher
```

可变集合意味其是不是可哈希









区别

列表：

集合：

元组：

字典：



