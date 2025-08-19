db = {}  # 初始化数据库，此为字典,当前为空
lockout_db = {}  # 存储用户锁定状态和错误次数

# 从文件加载用户数据，到字典中
with open('user.txt', 'r', encoding='utf-8') as file:
    for i in file:
        ret = i.strip().split('|')
        db[ret[0]] = ret[1]

# 从文件加载锁定状态数据（如果存在）
try:
    with open('lockout.txt', 'r', encoding='utf-8') as lock_file:
        for line in lock_file:
            parts = line.strip().split('|')
            username = parts[0]
            attempts = int(parts[1])
            lockout_db[username] = attempts
except FileNotFoundError:
    pass

while True:
    username = input("请输入用户名：")

    # 检查用户是否被锁定
    if username in lockout_db and lockout_db[username] >= 3:
        print("账号已被锁定，请联系管理员解锁")
        continue

    if username in db:
        mi_ma = input("请输入密码：")
        if mi_ma == db[username]:
            # 重置错误计数
            if username in lockout_db:
                del lockout_db[username]
            # 保存更新后的锁定状态
            with open('lockout.txt', 'w', encoding='utf-8') as lock_file:
                for user, attempts in lockout_db.items():
                    lock_file.write(f"{user}|{attempts}\n")
            print("登录成功")
            break
        else:
            # 增加错误计数
            if username in lockout_db:
                lockout_db[username] += 1
            else:
                lockout_db[username] = 1
            # 保存更新后的锁定状态
            with open('lockout.txt', 'w', encoding='utf-8') as lock_file:
                for user, attempts in lockout_db.items():
                    lock_file.write(f"{user}|{attempts}\n")
            # 检查是否达到锁定次数
            if lockout_db[username] >= 3:
                print("密码错误次数过多，账号已被锁定")
            else:
                print(f"密码错误，您还有{3 - lockout_db[username]}次尝试机会")
    else:
        print("用户不存在")