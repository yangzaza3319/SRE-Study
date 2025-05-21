import random
# random产生随机值或者从给定值中随机选择
a = 1
a = int(input("是否进行猜数字：")) 

def guess_number(a):
    while a:
        x=int(input("请输入下界："))
        y=int(input("请输入上界："))
        random_number = random.randint(x, y)  # 生成用户指定范围内的随机整数
        # print(f"生成的随机整数是：{random_number}")
        print("猜数字游戏开始！")
        flag = 0  # 初始化计数器
        while a:
            print("你还有", 3 - flag, "次机会！")
            guess = int(input("请输入你的猜测: "))
            flag += 1  # 每次猜测后增加计数器
            if guess < random_number:
                print("太小了！再试一次。")
            elif guess > random_number:
                print("太大了！再试一次。")
            else:
                print("恭喜你，猜对了！")
                break  # 满足条件时停止程序
            if flag == 3:  # 当计数器达到3时停止程序
                print("很遗憾，你已经用完了所有机会！")
                break
        a = int(input("是否继续猜数字："))
    
guess_number(a)