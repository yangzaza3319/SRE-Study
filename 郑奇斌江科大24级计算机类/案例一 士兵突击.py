class Gun:
    def __init__(self,model):
        self.model=model
        self.bullet_count=0
    def add_bullet(self,count):
        self.bullet_count+=count
    def shoot(self):
        if self.bullet_count<=0:
            print("没有子弹了")
            return
        self.bullet_count-=1
        print(f"{self.model}发射子弹{self.bullet_count}突突突")
ak47=Gun("ak47")
ak47.add_bullet(50)
ak47.shoot()
class Soldier:
    def __init__(self,name,gun=None):
        self.name=name
        self.gun=gun
    def fire(self):
        if self.gun is None:
            print(f"{self.name}还没有枪")
        else:
            print(f"冲啊{self.name}")
            if self.gun.bullet_count<=0:
                print("没弹夹了，快换弹夹")
                self.gun.add_bullet(50)
            self.gun.shoot()
xusanduo=Soldier("许三多",ak47)
xusanduo.fire()
