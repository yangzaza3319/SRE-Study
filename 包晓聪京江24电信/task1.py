with open('work\\user.txt', 'a',encoding='utf-8') as file:
content = input("注册用户名|密码：")
file.write(content + "\n")
print("用户信息已保存！")

db = {}
with open('work\\user.txt','r', encoding='utf-8') as f:
    data = f.readlines()
    for i in data:
        mon = i.strip().split("|")
        db[mon[0]] = mon[1]
        print(db)


max_try = 3
try_count = 0
while try_count < max_try:
    username = input('请输入用户名:')
    if username in db:
        password = input('请输入密码:')
        if password == db:
            print('登录成功')
            break
        else:
            print('密码错误')
            try_count += 1
    else:
        print('用户名不存在')
        try_count += 1