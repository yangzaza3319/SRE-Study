# Python 基本数据结构

## 列表（List）

列表是一个有序的可变集合，可以存储不同类型的元素。列表相比于字符串，不仅可以储存不同的数据类型，而且可以储存大量数据。而且列表是有序的，有索引值，可切片，方便取值

### 定义列表

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Output:
['apple', 'banana', 'cherry']
```

###  增加元素

```python
# 1. 按照索引的位置去增加
fruits.insert(1, "kiwi")

# 2. 在最末尾添加
fruits.append("orange")

# 3. 用迭代的方式去添加
fruits.extend(['a','b','c'])        
# 可以立即为再传递一个List进去，然后依次添加到末尾,而append会把括号里的当成一个整体添加到末尾

# Output:
['apple', 'kiwi', 'banana', 'cherry', 'orange', 'a', 'b', 'c']
```

### 删除元素

```python
# 1. 删除制定的具体元素
fruits.remove("cherry")

# 2. 按照索引位置去删除
fruits.pop()        # 默认是删除最后一个，可以加上索引。并且有返回值，返回值为删除的元素
fruits.pop(1)

# 3. 使用切片范围删除
del fruits[1:3]        # 没有返回值

# 4. 清空列表
fruits.clear()

# 5. 删除列表
del fruits

# clear是清空列表的内容，变成一个空列表，而del是删除列表本身，后续无法再次调用...

# Output:
['apple', 'banana', 'cherry']
['apple', 'kiwi', 'banana', 'cherry', 'orange', 'a', 'b', 'c']
[]
```

### 修改元素

```python
# 1. 按照索引修改某个元素的值
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
print(fruits)

# Output:
['apple', 'orange', 'cherry']

# 2. 按照切片范围修改
fruits[0:2] = ['kiwi','orange']
print(fruits)

# Output:
['kiwi', 'orange', 'cherry']
```

```python
#查找元素
# 1. index(element)：返回元素的索引
fruits = ["apple", "banana", "cherry"]
index_of_apple = fruits.index("apple")
print(index_of_apple)

# Output:
0

# 2. count(element)：返回元素出现的次数
count_of_cherry = fruits.count("cherry")
print(count_of_cherry)

# Output:
1
```

# 元组（Tuple）

有序的不可变集合，也被被称为只读列表，即数据可以被查询，但不能被修改。

### 定义元组

```python
tuple = (1,2,3,'a','b','c')
print(tuple)
print(tuple[1])

# 可以删除元素吗?
tuple.pop()

# Output:
AttributeError: 'tuple' object has no attribute 'pop'
```

### 可变元组

tuple 其实不可变的是地址空间，如果地址空间里存的是可变的数据类型的话，比如列表就是可变的

# 字典（Dict）

字典是 python 中唯一的映射类型，采用键值对（key-value）的形式存储数据。python 对 key 进行哈希函数运算，根据计算的结果决定 value 的存储地址，所以字典是无序存储的，且key必须是可哈希的。可哈希表示 key 必须是不可变类型，如：数字、字符串、元组。

不过在 Python 3.6 版本以后，字典会保留插入顺序，变成有序数据结构。

而且键是具有唯一性的，每个键只能出现一次，但是值没有限制，在一个字典中可以出现多个相同的值。

###  定义字典

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

# 集合（Set）

集合是**无序**的，**不重复**，**确定性**的数据集合，它里面的元素是可哈希的(不可变类型)，但是集合本身是不可哈希（所以集合做不了字典的键）的。以下是集合最重要的两点：

- 去重，把一个列表变成集合，就自动去重了。
- 关系测试，测试两组数据之前的交集、差集、并集等关系。

### 定义集合

```python
set1 = {1,2,3,'a','b','c'}        # 推荐方法
set2 = set({1,2,3})

print(set1, set2)

# Output:
{1, 2, 3, 'b', 'c', 'a'} {1, 2, 3}
```

## 数据结构的总结

| 数据结构   | 描述             | 特性                   | 常见操作               | 适用场景                                 | 优点                        | 缺点                                  |
| :--------- | :--------------- | :--------------------- | :--------------------- | :--------------------------------------- | :-------------------------- | :------------------------------------ |
| **列表**   | 有序的可变集合   | 有序、可变、支持重复   | 添加、删除、修改、查找 | 需要维护元素顺序的场景，如队列、栈的实现 | 灵活性高，支持多种操作      | 查询复杂度为 O(n)，插入和删除性能较差 |
| **元组**   | 有序的不可变集合 | 有序、不可变、支持重复 | 查找                   | 元素不需要修改的场景，如函数参数、字典键 | 更节省内存，速度较快        | 不支持修改                            |
| **集合**   | 无序的可变集合   | 无序、可变、不支持重复 | 添加、删除、查找       | 需要去重和快速查找的场景，如集合运算     | 快速查找和去重              | 不支持索引，元素无序                  |
| **字典**   | 有序的键值对集合 | 有序、可变、键唯一     | 添加、删除、修改、查找 | 需要快速查找和存储键值对的场景，如缓存   | 快速查找（O(1) 平均复杂度） | 键必须是不可变类型，内存开销较大      |
| **字符串** | 字符的序列       | 不可变                 | 查找、切片、替换       | 文本处理                                 | 易于使用，内置丰富的方法    | 不可修改，性能较低                    |

## enumerate

enumerate：枚举，对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate 将其组成一个索引序列，利用它可以同时获得索引和值。

```python
li = ['甲','乙','丙','丁']
for i in enumerate(li):
    print(i)

for index,value in enumerate(li):
    print(index,value)

for index,value in enumerate(li,100): #从哪个数字开始索引
    print(index,value)

# Output:
(0, '甲')
(1, '乙')
(2, '丙')
(3, '丁')
0 甲
1 乙
2 丙
3 丁
100 甲
101 乙
102 丙
103 丁
```

