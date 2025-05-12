import random
num=random.randint(1,101)
count=1
while count<4:
    num1 = int(input("请输入你猜的数字:"))
    if num1==num:
        print('恭喜你猜对了')
        print(f'一共猜了{count}次')
    elif num1<num:
        print('猜小了')
        print(f'一共猜了{count}次')
    else:
        print('猜大了')
        print(f'一共猜了{count}次')
    count+=1
else:
    print('你输了，游戏结束')