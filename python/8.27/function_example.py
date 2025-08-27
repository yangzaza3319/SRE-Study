# 案例1 简单计算器的实现 
def calculate(operation, num1 , num2):
    """简单计算器实现"""
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "错误：除数不能为零！"
        return num1 / num2
    else:
        return "错误：未知操作！"

# 用户输入
user_operation = input("请输入操作（add, subtract, multiply, divide）: ")
user_num1 = float(input("请输入第一个数字: "))
user_num2 = float(input("请输入第二个数字: "))

# 调用函数
result = calculate(user_operation, user_num1, user_num2)
print(f"结果: {result}")


# 案例2 书籍入库管理

# add_book_simple.py

def add_book(book_id, *authors, **details):
    """
    添加书籍信息并打印
    """
    print(f"书籍编号：{book_id}")
    print(f"作者：{','.join(authors)}")
    for key, value in details.items():
        print(f"{key}:{value}")
    print("-----")

# 添加书籍
add_book(101, "明朝人士", "少不读三国，老不读水浒")
add_book(102, "刘亮程", "一个人的村庄，不变的童年记忆")
add_book("西游记", "吴承恩", year=1592, publisher="明代世德堂刻本", genre="神魔小说")

add_book("Python编程", "Guido van Rossum", year=1991, publisher="ABC Press")
add_book("机器学习导论", "Andrew Ng", year=2015, course="Online Course")
add_book("建筑设计图集", "Frank Lloyd Wright", year=1930, style="现代主义")