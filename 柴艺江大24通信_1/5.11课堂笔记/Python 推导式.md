## Python 推导式

###  列表推导式

列表推导式主要是用于按照我们指定的内容填充，生成一个新的列表

#### 例：

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

### 集合推导式

集合推导式用于生成一个新的集合。它的语法与列表推导式类似，但使用大括号 `{}`。

#### 例：

```python
# 生成平方数的集合
squares_set = {x ** 2 for x in range(10)}
print(squares_set)  # 输出: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# 生成唯一的字符集合
unique_chars = {char for char in "hello world"}
print(unique_chars)  # 输出: {'h', 'e', 'l', 'o', ' ', 'r', 'w', 'd'} #集合自动去重了
```

### 字典推导式

#### 例：

```python
# 生成平方数的字典
squares_dict = {x: x ** 2 for x in range(10)}
print(squares_dict)  # 输出: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# 生成字符及其 ascii 值的字典
ascii_dict = {char: ord(char) for char in "abc"}
print(ascii_dict)  # 输出: {'a': 97, 'b': 98, 'c': 99}
```

###  生成器表达式

把列表推导式的的`[]`换成`()`就变成了生成器表达式，相比于列表表达式，生成器表达式不会直接产生值，而是需要我们手动去迭代它

```python
gen_expr = (x ** 2 for x in range(5))
print(gen_expr)
for value in gen_expr:
    print(value)
```

