db = {}
with open("user.txt","r",encoding="utf-8")as file:
    data=file.readlines()
    for i in data:
        ret=i.strip().split("|")
        db[ret[0]]=ret[1]
        print(db)
while True:
    username = input("输入用户名：")
    if username in db:
      password = input("输入密码：")
      if password == db[username]:
          print("登录成功")
      else:
          print("密码错误登录失败")
    else:
     print("用户名不存在")
