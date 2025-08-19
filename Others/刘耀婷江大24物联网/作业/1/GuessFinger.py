import random
# 可选择的选项
options = ["石头", "剪子", "布"]
print("欢迎来到三局两胜制石头剪子布游戏！")
player_score = 0
computer_score = 0
# 进行三局两胜的游戏
while player_score < 2 and computer_score < 2:
    print("请从以下选项中选择：")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
        # 玩家选择
        player_choice = int(input("请输入你的选择（1 - 3）：")) - 1
        # 计算机随机选择
        computer_choice = random.randint(0, 2)

        print(f"\n你选择了：{options[player_choice]}")
        print(f"计算机选择了：{options[computer_choice]}")
        # 判断胜负
        if player_choice == computer_choice:
            print("平局！此局无效，重新开始。")
            # continue
        elif (player_choice == 0 and computer_choice == 1) or \
                (player_choice == 1 and computer_choice == 2) or \
                (player_choice == 2 and computer_choice == 0):
            print("你赢了这一局！🎉")
            player_score += 1
        else:
            print("你输了这一局！😢")
            computer_score += 1

        print(f"当前比分：你 {player_score} - {computer_score} 计算机\n")
# 宣布最终结果
if player_score > computer_score:
    print("恭喜你，你在三局两胜的游戏中获胜啦！🎉")
else:
    print("很遗憾，你在三局两胜的游戏中输了。😢")
