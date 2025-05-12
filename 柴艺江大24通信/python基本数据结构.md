##  

## Python 基本数据结构

### 列表（List）

列表是一个有序的可变集合，可以存储不同类型的元素。列表相比于字符串，不仅可以储存不同的数据类型，而且可以储存大量数据。而且列表是有序的，有索引值，可切片，方便取值。

##### 定义列表

```python
lis=['apple','kiwi',1,2,3,4,5]
print(lis)
```

##### 增加元素

```python
a=['apple','banana','peach']

a.insert(1,'kiwi')#在索引1的位置插入kiwi
a.append('blueberry')#在末尾添加

#在列表末尾添加元素,增添的应当是可迭代的对象
a.extend(['欧润吉','strawberry','cherry'])
```

##### 删除元素

```python
a=['apple','banana','peach']
a.remove('apple')

a.pop(1)#按照索引删除元素

del a[1:2]#切片删除

#a.clear() 清空列表
#print(a)
#del a#删除列表
```

##### 修改元素

```python
lis=['apple','kiwi',1,2,3,4,5]

#按照索引修改某个元素的值
lis[1]='欧润吉'   

#按照切片范围修改
lis[2:4]=[6,7]
#Output=[apple','欧润吉',6,7,3,4,5]
```

##### 查找元素

```python
a=[apple','欧润吉',6,7,3,4,5]
print(a.index('欧润吉'))#返回元素第一次出现时的索引
print(a.count('欧润吉'))#返回元素出现次数
```

##### 其他

```python
a.sort()#对列表进行升序排序

a.reverse()#将列表中的元素反向存放

#将列表中的元素进行降序排序
a=list(reversed(a))# a.sort(reverse=True)
print(a)
```

### 元组（Tuple）

有序的不可变集合，也被被称为只读列表，即数据可以被查询，但不能被修改。

##### 定义元组

```python
tup=(1,2,3,'a','b','c')
print(tup[1])#输出元组索引为1的元素
#由于元组的不可变性，修改、删除元素的操作都不被允许（会报错），但可以将整个元组删除
#元组可进行 tup.index() tup.count()的操作
```

### 可变元组

元组其实不可变的是地址空间，如果地址空间里存的是可变的数据类型的话，比如列表就是可变的

```python
tup = (1, 2, 3, [1, 4, 7])
print(tup)
tup[3][2]=2
print(tup)
# Output:
(1, 2, 3, [1, 4, 7])
(1, 2, 3, [2, 4, 7])
```

### 字典（Dict）

字典是 python 中唯一的映射类型，采用键值对（key-value）的形式存储数据。python 对 key 进行哈希函数运

算，根据计算的结果决定 value 的存储地址，所以字典是无序存储的，且key必须是可哈希的。可哈希表示 key 必

须是不可变类型，如：数字、字符串、元组。

不过在 Python 3.6 版本以后，字典会保留插入顺序，变成有序数据结构。

而且键是具有唯一性的，每个键只能出现一次，但是值没有限制，在一个字典中可以出现多个相同的值。

##### 定义字典

```python
# 字典里面的value也可以是容器类型的数据，比如列表，字典等等...但是key必须是不可变的
dic = {'name':'nls','age':18,"phone":['1888888888','0511-10101010']}

c={'name':'cy','age':18,'sch':'jsu'}
print(c)
print(c['name'])
#Outut:{'name':'cy','age':18,'sch':'jsu'}
#Output:cy
```

##### 增加键值

```python
c={'name':'cy','age':18,'sch':'jsu'}
c['hobby']='game' #如果键已经存在，那么就会替换原来的值,不存在则增添这个键值对

# dict.setdefault(key,default=None) 在字典中添加键值对时，如果指定的键已经存在则不做任何操作,如果原字典中不存在指定的键值对，则会添加。
c.setdefault('sex','female')
print(c)
#Output:{'name':'cy','age':18,'sch':'jsu','sex':'female'}
```

##### 删除键值

```python
c={'name':'cy','age':18,'sch':'jsu'}
na=c.pop('name',"查无此项")#删除字典中指定的键值对并返回它的值，不存在则抛会后一项

del dic['age']#使用del关键字删除指定的键值对

c_pop=c.popitem()# 删除字典中最后一个键值对并返回其元组形式  ('sch','jsu')

c.claer()#清空字典
```

