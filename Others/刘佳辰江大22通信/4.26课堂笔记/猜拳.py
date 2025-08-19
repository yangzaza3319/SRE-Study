import random
# random产生随机值或者从给定值中随机选择

# 可选择的选项
options = ["石头", "剪子", "布"]
player_wins=0
compulator_wins=0
print("欢迎来到石头剪子布游戏！")

while True:
    print("请从以下选项中选择：")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    # 玩家选择
    player_choice = int(input("请输入你的选择（1-3）：")) - 1
    # 计算机随机选择
    computer_choice = random.randint(0, 2)
    print(f"\n你选择了：{options[player_choice]}")
    print(f"计算机选择了：{options[computer_choice]}")
    # 判断胜负
    if player_choice == computer_choice:
        print("平局！")
    elif(player_choice == 0 and computer_choice == 1) or \
        (player_choice == 1 and computer_choice == 2) or \
        (player_choice == 2 and computer_choice == 0):
        player_wins+=1
        print("你赢了一局！")
    else:
        compulator_wins+=1
        print("你输了一局！")
        
    if (player_wins==3 and compulator_wins==0) or \
    (player_wins==2 and compulator_wins==1):
        print("你赢了！🎉")
        break
    elif (player_wins==0 and compulator_wins==3) or \
    (player_wins==1 and compulator_wins==2):
        print("你输了😢")
        break