db = {}
with open("user.txt","r", encoding="utf-8") as f:
    data = f.readlines()
    print(data)
    for i in data:
        ret = i.strip().split("|")
        print(ret)
        db[ret[0]] = ret[1]
        print(db)

while True:
    username = input("请输入用户名：")

    if username in db:
        password = input("请输入密码：")
        if password ==db[username]:
            print("登录成功")
        else:
            print("密码错误登录失败")
    else:
        print("用户名不存在,请创建新用户")
        password = input("请输入密码：")
        db[username]=password
        print(f"{username}新用户创建成功啦")
        with open("user.txt", "a+", encoding="utf-8") as f:
            data1 = "%s|%s\n" % (username, password)
            f.write(data1)