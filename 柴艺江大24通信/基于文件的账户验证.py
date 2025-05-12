db={}
b=input("您是否已有账号(是或否)")
if b=='否':
    print('请先注册账号')
    with open('sql.txt','a',encoding='utf-8') as append_f:
        append_f.write(input("请输入您的用户名："))
        append_f.write('|')
        password1=input('请设置您的密码：')
        append_f.write(password1)
        while True:
            password2=input('请确认您的密码：')
            if password1==password2:
                break
            else:
                print('密码不一致，请重新确认密码')
        print('注册成功')
with open('sql.txt','r',encoding='utf-8') as file:
    li=file.readlines()
    for i in li:
        i=i.strip('\n').split('|')
        db[i[0]]=i[1]
a=0
name=input('请输入用户名：')
if name in db:
    while a<3:
        password = input('请输入密码：')
        if password==db[name]:
            print("登陆成功")
            break
        else:
            a+=1
            print(f'密码错误,请重新输入,您还有{3-a}次机会')
    else:
        print("您被封号了")
else:
    print('用户不存在')
