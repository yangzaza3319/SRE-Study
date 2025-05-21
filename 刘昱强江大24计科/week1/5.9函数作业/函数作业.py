def initialize_user_file():
    """初始化用户文件，如果不存在则创建并添加默认用户"""
    a = open('user.txt', 'w', encoding='utf-8')
    a.write("张三|123456")
    a.close()


def load_users_to_dict():
    """从文件加载用户数据到字典"""
    db = {}
    with open("user.txt", "r", encoding="utf-8") as f:
        data = f.readlines()
        for i in data:
            ret = i.strip().split("|")
            db[ret[0]] = ret[1]
    return db


def create_new_account():
    """创建新账户并写入文件"""
    tempname = input("请输入姓名:")
    tempkey = input("请输入密码:")
    temp_key = input("请确认密码:")
    if tempkey == temp_key:
        with open('user.txt', 'a', encoding='utf-8') as u:
            u.write(f"\n{tempname}|{tempkey}")
        return True
    else:
        print("密码不匹配")
        return False


def login(db, count=0):
    """用户登录验证"""
    while count < 3:
        username = input("请输入用户名：")
        if username in db:
            password = input("请输入密码：")
            if password == db[username]:
                print("登录成功")
                return True
            else:
                print("密码错误登录失败")
                count += 1
        else:
            print("用户名不存在")
            break
    if count == 3:
        print("连续输错三次密码，账户已锁定")
    return False


def main():
    # 初始化用户文件
    initialize_user_file()

    # 加载用户数据
    db = load_users_to_dict()

    # 询问是否创建新账户
    ios = input("是否创建新的账户？")
    while ios == "是":
        if create_new_account():
            ios = "否"
        else:
            ios = input("密码不匹配，是否重新创建:")

    # 重新加载更新后的用户数据
    db = load_users_to_dict()

    # 登录验证
    login(db)


if __name__ == "__main__":
    main()