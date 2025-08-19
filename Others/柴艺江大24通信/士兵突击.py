class Gun:
    def __init__(self,type):
        self.name = type
        self.bullets = 0


    def fill_bullet(self,num):
        self.bullets += num
        print(f'装填子弹数: {num},{self.name}现在有{self.bullets}发子弹')
    def shoot(self,num):
        if self.bullets >= num:
            print('发射了{num}发子弹')
            print('突'*num)
            self.bullets -= num
            print(f'剩余子弹数: {self.bullets}')
        elif self.bullets <= num:
            print(f'{self.name}里的子弹不够')
            n = int(input('请输入要装填的子弹数：'))
            self.fill_bullet(n)
            return

class Soldier:
    def __init__(self,name,weapon = None):
        self.name = name
        self.weapon = weapon
    def fire(self):
        if not self.weapon:
            print(f'{self.name}还没有枪，快去捡一把枪')
            return
        else:
            if self.weapon.bullets == 0:
                print(f'没子弹了，{self.name}快去装子弹')
                b = int(input('请输入要装填的子弹数:'))
                self.weapon.fill_bullet(b)
            f = int(input('请输入要发射的子弹数:'))
            print(f'{self.name}！！！ 冲啊！！！')
            self.weapon.shoot(f)

soldier = Soldier('维也纳传奇枪王')
gun = Gun('小手枪')
soldier.weapon = gun
while True:
    soldier.fire()
    if input('是否继续:') == '否':
        break



