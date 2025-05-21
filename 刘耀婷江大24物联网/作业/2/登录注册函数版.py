import os


#  从文件读取用户数据函数
def load_users():
    if os.path.exists('user.txt'):  # 检查数据库文件是否存在
        with open('user.txt', 'r', encoding='utf-8') as f:
            result = {}  # 初始化结果字典
            for line in f:
                # 去除行末换行符并按"|"分割
                parts = line.strip().split("|")
                # 将分割后的键值对添加到字典
                result[parts[0]] = parts[1]
            return result  # 返回生成的字典 # 将每行按 | 分割为 [用户名, 密码] # 转换为字典格式


#  将内存数据写入文件函数
def save_users(users):
    with open('user.txt', "w", encoding="utf-8") as f:
        for username, password in users.items():  # 遍历字典，返回键值对
            f.write(f"{username}|{password}\n")  # 按 用户名|密码\n 格式写入文件


# 1. 加载已有用户数据
users = load_users()

# 2. 主循环 - 持续显示菜单并处理用户选择
while True:
    # 菜单界面
    print("\n=== 账户系统 ===")
    print("1. 登录")
    print("2. 注册")
    print("3. 退出")
    # 获取用户选择
    choice = input("请选择操作: ")
    # 登录
    if choice == "1":
        username = input("用户名: ")
        password = input("密码: ")
        # 使用字典的 get 方法获取用户密码（不存在时返回 None）
        if users.get(username) == password:
            print("登录成功!")
        else:
            print("用户名或密码错误")
    #  注册
    elif choice == "2":
        username = input("注册用户名: ")
        # 检查用户名是否已存在
        if username in users:
            print("用户名已存在!")
            # 跳过本次循环剩余代码，直接开始下一次循环
            continue
        password = input("注册密码: ")
        # 添加新用户到内存
        users[username] = password
        # 保存到文件
        save_users(users)
        print("注册成功!")
    # 结束程序
    else:
        break
