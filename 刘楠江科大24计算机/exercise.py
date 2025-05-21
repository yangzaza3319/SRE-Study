db = {}
count=0
with open("test.txt","r", encoding="utf-8") as f:
  data = f.readlines()
print(data)
for i in data:
       ret = i.strip().split("|")
       # ret = ["张三", "123"]
       print(ret)
       db[ret[0]] = ret[1]
        # db["张三"] = "123"
       print(db)

while True:
   username = input("请输入用户名：")

   if username in db:
       while count<3:
           password = input("请输入密码：")
           if password ==db[username]:
              print("登录成功")
              break
           else:
               print("密码错误登录失败")
               count += 1
               print("你还有" + str(3-count) + "次机会")
       if count>=3:
           print("你密码错误了3次，将封号")

   else:
       print("用户名不存在")
       new_username=input("请输入新用户名：")
       new_password=input("请输入新密码：")
       db[new_username]=new_password
       with open("test.txt", "a", encoding="utf-8") as f:
           f.write(new_username+"|"+new_password+"\n")
           print("注册成功")