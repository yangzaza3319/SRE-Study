def read_accounts():
    db = {}
    try:
        with open('sql.txt', 'r', encoding='utf-8') as f:
            data = f.readlines()
            for i in data:
                ret = i.strip().split('|')
                db[ret[0]] = ret[1]
    except FileNotFoundError:
        pass
    return db


def register(db):
    while True:
        username = input('请输入要注册的用户名: ')
        if username in db:
            print('该用户名已存在，请重新输入')
            continue
        password = input('请输入密码: ')
        confirm_password = input('请再次确认密码: ')
        if password != confirm_password:
            print('两次输入的密码不一致，请重新输入')
            continue
        db[username] = password
        with open('sql.txt', 'a', encoding='utf-8') as f:
            f.write(f'{username}|{password}\n')
        print('注册成功')
        break


def login(db):
    while True:
        username = input('请输入用户名: ')
        if username not in db:
            print('用户名不存在')
            continue
        password = input('请输入密码: ')
        if password == db[username]:
            print('登录成功')
            break
        else:
            print('密码错误，登录失败')


if __name__ == '__main__':
    account_db = read_accounts()
    operation = input('请选择操作，1为注册，2为登录: ')
    if operation == '1':
        register(account_db)
    elif operation == '2':
        login(account_db)
    else:
        print('无效的选择，请重新运行程序')
