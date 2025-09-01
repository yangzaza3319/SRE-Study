# 定义列表

fruits = ["apple","banana","watermelen"]
print(fruits)  # 输出 ['apple', 'banana', 'watermelen']

# 增加元素
# 1.在索引的位置去增加
fruits.insert(1,"kiwi")

# 2.在最末尾添加
fruits.append("orange")

# 3.用迭代的方法去添加
fruits.extend(['a','b','c'])

print(fruits) # 输出 ['apple', 'kiwi', 'banana', 'watermelen', 'orange', 'a', 'b', 'c']


# 删除元素

# 1.删除指定元素
fruits.remove("kivi")
print(fruits)
# 2.按照索引位置去删除
fruits.pop()  # 默认删除最后一个，可以加上索引，并且有返回值，返回值为删除后的元素
print(fruits)
fruits.pop(1)
print(fruits)

# 3.使用切片范围删除
del fruits[1:3]
print(fruits)   # 输出 ['apple', 'orange', 'a', 'b']

# 4.清空列表
fruits.clear()
print(fruits)  # 输出 []


# 5.删除列表
del fruits
print(fruits)  # 报错：fruits变量未被定义



# 修改元素
# 1.按照索引修改某个元素的值
city = ["上海"，"北京","悉尼","巴黎"]