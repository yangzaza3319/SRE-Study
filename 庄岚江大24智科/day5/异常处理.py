#语法错误
#python编辑器会直接检测不通过
# print("hello world"
# SyntaxError: unexpected EOF while parsing

#逻辑错误
# print(1/0)
# ZeroDivisionError: division by zero



#异常处理
try:
    num = input("<<:")
    int(num)
except:
    print('你输入的是非数字')
finally:
    print('程序结束')

# 处理数据类型转换时异常ValueError

s1 = 'hello'
try:
    int(s1)
except ValueError as e:
    print(e)

# Output:
# invalid iteral for int() with base 10: 'hello'

"""
格式
try
    主逻辑
except
    异常处理
finally
    扫尾工作（不管异常是否发生，都会执行的语句）
"""

#捕获多分支异常
try:
    num = input("<<:")
    int(num)
except ValueError as e:
    print('你输入的是非数字')
except TypeError as e:
    print('你输入的是非数字')
finally:
    print('程序结束')

#Exception
try:
    num = input("<<:")
    int(num)
except Exception as e:#捕获所有异常
    print(e)

#主动抛出异常
try:
    raise ValueError('主动抛出异常')
except ValueError as e:
    print(e)

#自定义异常
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
try:
    raise MyError('自定义异常')
except MyError as e:
    print(e)
