import random
options = ['石头', '剪刀', '布']
print("请从以下选项中选择：")
for i,option in enumerate(options):
    print(f"{i+1}.{option}")
    player_count = 0
    computer_count = 0
for j in range(3):
    player_choice = int(input("请输入你的选择："))-1
    computer_choice = random.randint(0, 2)
    print(f"你选择了{options[player_choice]}，计算机选择了{options[computer_choice]}")
    if player_choice == computer_choice:
        print("平局！")
    elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
        computer_count += 1
    else:
        player_count += 1
print(f"{player_count}:{computer_count}")
if player_count > computer_count:
    print("恭喜你，你赢了！")
elif player_count==computer_count:
    print("平局，请重新开始！")
else:
    print("计算机赢了，再接再励！")