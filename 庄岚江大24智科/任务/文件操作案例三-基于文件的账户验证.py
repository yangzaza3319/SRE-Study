db={}
with open('user.txt','w',encoding='utf') as f:
    print("请注册")
    username=input("请输入用户名：")
    password=input("请输入密码：")
    inf=username+'|'+password
    f.write(inf)
with  open('user.txt','r',encoding='utf') as file:
    data=file.readlines()
    for i in data:
        ret=i.strip().split('|')
        print(ret)
        db[ret[0]]=ret[1]
        print(db)
while  True:
    username1=input("请输入用户名：")
    if username1 in db:
        passsword1=input("请输入密码：")
        if passsword1==db[username1]:
            print("登录成功")
            break
        else:
            for i in range(2):
                password1=input(f"密码错误，请重新输入密码（还有{2-i}次机会）：")
                if password1==db[username1]:
                    print("登录成功")
                    break
                if i==1:
                    print("密码错误三次，账号封禁")
            break
    else:
        print("用户名不存在")