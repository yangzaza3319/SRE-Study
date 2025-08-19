class Soldier:
    def __init__(self, name, gun=None):
        self.name = name
        self.gun = gun

    def get_gun(self, gun):
        self.gun = gun

    def shoot(self):
        if self.gun is None:
            print("没有枪")
        elif self.gun.count <= 0:
            print("没弹药了，请换弹")
        else:
            self.gun.fire()
            print("冲刺冲刺")

    def add(self):
        if self.gun is None:
            print("没有枪，无法装填子弹")
        else:
            self.gun.add_count()


class Gun:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def fire(self):
        print("开火，子弹数-1")
        self.count -= 1

    def add_count(self):
        if self.count >= 30:
            print("子弹已满，无法装入")
        elif self.count <= 0:
            self.count += 30
            print("已换弹完成")
        else:
            num = 30 - self.count
            self.count += num
            print("已换弹完成")


ak47 = Gun("ak47", 30)
xsd = Soldier("xsd")
xsd.get_gun(ak47)
xsd.add()
xsd.shoot()