import time


# 创建枪对象
class Gun:
    def __init__(self, model):
        self.model = model  # 枪的型号
        self.bullet_count = 0  # 子弹数量,初始为0

    def add_bullet(self, count):
        print("装弹中")
        time.sleep(1)
        self.bullet_count += count
        print(f"装弹成功，剩余子弹{self.bullet_count}")

    def shoot(self):
        if self.bullet_count <= 0:  # 判断是否还有子弹
            print("没有子弹了..快装弹")
            return
        # 发射一颗子弹
        self.bullet_count -= 1
        print("%s 发射子弹，剩余子弹[%d]" % (self.model, self.bullet_count))


ak47 = Gun("ak47")
ak47.shoot()
ak47.add_bullet(50)


# 创建士兵类
class Soldier:
    def __init__(self, name, gun=None):
        self.name = name
        self.gun = gun

    def fire(self):
        if self.gun is None:
            print("{self.name}还没枪，去捡一把")
        else:
            print("冲啊...[%s]" % self.name)
            if self.gun.bullet_count <= 0:
                print("没子弹了，快换弹夹...")
                # 3. 让枪装填子弹
                self.gun.add_bullet(50)
                # 4. 让枪发射子弹
                self.gun.shoot()


xsd = Soldier("xsd", ak47)
xsd.fire()