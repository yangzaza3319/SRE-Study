import random
num=random.randint(1,100)
i=1
while i<4:
    i+=1
    num1=int(input("请输入数字："))
    if num1>num:
        print("猜大了")
    elif num1<num:
        print("猜小了")
    else:
        print("猜对了")
        break
if i==4:
    print("寄了")
    print("答案是：",num)