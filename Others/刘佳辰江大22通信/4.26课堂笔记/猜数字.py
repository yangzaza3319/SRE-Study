import random
print('猜数字游戏开始')
num = random.randint(0,100)
print(num)
i=0
while i<3:
    i+=1
    guess = int(input("您猜数字是什么？(输入0-100的数字):"))
    if guess < num:
         print("您猜小了")
         continue    # 继续循环
    elif guess > num:
         print("您猜大了")
         continue
    else :
         print("您猜对了！")
    break   # 退出循环
