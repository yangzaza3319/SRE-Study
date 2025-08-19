import time
import random


class GameRole:
    def __init__(self, name, hp, ad, wea=None):
        self.name = name
        self.hp = hp
        self.ad = ad
        self.wea = wea

    def attack(self, enemy):
        enemy.hp -= self.ad
        print(f'{self.name}攻击了{enemy.name}，造成了{self.ad}点伤害，{enemy.name}的剩余血量为{enemy.hp}')

    def equip_weapon(self,weapon):
        self.wea = weapon
        self.ad = weapon.effect(self.ad)
        weapon.owner = self.name

class Weapon:
    def __init__(self,name,effect,owner = None):
        self.name = name
        self.effect = effect
        self.owner = owner

yao = GameRole('曜',1500,120)
yuanliu = GameRole('元流',2000,120)
kai = GameRole('铠',1800,150)
sunshangxiang = GameRole('孙尚香',1200,180)
yixing = GameRole('奕星',1400,150)
shaosiyuan = GameRole('少司缘',1800,150)


tiejian1 = Weapon('铁剑',lambda x:x+50)
tiejian2 = Weapon('铁剑',lambda x:x+50)
tiejian3 = Weapon('铁剑',lambda x:x+50)
bishou  = Weapon('匕首',lambda x:x*1.25)
fadian  = Weapon('法典',lambda x:x*1.3)
baoshi  = Weapon('宝石',lambda x:x*1.15)

yao.equip_weapon(tiejian1)
yuanliu.equip_weapon(tiejian2)
kai.equip_weapon(tiejian3)
sunshangxiang.equip_weapon(bishou)
yixing.equip_weapon(fadian)
shaosiyuan.equip_weapon(baoshi)

blue_list = list(random.sample([yao,yuanliu,kai,sunshangxiang,yixing,shaosiyuan],3))
red_list = list({yao,yuanliu,kai,sunshangxiang,yixing,shaosiyuan}-set(blue_list))

print('游戏开始加载')
for i in range(0, 101, 2):
    time.sleep(0.1)
    char_num =  i//2
    line = f'\r{i}% :' + '-'*char_num + '\n' if i==100 else f'\r{i}% :' + '-' * char_num
    print(line, end='', flush=True)

# 打印一个进度条

info = input('游戏加载完毕，输入任一字符开始游戏: ')
print('蓝方阵营'.center(20,'*'))
for i in blue_list:
    print(i.name.center(20,'-'))
print('红方阵营'.center(20,'*'))
for i in red_list:
    print(i.name.center(20,'-'))


a = 1
while True:
    if len(blue_list) == 0:
        print('红方赢')
        break
    if len(red_list) == 0:
        print('蓝方赢')
        break
    print(f'这是第{a}回合')
    a += 1




    r_p = random.choice(red_list)
    b_p = random.choice(blue_list)

    r_p.attack(b_p)
    time.sleep(1)
    if b_p.hp <= 0:
        print(f'{b_p.name}死亡')
        blue_list.remove(b_p)
    else:
        b_p.attack(r_p)
        if r_p.hp <= 0:
            print(f'{r_p.name}死亡')
            red_list.remove(r_p)


# 由于红方先手 红方胜率远大于蓝方胜率




