import random

print('猜数字游戏开始')

# 生成一个0到100之间的随机数
num = random.randint(0, 100)

# 初始化猜错次数
attempts = 0

while attempts < 3:
    guess = int(input("您猜数字是什么？(输入0-100的数字):"))
    
    if guess < num:
        print("您猜小了")
    elif guess > num:
        print("您猜大了")
    else:
        print("您猜对了！")
        break  # 猜对了就退出循环
    
    attempts += 1  # 猜错次数加1

if attempts == 3 and guess != num:
    print(f"很遗憾，您已经猜错了3次，正确数字是 {num} 。")
