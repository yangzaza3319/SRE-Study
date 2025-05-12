db={}
def register():
    name=input('请输入你的用户名：')
    password=input('请输入你的密码：')

    with open('user.txt','a',encoding='utf-8') as a_f:
        a_f.write(f'{name}|{password}\n')
    print('注册成功')


def enter():
    with open('user.txt','r',encoding='utf-8') as r_f:
        l=r_f.readlines()
        for i in l:
            i=i.strip('\n').split('|')
            db[i[0]]=i[1]
        name=input('请输入你的用户名：')
        if name not in db:
            print('用户不存在')
        else:
            password=input('请输入你的密码：')
            if password==db[name]:
                print('登陆成功')
            else:
                print('密码错误')

a=input('请输入1注册，2登陆：')
if a=='1':
    register()
elif a!='2':
    print('输入错误')
enter()



