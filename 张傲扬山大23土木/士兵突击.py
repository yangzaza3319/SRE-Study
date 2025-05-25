from time import sleep

class Gun:
    def __init__(self, model, magazine_capacity):
        self.model = model
        self.magazine_capacity = magazine_capacity  # 弹匣容量
        self.ammo = 0  # 当前子弹数量（含枪膛）

    def reload(self, bullets):
        if self.ammo == 0:
            # 空枪装填
            self.ammo = min(bullets, self.magazine_capacity)
            print(f'弹匣装入 {self.ammo} 发子弹，{self.model}现在共有{self.ammo}发子弹')
        else:
            # 非空枪换弹匣（保留枪膛内1发）
            self.ammo = min(bullets, self.magazine_capacity) + 1
            print(f'弹匣装入 {bullets} 发子弹，{self.model}现在共有{self.ammo}发子弹')

# 射击
    def shoot(self, count):
        if self.ammo <= 0:
            print(f'{self.model}没子弹了，需要换弹匣')
            return False

        actual_shoot = min(count, self.ammo)
        for _ in range(actual_shoot):
            print('发射1发子弹')
            print('上膛')
            sleep(0.1)
            self.ammo -= 1
            print(f'{self.model}: {self.ammo}/{self.magazine_capacity}')

        if self.ammo <= 0:
            print(f'{self.model}已空仓')
        return True

class Soldier:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def equip(self, gun):
        self.weapon = gun
        print(f'{self.name}装备了{self.weapon.model}')

    def fire_weapon(self):
        if not self.weapon:
            print(f'{self.name}没有装备武器')
            return

        if self.weapon.ammo == 0:
            print(f'没子弹了，{self.name}快去装子弹')
            bullets = int(input('请输入要装填的子弹数: '))
            self.weapon.reload(bullets)

        count = int(input('请输入要发射的子弹数: '))
        print(f'{self.name}: 开火！')
        self.weapon.shoot(count)

        if input('是否更换弹匣(输入1更换): ') == '1':
            bullets = int(input('请输入更换弹匣内装填的子弹数: '))
            self.weapon.reload(bullets)

# 主程序
if __name__ == "__main__":
    # 创建士兵和武器

    soldier = Soldier('大兵乌鲁鲁')
    gun_model = input("请输入枪支型号: ")
    maga = int(input("请输入弹匣容量: "))
    gun = Gun(gun_model, maga)

    # 装备武器
    soldier.equip(gun)

    
    # 循环
    while True:
        soldier.fire_weapon()
        if input('是否继续 (输入"0"退出): ') == '0':
            break    