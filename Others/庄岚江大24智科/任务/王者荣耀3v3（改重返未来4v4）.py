import time
import random
class Mystic:
    def __init__(self,name,ad,hp):
        self.name = name
        self.ad = ad
        self.hp = hp
    def attack(self,p1):
        p1.hp -= self.ad
        print("%s攻击了%s,%s掉了%s血，还剩%s血"%(self.name,p1.name,p1.name,self.ad,p1.hp))
    def equip_mystic_art(self,art):
        self.art = art
        art.ad+=self.ad
        art.owner_name = self.name
class Mystic_art:
    def __init__(self,name,ad,owner_name = None):
        self.name = name
        self.owner_name = owner_name
        self.ad = ad
    def art_attack(self,p2):
        p2.hp -= self.ad
        print("%s使用%s攻击了%s,%s还剩%s血"%(self.owner_name,self.name,p2.name,p2.name,p2.hp))
Aleph = Mystic("阿莱夫",100,1300)
Vouager =  Mystic("远旅",70,1500)
Garland =  Mystic("库伯花环",100,1200)
Cello =  Mystic("芭卡洛儿",80,1000)

Nana = Mystic("娜娜",120,1800)
Fiction = Mystic("虚构集",80,1200)
Child = Mystic("纸信圈儿",100,800)
Tutu = Mystic("图图石子",60,1000)

one_list  = [Aleph,Vouager,Garland,Cello]
two_list = [Nana,Fiction,Child,Tutu]

if  __name__ == '__main__':
    print("人工梦游准备...")
    for i in range(0, 101, 2):
        time.sleep(0.1)
        char_num = i // 2
        per_str = '\r%s%% : %s\n' % (i, '*' * char_num) \
            if i == 100 else '\r%s%% : %s' % (i, '*' * char_num)
        print(per_str, end='', flush=True)
    info = input("梦游仓准备完毕，输入任意字符开始！")
    print("一队".center(20,'*'))
    for i in one_list:
        print(i.name.center(20))
    print("二队".center(20,'*'))
    for i in two_list:
        print(i.name.center(20))
    while True:
        # 判断游戏结束的条件是某一方全部阵亡
        if len(one_list) == 0:
            print("二队胜利！！！")
            break
        if len(two_list) == 0:
            print("一队胜利！! !")
            break
        index1 = random.randint(0, len(one_list) - 1)
        index2 = random.randint(0, len(two_list) - 1)

        #  开始攻击
        time.sleep(0.5)
        role1 = one_list[index1]
        time.sleep(0.5)
        role2 = two_list[index2]
        time.sleep(0.5)
        role1.attack(role2)
        role2.attack(role1)
        # 判断是否有神秘学家阵亡
        if role1.hp <= 0:
            print("%s阵亡！" % role1.name)
            one_list.remove(role1)
        if role2.hp <= 0:
            print("%s阵亡！" % role2.name)
            two_list.remove(role2)