class Gamerole:
    def __init__(self,name,hp,ad,weap=0):
        self.name = name
        self.hp = hp
        self.ad = ad
        self.weap = weap
    def equipweap(self,weap):
        self.ad += weap.ad
    def mutual_attack(self,opponent):
        opponent.hp -= self.ad
        self.hp -= opponent.ad
        print("{}和{}互殴，{}掉了{}点血，{}掉了{}点血".format(self.name,opponent.name,self.name,opponent.ad,opponent.name,self.ad))
    def attack(self,opponent):
        opponent.hp -= self.ad
        print("{}攻击了{}，{}掉了{}点血".format(self.name,opponent.name,opponent.name,self.ad))
class Weapon:
    def __init__(self,name,ad):
        self.name = name
        self.ad = ad

    def provide_weap(self,owenner,oppent=None):
        self.owner = owenner
        self.owner.equipweap(self)
        print("{}装备了{}".format(self.owner.name,self.name))
        if oppent !=None:
            owenner.attack(oppent)

role1 = Gamerole("小明",100,10)
role2 = Gamerole("小红",100,20)
role1.mutual_attack(role2)
weap1 = Weapon("双节棍",10)
weap1.provide_weap(role2)
weap1.provide_weap(role1,role2)

