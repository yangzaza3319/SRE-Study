import random

options = ['石头', '剪刀', '布']
print('欢迎来到石头剪刀布游戏！')

player_wins = 0
computer_wins = 0
while player_wins < 2 and computer_wins < 2:
    print('请从以下选项中选择：')
    for i, option in enumerate(options):
        print(f'{i + 1}、{option}')
    player_choice = int(input('请输入你的选择(1 - 3): ')) - 1
    computer_choice = random.randint(0, 2)

    print(f'\n你选择了：{options[player_choice]}')
    print(f'计算机选择了：{options[computer_choice]}')

    if player_choice == computer_choice:
        print('平局！')
    elif (player_choice == 0 and computer_choice == 2) or \
         (player_choice == 1 and computer_choice == 0) or \
         (player_choice == 2 and computer_choice == 1):
        player_wins += 1
        print('你赢了这一局！')
    else:
        computer_wins += 1
        print('你输了这一局！')

if player_wins == 2:
    print('你赢了')
else:
    print('你输了')