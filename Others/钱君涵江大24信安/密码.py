db = {}
lock_db = {}

# 从文件中读取用户名和密码
with open("sql.txt", "r", encoding="utf-8") as f:
    data = f.readlines()
    for line in data:
        ret = line.strip().split("|")
        db[ret[0]] = ret[1]

# 登录验证
while True:
    username = input("请输入用户名: ")

    # 检查是否被封号
    if lock_db.get(username, 0) >= 3:
        print("⚠️ 账号已被锁定，请联系管理员！")
        continue

    if username in db:
        password = input("请输入密码: ")
        if password == db[username]:
            print("✅ 登录成功")
            break
        else:
            lock_db[username] = lock_db.get(username, 0) + 1
            print(f"❌ 密码错误（{lock_db[username]}次）")
            if lock_db[username] >= 3:
                print("⚠️ 密码错误3次，账号已被锁定！")
    else:
        print("❌ 用户名不存在")
