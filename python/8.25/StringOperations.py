# 字符串操作示例

words = "beautiful is better than ugly."

##  字符串的基本操作
print(words)
print(words.capitalize())   # 首字母大写
print(words.swapcase())     # 大小写翻转
print(words.title())        # 每个单词的首字母大写

## 内容居中，宽度为50，填充字符为*
print(words.center(50, '*'))


## 统计子字符串出现的次数
print(words.count("b"))          # 统计 b 出现的次数


## 开头结尾判断
print(words.startswith("b"))     # 判断是否以 b 开头，结果为true
print(words.endswith("y."))      # 判断是否以 y. 结尾，结果为true

## 查找子字符串元素是否存在
print(words.find("is"))          # 查找 is 的索引位置，结果为10
print(words.index("than"))       # 查找 than 的索引位置，结果为20