# 示例1: 生成0～10的一个列表
list = [ i for i in range(0,10)]
print(list)
# 输出 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 示例2: 生成1～10的平方数的列表
squares = [x ** 2 for x in range(1,10)]
print(squares)
# 输出 [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 示例3: 生成偶数的列表
even_numbers = [x for x in range(0,21) if x % 2 == 0]
print(even_numbers)  # 输出 [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 推导式案例1. 找到嵌套列表中名字含有两个及以上`a`的所有名字
fruits = [['peach','lemon','pear','avocado','cantaloupe','banana','grape'],
          ['raisins','plum','apricot','nectarine','orange','papaya']]

print([name for list in fruits for name in list if name.count('a') >= 2])


# 推导式案例2. 找到30以内所有能被3整除的数

mutiples = [i for i in range(30) if i % 3 == 0]
print(mutiples)   # 输出 [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]