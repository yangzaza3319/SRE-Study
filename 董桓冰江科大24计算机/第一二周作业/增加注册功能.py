def read_accounts():
    """读取文件中的账户信息"""
    db = {}
    try:
        with open("sql.txt", "r", encoding="utf-8") as f:
            data = f.readlines()
            for i in data:
                ret = i.strip().split("|")
                db[ret[0]] = ret[1]
    except FileNotFoundError:
        pass
    return db


def register(db):
    """注册功能"""
    while True:
        new_username = input("请输入要注册的用户名: ")
        if new_username in db:
            print("该用户名已存在，请重新输入！")
            continue
        new_password = input("请输入密码: ")
        confirm_password = input("请再次确认密码: ")
        if new_password != confirm_password:
            print("两次输入的密码不一致，请重新输入！")
            continue
        db[new_username] = new_password
        with open("sql.txt", "a", encoding="utf-8") as f:
            f.write(f"{new_username}|{new_password}\n")
        print("注册成功！")
        break


def login(db):
    """登录功能"""
    while True:
        username = input("请输入用户名: ")
        if username not in db:
            print("用户名不存在")
            continue
        password = input("请输入密码: ")
        if password == db[username]:
            print("登录成功")
            break
        else:
            print("密码错误登录失败")


if __name__ == "__main__":
    accounts = read_accounts()
    choice = input("请选择操作，1为注册，2为登录: ")
    if choice == "1":
        register(accounts)
    elif choice == "2":
        login(accounts)
    else:
        print("无效的选择，请重新运行程序")