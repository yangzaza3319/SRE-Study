# for循环遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

"""
输出
apple
banana
cherry
"""

# 遍历字符串
words = "wuyanzu"
for i in words:
    print(i)

"""
输出 
w
u
y
a
n
z
u
"""

#### 枚举法（enumerate）
> 利用枚举获得可迭代/可遍历对象的索引和值

li = ['甲','乙','丙','丁']
for i in enumerate(li): # 不指定开始索引的值，则默认从0开始索引
    print(i)  
    """
    输出
    (0, '甲')
    (1, '乙')
    (2, '丙')
    (3, '丁')
    """
for index,value in enumerate(li): # 不指定开始索引的值，则默认从0开始索引
    print(index,value)
    """
    输出
    0 甲
    1 乙
    2 丙
    3 丁
    """
for index,value in enumerate(li,100): # 指定从100开始索引
    print(index,value)

# range--指定范围，生成指定数字
for i in range(1,10):
    print(i)
print("++++++++++")
for i in range(1,10,2):
    print(i)
print("++++++++++")
for i in range(10,1,-2):
    print(i)
"""
输出
1
2
3
4
5
6
7
8
9
++++++++++
1
3
5
7
9
++++++++++
10
8
6
4
2
"""