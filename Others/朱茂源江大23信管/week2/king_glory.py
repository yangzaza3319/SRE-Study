import time
import random
class Gamerole:
    def __init__(self,name,ad,hp):
        self.name = name
        self.ad = ad
        self.hp = hp

    def attack(self,p1):
        p1.hp -= self.ad
        print('%s攻击%s,%s掉了%s血,还剩%s'%(self.name,p1.name,p1.name,self.ad,p1.hp))

    def equip_weapon(self,wea):
        self.wea = wea
        wea.ad += self.ad
        wea.owner_name = self.name

class Weapon:
    def __init__(self,name,ad,owner_name = None):
        self.name = name
        self.owner_name = owner_name
        self.ad = ad
    def weapon_attack(self,p2):
        p2.hp = p2.hp - self.ad
        print('%s利用%s攻击了%s，%s还剩%s血'%(self.owner_name,self.name,p2.name,p2.name,p2.hp))

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
    # 打印一个菜单
    for i in range(0, 101, 2):
        time.sleep(0.1)
        char_num = i // 2
        per_str = '\r%s%% : %s\n' % (i, '*' * char_num) \
            if i == 100 else '\r%s%% : %s' % (i, '*' * char_num)
        print(per_str, end='', flush=True)

    info = input("游戏加载完毕，输入任意字符开始！")
    # 输出东邪吸毒阵营里的任务角色
    print("蓝方阵营".center(20, '*'))
    for i in blue_list:
        print(i.name.center(20))
    print("红方阵营".center(20, '*'))
    for i in red_list:
        print(i.name.center(20))

    while True:
        # 判断游戏结束的条件是某一方全部阵亡
        if len(blue_list) == 0:
            print("红方阵营胜利！！！")
            break
        if  len(red_list) == 0:
            print("蓝方阵营胜利！")
            break


        # 游戏逻辑，每次随机选择一名角色出击
        index1 = random.randint(0, len(blue_list) - 1)
        index2 = random.randint(0, len(red_list) - 1)

        # 开始攻击
        time.sleep(1)
        role1 = blue_list[index1]
        time.sleep(1)
        role2 = red_list[index2]
        time.sleep(1)
        role1.attack(role2)
        role2.attack(role1)

        # 判断是否有英雄阵亡
        if role1.hp <= 0:
            print("%s阵亡！" % role1.name)
            blue_list.remove(role1)
        if role2.hp <= 0:
            print("%s阵亡！" % role2.name)
            red_list.remove(role2)