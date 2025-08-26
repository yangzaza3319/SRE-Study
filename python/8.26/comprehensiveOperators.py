# comprehensive_operators.py
## python基本运算符演示

# --- 算术运算符 ---
print("1 + 1 =", 1 + 1)
print("5 - 2 =", 5 - 2)
print("10 / 2 =", 10 / 2)     # 浮点数
print("7 // 2 =", 7 // 2)     # 地板除
print("7 % 3 =", 7 % 3)       # 取模
print("2 ** 3 =", 2 ** 3)     # 幂运算

# --- 关系运算符 ---
print("5 == 5 is", 5 == 5)
print("1 != 1 is", 1 != 1)
print("3 > 2 is", 3 > 2)
print("5 < 9 is", 5 < 9)
print("3 >= 19 is", 3 >= 19)
print("45 <= 45 is", 45 <= 45)


# --- 逻辑运算符 ---
print("True and False is", True and False)
print("True or False is", True or False)
print("not True is", not True)


# --- 赋值运算符 ---
x = 5
print(x) # 输出 5 

x += 7  # x = x + 7
print("x += 7 -> x =", x)

x -= 6  # x = x - 6
print("x -= 6 -> x =", x)

x *= 5  # x = x * 5
print("x *= 5 -> x =", x)

x /= 3  # x = x / 3
print("x /= 3 -> x =", x)

x //= 2 # x = x // 2
print("x //= 2 -> x =", x)

x %= 5  # x = x % 5
print("x %= 5 -> x =", x)

x = 2
x **= 3 # x = x ** 3
print("x **= 3 -> x =", x)

# --- 位运算符 ---
a = 5  # 二进制: 101
b = 3  # 二进制: 011
print(f"a = {a} (二进制: {bin(a)})")
print(f"b = {b} (二进制: {bin(b)})")

print(f"{a} & {b} =", a & b)  # 101 & 011 = 001 -> 1
print(f"{a} | {b} =", a | b)  # 101 | 011 = 111 -> 7
print(f"{a} ^ {b} =", a ^ b)  # 101 ^ 011 = 110 -> 6
print(f"~{a} =", ~a)          # 按位取反
print(f"{a} << 1 =", a << 1)  # 左移1位: 1010 -> 10
print(f"{a} >> 1 =", a >> 1)  # 右移1位: 010 -> 2
