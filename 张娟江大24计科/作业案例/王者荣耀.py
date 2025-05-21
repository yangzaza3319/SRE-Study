import time
import random

class Gamerole:
    def __init__(self,name,hp,ad):
        self.name=name
        self.hp=hp
        self.ad=ad
    def attack(self,enemy):
        enemy.hp-=self.ad
        print("%s攻击了%s，%s掉了%s点血，剩余%s血"%(self.name,enemy.name,enemy.name,self.ad,enemy.hp))
    def equip_weapon(self,wea):
                    self.wea = wea
                    wea.ad += self.ad
                    wea.owner_name = self.name
                    print("%s装备了%s"%(self.name,wea.name))
class Weapon:
            def __init__(self,name,ad,owner_name=None):
                self.name=name
                self.ad=ad
                self.owner_name=owner_name
            def weapon_attack(self,enemy):
                    enemy.hp-=self.ad
                    print("%s攻击了%s，%s掉了%s点血，剩余%s血"%(self.owner_name,enemy.name,enemy.name,self.ad,enemy.hp))
sunwukong=Gamerole("孙悟空",1000,200)
dajia=Gamerole("妲己",800,150)
lan=Gamerole("澜",700,180)

zhaoyun = Gamerole("赵云", 800, 450)
guanyu = Gamerole("关羽", 700, 200)
diaochan = Gamerole("貂蝉", 900, 150)            
blue_list = [zhaoyun, guanyu, diaochan]
red_list = [sunwukong, dajia, lan]
if __name__=="__main__":
       print("游戏加载中")
       for i in range(0,101,2):
            time.sleep(0.1)
            num = i//2
            per_str = '\r%s%% : %s\n' % (i, '*' * num) \
            if i == 100 else '\r%s%% : %s' % (i, '*' *num)
            print(per_str, end='', flush=True)
       print("游戏开始,请做好准备")
       
       time.sleep(1)
       print("蓝方阵营".center(20,"*"))#center是字符串的一个方法，用来居中对齐，并指定字符填充
       for i in blue_list:
           print(i.name.center(20,"-"))
       print("红方阵营".center(20,"*"))
       for i in red_list:
           print(i.name.center(20,"-"))
       time.sleep(1)
       print("全军出击")
       while True:
            if len(blue_list)==0:
                 print("蓝方阵营死亡，红方胜利")
                 break
            if len(red_list)==0:
                 print("红方阵营死亡，蓝方胜利")
                 break  
            index1 = random.randint(0,len(blue_list)-1)
            index2 = random.randint(0,len(red_list)-1)
            blue_list[index1].attack(red_list[index2])
            red_list[index2].attack(blue_list[index1])  
            time.sleep(1)
            if red_list[index2].hp<=0:
                 print("%s死亡"%(red_list[index2].name))
                 red_list.pop(index2) #pop:索引，不指定则返回最后一个，remove：通过元素查找，从前往后第一个元素
                
            if blue_list[index1].hp<=0:
                 print("%s死亡"%(blue_list[index1].name))
                 blue_list.pop(index1)
                 
