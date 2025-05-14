a = open('user.txt', 'w', encoding='utf-8')
a.write("张三|123456")
a.close()
db = {}
with open("user.txt", "r", encoding="utf-8") as f:
    data = f.readlines()
    for i in data:
        ret = i.strip().split("|")
        db[ret[0]] = ret[1]

count = 0
ios = input("是否创建新的账户？")
while ios == "是":
    tempname = input("请输入姓名:")
    tempkey = input("请输入密码:")
    temp_key = input("请确认密码:")
    if tempkey== temp_key:
        with open('user.txt', 'a', encoding='utf-8') as u:
            u.write(f"\n{tempname}|{tempkey}")
            ios = "否"
    else:
        ios = "否"
        ios = input("密码不匹配，是否重新创建:")

with open("user.txt", "r", encoding="utf-8") as f:
    data = f.readlines()
    for i in data:
        ret = i.strip().split("|")
        db[ret[0]] = ret[1]

while count < 3:
    username = input("请输入用户名：")

    if username in db:
        password = input("请输入密码：")
        if password == db[username]:
            print("登录成功")
            break
        else:
            print("密码错误登录失败")
            count += 1
    else:
        print("用户名不存在")
        break
if count == 3:
    print("连续输错三次密码，账户已锁定")
