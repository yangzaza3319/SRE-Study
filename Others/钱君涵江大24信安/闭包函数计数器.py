def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

# 创建一个计数器
my_counter = make_counter()

print(my_counter())  # 输出：1
print(my_counter())  # 输出：2
print(my_counter())  # 输出：3
