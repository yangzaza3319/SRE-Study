db = {}
with open("sql.txt","r", encoding="utf-8") as f:
    data = f.readlines()
    print(data)
    for i in data:
        ret = i.strip().split("|")
        # ret = ["张三", "123"]
        print(ret)
        db[ret[0]] = ret[1]
        # db["张三"] = "123"
        print(db)

while True:
    username = input("请输入用户名：")

    if username in db:
        password = input("请输入密码：")
        if password == db[username]:
            print("登录成功")
        else:
            print("密码错误登录失败")
    else:
        print("用户名不存在")