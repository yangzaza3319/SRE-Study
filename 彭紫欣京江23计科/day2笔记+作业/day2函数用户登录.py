# 初始化用户数据库和错误计数
db = {}
error_count = {}
try:
    # 读取用户信息文件
    with open("sql.txt", "r", encoding="utf-8") as f:
        for line in f:
            user_info = line.strip().split("|")
            if len(user_info) == 3:#长度为3说明记录了用户名，密码，错误次数
                username, password, count = user_info#将user_info列表中的元素依次赋值给变量
                db[username] = password
                error_count[username] = int(count)
            elif len(user_info) == 2:
                username, password = user_info#记录了用户名和密码
                db[username] = password
                error_count[username] = 0
except FileNotFoundError:
    # 若文件不存在则创建空文件
    open("sql.txt", "w", encoding="utf-8").close()
def update_file():
    # 更新用户信息文件
    with open("sql.txt", "w", encoding="utf-8") as f:
        for user, pwd in db.items():
            f.write(f"{user}|{pwd}|{error_count[user]}\n")


while True:
    choice = input("请选择操作（1. 登录，2. 注册，3. 退出）：")
    #登录
    if choice == "1":
        username = input("请输入用户名：")
        if username in db:
            if error_count[username] >= 3:
                print("该用户已被封号，请联系管理员解封。")
                continue#跳过本次循环，直接转到未到3次继续
            password = input("请输入密码：")
            if password == db[username]:
                error_count[username] = 0
                print("登录成功")
            else:
                error_count[username] += 1
                if error_count[username] >= 3:
                    print("密码错误次数达到3次，该用户已被封号。")
                else:
                    print(f"密码错误登录失败，你还可以尝试 {3 - error_count[username]} 次。")
            update_file()
        else:
            print("用户名不存在")
    #注册
    elif choice == "2":
        username = input("请输入要注册的用户名：")
        if username in db:
            if error_count[username] >= 3:
                print("该用户名已被封号，无法注册。")
            else:
                print("该用户名已存在，请选择其他用户名。")
        else:
            password = input("请输入要注册的密码：")
            db[username] = password
            error_count[username] = 0
            with open("sql.txt", "a", encoding="utf-8") as f:
                #a追加模式打开，数据会被添进文件，不会覆盖已有内容
                f.write(f"{username}|{password}|0\n")
            print("注册成功，请登录。")
    #退出
    elif choice == "3":
        break
    else:
        print("无效的选择，请重新输入。")