##### 修改键值

```python
c={'name':'cy','age':18,'sch':'jsu'}
c['age']=20
print(c)
#Output:{'name':'cy','age':20,'sch':'jsu'}
```

##### 查找键值

```python
c={'name':'cy','age':18,'sch':'jsu'}
v1=c['name']#直接通过键名获取，如果键不存在，会抛出KeyError
print(v1)

v2=c.get('job','查无此项')# 通过键名获取值，如果键不存在，则返回默认值（None）或是自定义的返回值，也可以是个整数

print('name' in c)
```

##### 其他操作

```python
c={'name':'cy','age':18,'sch':'jsu'}
for i in c.items():#对键和值进行迭代
    print(i)# 以元组形式输出

for i in c:#对键进行迭代
    print(i)# 以元组形式输出

for i in c.keys():#对键进行迭代
    print(i)# 以元组形式输出

for i in c.values():#对值进行迭代
    print(i)# 以元组形式输出
    
    
#使用keys()和values()方法获取键值
keys = c.keys()
print(keys,type(keys))

value = c.values()
print(value,type(value))

#Output:dict_keys(['name', 'age', 'sch']) <class 'dict_keys'>
#       dict_values(['cy', 18, 'jsu']) <class 'dict_values'>

```

### 集合

集合是**无序**的，**不重复**，**确定性**的数据集合，它里面的元素是可哈希的(不可变类型)，但是集合本身是不可哈希（所以集合做不了字典的键）的。以下是集合最重要的两点：

- 去重，把一个列表变成集合，就自动去重了。
- 关系测试，测试两组数据之前的交集、差集、并集等关系。

##### 定义集合

```python
set1 = {1,2,3,'a','b','c'}        # 推荐方法
set2 = set({1,2,3})

print(set1, set2)

# Output:
{1, 2, 3, 'b', 'c', 'a'} {1, 2, 3}
```

##### 增加元素

```python
d={'apple','banana','peach'}

d.add('kiwi')#添加元素

# update接收的参数应该是可迭代的数据类型，比如字符串、元组、列表、集合、字典。这些都可以向集合中添加元素，但是整型、浮点型不可以
d.update([1,2,3])#update可添加可迭代对象

print('banana' in d)#判断元素是否存在
```

##### 删除元素

```python
d={'apple','banana','peach'}

d.pop()#随机删除一个元素（因为集合无序）

d.remove('apple')#删除指定元素

#删除集合本身
del d
```

##### 查找元素

```python
d={'apple','banana','peach'}
print('banana' in d)#判断元素是否存在
```

##### 关系测试

```python
set1={1,2,3,4,5}
set2={3,4,5,6,7}
print(set1&set2)#交集，取出两个集合共有的元素
print(set1.intersection(set2))#交集

#反交集
print(set1 ^ set2)
print(set1.symmetric_difference(set2))
# Output:
{1, 2, 6, 7}
{1, 2, 6, 7}

#并集，合并两个集合的所有元素
print(set1 | set2)
print(set2.union(set1))
# Output:
{1, 2, 3, 4, 5, 6, 7}
{1, 2, 3, 4, 5, 6, 7}

#差集，第一个集合去除二者共有的元素
print(set1^set2)
print(set1.difference(set2))
# Output:
{1, 2}
{1, 2}

#子集与超集
#当一共集合的所有元素都在另一个集合里，则称这个集合是另一个集合的子集，另一个集合是这个集合的超集
#返回的都是布尔值
print(set1 < set2)
print(set1.issubset(set2))  # 这两个相同，都是说明set1是set2子集。

print(set2 > set1)
print(set2.issuperset(set1))  # 这两个相同，都是说明set2是set1超集
```

##### 不可变集合

```python
set1 = {1,2,3,4,5,6}

set2 = frozenset(set1)#frozenset()函数，不可变，修改则会报错
print(set2,type(set2))

set2.add(7) # 不可以修改,会报错

# Output:
AttributeError: 'frozenset' object has no attribute 'add'
```

### 数据结构总结

