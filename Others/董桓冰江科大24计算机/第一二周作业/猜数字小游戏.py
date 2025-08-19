print('猜数字游戏开始')
num = 54
a = 0
while True:
    guess = int(input("您猜数字是什么？(输入0-100的数字):"))
    a += 1
    if guess < num:
        print("您猜小了")
        continue
    if guess > num:
        print("您猜大了")
        continue
    if guess == num:
        print("您猜对了")
        break
    elif a == 3:
        print("您已猜三次，游戏结束")
    break