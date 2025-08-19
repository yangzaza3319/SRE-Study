import random
choices =["石头","剪刀","布"]
user_wins=0
computer_wins=0
for i in range(1,4):
    print(f"第{i}局开始")

    user_choice = input("输入你的选择：")
    computer_choice = random.choice(choices)
    while user_choice == random.choices:
        print("输入无效，重新输入：")
        user_choice = input("输入你的选择：")

    computer_choice = random.choice(choices)
    print(f"你出了{user_choice}，电脑出了{computer_choice}")
    if user_choice == computer_choice:
        print("此局平局")
    elif (
            (user_choice == "石头" and computer_choice == "剪刀") or
            (user_choice == "剪刀" and computer_choice == "布") or
            (user_choice == "布" and computer_choice == "石头")
    ):
        user_wins+=1
        print("你赢了这局")
    else:
        computer_choice+=1
        print("你输了这局")
    if user_wins >=2:
        print("\n恭喜你，赢得了比赛！")
    elif computer_wins >=2:
        print("\n很遗憾，你输了比赛。")
        break
    if user_wins < 2 and computer_wins < 2:
        if user_wins > computer_wins:
            print("\n恭喜你，你赢了！")
        else:
            print("\n很遗憾，你输了。")