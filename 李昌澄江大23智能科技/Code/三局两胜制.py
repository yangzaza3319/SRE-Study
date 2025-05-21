import random
# random产生随机值或者从给定值中随机选择

# 可选择的选项
options = ["石头", "剪子", "布"]

print("欢迎来到石头剪子布游戏！")
print("请从以下选项中选择：")
for i, option in enumerate(options):
    print(f"{i + 1}. {option}")

a = 0
b = 0
while True:
    # 玩家选择
    if (a ==3 and b == 0) or (a ==2 and b == 1):
        print(f"你赢了！🎉比分{a}:{b}")
        break
    elif (a ==0 and b == 3) or (a ==1 and b == 2):
        print(f"电脑赢了！🎉比分{a}:{b}")
        break

    player_choice = int(input("请输入你的选择（1-3）：")) - 1

    # 计算机随机选择
    computer_choice = random.randint(0, 2)

    print(f"\n你选择了：{options[player_choice]}")
    print(f"计算机选择了：{options[computer_choice]}")

    # 单局判断胜负
    if player_choice == computer_choice:
        print("平局！")
    elif (player_choice == 0 and computer_choice == 1) or \
         (player_choice == 1 and computer_choice == 2) or \
         (player_choice == 2 and computer_choice == 0):
        a += 1
        print(f"======你得到{a}分！🎉======")

    else:
        b += 1
        print(f"======电脑得到{b}分！🎉======")