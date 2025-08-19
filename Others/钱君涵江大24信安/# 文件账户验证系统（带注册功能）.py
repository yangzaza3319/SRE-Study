# 文件账户验证系统（带注册功能）

def register():
    username = input("请输入用户名进行注册: ")
    password = input("请输入密码: ")

    with open('users.txt', 'a', encoding='utf-8') as f:
        f.write(f"{username},{password}\n")

    print("✅ 注册成功！")


def login():
    username = input("请输入用户名进行登录: ")
    password = input("请输入密码: ")

    with open('users.txt', 'r', encoding='utf-8') as f:
        for line in f:
            stored_username, stored_password = line.strip().split(',')
            if stored_username == username and stored_password == password:
                print("✅ 登录成功！")
                return True

    print("❌ 登录失败，用户名或密码错误。")
    return False


def main():
    print("欢迎使用文件账户系统")
    while True:
        choice = input("请选择操作：[1] 注册 [2] 登录 [0] 退出: ")
        if choice == '1':
            register()
        elif choice == '2':
            if login():
                break  # 登录成功后退出循环
        elif choice == '0':
            print("已退出程序。")
            break
        else:
            print("无效选项，请重新输入。")

if __name__ == "__main__":
    main()
