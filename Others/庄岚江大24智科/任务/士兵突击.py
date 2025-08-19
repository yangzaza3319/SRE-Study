class Gun:
    def __init__(self,model):
        self.model = model
        self.bullet = 0
    def add_bullet(self,count):
        self.bullet += count
    def shoot(self):
        if self.bullet <= 0:
            print("[%s] 没有子弹了"%self.model)
            return
        print("[%s]发射子弹[%d]...突突突"%(self.model,self.bullet))
        self.bullet -= 1
ak47 = Gun("ak47")
ak47.add_bullet(50)
ak47.shoot()

class Soldier:
    def __init__(self,name,gun=None):
        self.name = name
        self.gun = gun
    def fire(self,shots=5):
        if self.gun is None:
            print("[%s] 没有枪"%self.name)
            return
        print(f"[{self.name}] 开火...")
        fired_any = False  # 是否成功发射过子弹
        for _ in range(shots):
            if self.gun.bullet > 0:
                self.gun.shoot()
                fired_any = True
            elif self.gun.bullet <= 0:
                print(f"[{self.gun.model}] 没有子弹了，正在换弹夹")
                self.gun.add_bullet(50)
            else:
                print(f"[{self.gun.model}] 换弹失败，无法射击")
                break
        if not fired_any:
            # 可以选择不输出“开火”或做其他处理
            pass
hongnujian = Soldier("红弩箭",ak47)
for i in range(10):
    hongnujian.fire()



