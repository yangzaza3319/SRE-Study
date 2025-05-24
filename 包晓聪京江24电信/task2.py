def get_db():
    db = {}
    with open('work\\user.txt','r', encoding='utf-8') as f:
        data = f.readlines()
        for i in data:
            mon = i.strip().split("|")
            db[mon[0]] = mon[1]
    return db
def login(username, password):
    db = get_db()
    if username in db:
        if password == db[username]:
            print('登录成功')
            return True
        else:
            print('密码错误')
    else:
        print('用户名不存在')
def register(username, password):
    db = get_db()
    if username in db:
        print('用户名已存在')
    else:
        db[username] = password
        with open('work\\user.txt','a', encoding='utf-8') as f:
            f.write(f'{username}|{password}\n')
        print('注册成功')