| 数据结构   | 描述             | 特性                   | 常见操作               | 适用场景                                 | 优点                        | 缺点                                  |
| :--------- | :--------------- | :--------------------- | :--------------------- | :--------------------------------------- | :-------------------------- | :------------------------------------ |
| **列表**   | 有序的可变集合   | 有序、可变、支持重复   | 添加、删除、修改、查找 | 需要维护元素顺序的场景，如队列、栈的实现 | 灵活性高，支持多种操作      | 查询复杂度为 O(n)，插入和删除性能较差 |
| **元组**   | 有序的不可变集合 | 有序、不可变、支持重复 | 查找                   | 元素不需要修改的场景，如函数参数、字典键 | 更节省内存，速度较快        | 不支持修改                            |
| **集合**   | 无序的可变集合   | 无序、可变、不支持重复 | 添加、删除、查找       | 需要去重和快速查找的场景，如集合运算     | 快速查找和去重              | 不支持索引，元素无序                  |
| **字典**   | 有序的键值对集合 | 有序、可变、键唯一     | 添加、删除、修改、查找 | 需要快速查找和存储键值对的场景，如缓存   | 快速查找（O(1) 平均复杂度） | 键必须是不可变类型，内存开销较大      |
| **字符串** | 字符的序列       | 不可变                 | 查找、切片、替换       | 文本处理                                 | 易于使用，内置丰富的方法    | 不可修改，性能较低                    |

### 流程控制

##### 判断语句

```python
a,b,c=1,2,3

#单分支
if a==1:
    print(a)
 

#双分支
if a==2:
    print(a)
else:
    print(b)
    
#多分支
if a==3:
    print(a)
elif b==1:
    print(b)
else:
    print(c)
```

##### 循环语句-while

```python
#如果条件为真，那么循环体则执行 如果条件为假，那么循环体不执行
while True:
    print('是真的！！！')
    
    
    
#猜数
import random
num=random.randint(1,101)
count=1
while count<4:
    num1 = int(input("请输入你猜的数字(0-100):"))
    if num1==num:
        print('恭喜你猜对了')
        print(f'一共猜了{count}次')
    elif num1<num:
        print('猜小了')
        print(f'一共猜了{count}次')
    else:
        print('猜大了')
        print(f'一共猜了{count}次')
    count+=1
else:
    print('你输了，游戏结束')
```

###### 循环终止语句

**break**

用于完全结束一个循环，跳出循环体执行循环后面的语句

**continue**

和 break 有点类似，区别在于 continue 只是终止本次循环，接着还执行后面的循环，break 则完全终止循环

**while else**

while 后面的 else 作用是指，当 while 循环**正常执行完**，中间没有被 break 中止的话，就会**执行 else** 后面的语句

- ```python
  while condition:
      # 循环体
      if some_condition:
          break
  else:
      # 循环正常结束时执行的代码
      
      
  #判断一个数是否为素数
  num=int(input("(输入一个大于等于3的整数)"))
  i=2
  
  while i<num:
      if num%i==0:
          print(f"{num}不是素数，它可以被{i}整除")
          break
      i+=1
  else:
      print("这个数是素数")
  ```

##### 循环语句-for

```python
for variable in iterable:
    # 循环体
    # 执行的代码
```

```python
#遍历列表
a=[1,2,3,4,5]
for i in a:
    print(i)
    
    
#遍历字符串
st='Reverse:19999'
for w in st:
    print(w)
```

##### enumerate

enumerate：枚举，对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate 将其组成一个索引序列，利用它可以同时获得索引和值。(返回索引和值组成的元组（index,value）)

```python
for r in enumerate(['cy','jsu','jsu'],2):#从哪个数字开始索引,默认是0
    print(r)
    
'''Output:
(2, 'cy')
(3, 'jsu')
(4, 'jsu')'''

for i,j in enumerate(['cy','jsu','jsu'],2):#从哪个数字开始索引,默认是0
    print(i,j)
'''Output:
2 cy
3 jsu
4 jsu'''
```

##### range

```python
#同样是取前不取后
for i in range(1,10):
    print(i)

for i in range(1,10,2):  # 步长
    print(i)
'''
1
3
5
7
9
'''

for i in range(10,1,-2): # 反向步长
    print(i)
'''
10
8
6
4
2
'''
```

