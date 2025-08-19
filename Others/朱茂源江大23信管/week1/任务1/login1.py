db = {}
with open("user.txt","r", encoding="utf-8") as f:
    data = f.readlines()
    print(data)
    for i in data:
        ret = i.strip().split("|")
        # ret = ["张三", "123"]
        print(ret)
        db[ret[0]] = ret[1]
        # db["张三"] = "123"
        print(db)

import time

error_log = {}

while True:
    print("输入1: 注册\n")
    print("输入2: 登录\n")
    select = input("请选择登录或注册: ")

    if select == "1":
        print("欢迎注册")
        newuser = input("请输入新用户名: ")
        if newuser in db:
            print("用户名已存在，请重新注册")
            continue
        newpass = input("请输入密码: ")
        db[newuser] = newpass
        with open("user.txt", "a+", encoding="utf-8") as f:
            f.seek(0)  # 将文件指针移动到文件开头
            content = f.read()
            if content and not content.endswith("\n"):
                f.write("\n")
            f.write(newuser + "|" + newpass + "\n")
        print("注册成功")

    elif select == "2":
        username = input("请输入用户名: ")

        if username not in db:
            print("用户名不存在")
            continue

        # 检查是否处于封号状态
        if username in error_log:
            error_count, last_error_time = error_log[username]
            if error_count >= 3:
                elapsed_time = time.time() - last_error_time
                if elapsed_time < 60:
                    print(f"密码错误次数过多，账号已被锁定，剩余锁定时间: {60 - int(elapsed_time)}秒")
                    continue
                else:
                    # 锁定时间已过，重置错误次数
                    error_log[username] = (0, 0)

        password = input("请输入密码: ")
        if password == db[username]:
            print("登录成功")
            error_log.pop(username, None)
        else:
            print("密码错误登录失败")
            # 更新错误记录
            if username in error_log:
                error_count, last_error_time = error_log[username]
                error_log[username] = (error_count + 1, time.time())
            else:
                error_log[username] = (1, time.time())

    else:
        print("选项输入错误，请重新输入")