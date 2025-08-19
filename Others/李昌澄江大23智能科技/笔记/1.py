# dic = {'name':'nls','age':18,'job':'teacher'}

# 1. 删除指定的键,并且返回对应的值
# name = dic.pop('job')
# hobby = dic.pop('hobby','查无此项')        # 可以在后面加上一个异常处理，如果key不存在，就输出后面的内容
# print(dic)
# print(name)
# print(hobby)

# Output:
# {'name': 'nls', 'age': 18}
# teacher
# 查无此项

# 2. 使用del关键字删除指定的键值对
# del dic['name']

# # 3. 删除最后插入的键值对
# dic_pop = dic.popitem()
# print(dic_pop)

# # 4. 清空字典
# dic.clear()
# print(dic)

# # Output: {}

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

print(set1 ^ set2)
print(set1.symmetric_difference(set2))