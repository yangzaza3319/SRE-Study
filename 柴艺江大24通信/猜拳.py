import random
a=1
pla_so=0
com_so=0
op=(['剪刀','石头','布'])
print("你的选择有")
for i,j in enumerate(op):
    print(i,j)
def game():
    global a
    global pla_so
    global com_so
    com=random.randint(0,2)
    pla=int(input("请输入你的选择(在 1 2 3 内选择)："))-1
    print(f"你的选择是{op[pla]},电脑的选择是{op[com]}")
    if pla==com:
        print('平局')
        print(f"现在比分是{pla_so}:{com_so}")

    elif (pla==2 and com==1) or (pla==1 and com==0)  or (pla==0 and com==2):
        print('你赢了一局')
        a+=1
        pla_so += 1
        print(f"现在比分是{pla_so}:{com_so}")
    else:
        print('你输了一局')
        a+=1
        com_so += 1
        print(f"现在比分是{pla_so}:{com_so}")

while a<4:
   game()
else:
    if pla_so>com_so:
        print(f"你赢了，比分是{pla_so}:{com_so}")
    else:
        print(f"你输了，比分是{pla_so}:{com_so}")