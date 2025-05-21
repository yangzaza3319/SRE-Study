import random
print('猜数字游戏开始')
# 随机生成一个 0 到 100 之间的数字
num = random.randint(0, 100)
# 初始化猜测次数
guess_count = 0
while guess_count < 3:
        guess = int(input("您猜数字是什么？(输入 0 - 100 的数字):"))
        if guess < num:
            print("您猜小了")
        elif guess > num:
            print("您猜大了")
        else:
            print("您猜对了！")
            break
        guess_count += 1
# 检查是否达到最大猜测次数
if guess_count == 3:
    print(f"很遗憾，您已经猜错三次，游戏结束，正确答案是 {num}。")
