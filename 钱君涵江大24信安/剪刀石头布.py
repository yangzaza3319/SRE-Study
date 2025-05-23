import random

# 可选择的选项
options = ["石头", "剪子", "布"]

print("欢迎来到石头剪子布游戏（三局两胜）！")

# 玩家和计算机的胜局数
player_wins = 0
computer_wins = 0
round_num = 1

while player_wins < 2 and computer_wins < 2 and (player_wins + computer_wins) < 3:
    print(f"\n--- 第 {round_num} 局 ---")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    try:
        player_choice = int(input("请输入你的选择（1-3）：")) - 1
        if player_choice not in [0, 1, 2]:
            print("无效输入，请输入1、2或3。")
            continue
    except ValueError:
        print("输入必须是数字！")
        continue

    computer_choice = random.randint(0, 2)

    print(f"你选择了：{options[player_choice]}")
    print(f"计算机选择了：{options[computer_choice]}")

    # 判断胜负
    if player_choice == computer_choice:
        print("这一局是平局！")
    elif (player_choice == 0 and computer_choice == 1) or \
         (player_choice == 1 and computer_choice == 2) or \
         (player_choice == 2 and computer_choice == 0):
        print("你赢了这一局！🎉")
        player_wins += 1
    else:
        print("你输了这一局！😢")
        computer_wins += 1

    print(f"当前比分：你 {player_wins} - {computer_wins} 计算机")
    round_num += 1

# 输出最终结果
print("\n游戏结束！")
if player_wins > computer_wins:
    print("🎉 恭喜你，赢得了比赛！（三局两胜）")
else:
    print("😢 很遗憾，计算机赢得了比赛。")
