import time
import random


class Gamerole:
    def __init__(self, name, ad, hp):
        self.name = name
        self.ad = ad
        self.hp = hp

    def attack(self, p1):
        p1.hp -= self.ad
        print(f"{self.name}攻击{p1.name},{p1.name}掉了{self.ad}血,还剩{p1.hp}")

    def equip_weapon(self, wea):
        self.wea = wea
        wea.ad += self.ad
        wea.owner_name = self.name


class Weapon:
    def __init__(self, name, ad, owner_name=None):
        self.name = name
        self.owner_name = owner_name
        self.ad = ad

    def weapon_attack(self, p2):
        p2.hp = p2.hp - self.ad
        print(f"{self.owner_name}利用{self.name}攻击了{p2.name}，{p2.name}还剩{p2.hp}血")


sunwukong = Gamerole("孙悟空", 20, 500)
caocao = Gamerole("曹操", 20, 100)
anqila = Gamerole("安琪拉", 50, 80)

zhaoyun = Gamerole("赵云", 30, 450)
guanyu = Gamerole("关羽", 80, 200)
diaochan = Gamerole("貂蝉", 60, 150)

blue_list = [sunwukong, caocao, anqila]
red_list = [zhaoyun, guanyu, diaochan]

if __name__ == '__main__':
    print("游戏开始加载")
    # 打印加载进度
    for i in range(0, 101, 2):
        time.sleep(0.1)
        char_num = i // 2
        if i == 100:
            per_str = f"\r{i}% : {'*' * char_num}\n"
        else:
            per_str = f"\r{i}% : {'*' * char_num}"
        print(per_str, end='', flush=True)

    input("游戏加载完毕，输入任意字符开始！")

    # 输出阵营角色
    print("\n" + "蓝方阵营".center(20, '*'))
    for role in blue_list:
        print(role.name.center(20))
    print("\n" + "红方阵营".center(20, '*'))
    for role in red_list:
        print(role.name.center(20))

    # 游戏主循环
    while True:
        # 检查游戏结束条件
        if not blue_list:
            print("\n红方阵营胜利！！！")
            break
        if not red_list:
            print("\n蓝方阵营胜利！")
            break

        # 随机选择攻击角色
        idx1 = random.randint(0, len(blue_list) - 1)
        idx2 = random.randint(0, len(red_list) - 1)

        attacker = blue_list[idx1]
        defender = red_list[idx2]

        time.sleep(1)
        # 双方互相攻击
        attacker.attack(defender)
        time.sleep(1)
        defender.attack(attacker)

        # 检查角色是否阵亡
        if attacker.hp <= 0:
            print(f"\n{attacker.name}阵亡！")
            blue_list.remove(attacker)
        if defender.hp <= 0:
            print(f"\n{defender.name}阵亡！")
            red_list.remove(defender)