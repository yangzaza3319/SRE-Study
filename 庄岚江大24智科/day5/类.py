class MyClass:
    #  类属性:内部添加
    class_atttr = "I am a class attribute"
    def __init__(self,name):
        #对象属性：内部添加
        self.name = name
    def add_attr(self,age):
        #对象属性：内部添加
        self.age = age
mc1 = MyClass("张三")#实例化对象
print(mc1.name)#访问对象属性
print(MyClass.class_atttr)#访问类属性

MyClass.new_class_atttr = "I am a new class attribute"#外部动态添加类属性
print(MyClass.new_class_atttr)
mc1.address = "北京"#外部动态添加对象属性
print(mc1.address)
mc2 = MyClass("李四")
print(mc2.__dict__)#查看对象所有属性
print(MyClass.__dict__)#查看类所有属性
print(MyClass.new_class_atttr)


"""
对象如何找到类属性
顺序：
    -先从对象空间找(__init__)
    -类空间找(MyClass)
    -父类空间找(MyClass(OtherClass))
    -基类空间找(object)

类名查找顺序：
1.从本类空间找
2.从父类空间找
3.从基类空间找
"""

class TestClass:
    name = "TestClass"
    def __init__(self,name):
        pass

tc1 = TestClass("sre")
print(tc1.name)#TestClass

"""
类之间的关系：
依赖关系
关联关系
组合关系
聚合关系
实现关系
继承关系 
"""

#依赖关系
#例：将大象装进冰箱，需要两个类, ⼀个是⼤象类, ⼀个是冰箱类
class elephant:
    def __init__(self,name):
        self.name = name
    def open(self,obj):
        print("Elephant opens the Refrigerator")
    def go(self):
        print("Elephant goes into the Refrigerator")
    def close(self,obj):
        print("Elephant closes the Refrigerator")
class refrigerator:
    def __init__(self,name):
        self.name = name
    def open_door(self):
        print("Refrigerator opens")

    def close_door(self):
        print("Refrigerator closes")
rf1 = refrigerator("geli")
el1 = elephant("xiaofeixiang")
el1.open(rf1)#依赖关系elephant 依赖refrigerator
el1.go()
el1.close(rf1)

#关联-聚合-组合关系
# 其实这三个在代码上写法是⼀样的，但是从含义上是不⼀样的：
#
# 关联关系：两种事物必须是互相关联的，但是在某些特殊情况下是可以更改和更换的。
# 聚合关系：属于关联关系中的一种特例，侧重点是xxx和xxx聚合成xxx，各自有各自的声明周期，比如电脑，电脑里有 CPU， 硬盘， 内存等等。电脑挂了， CPU 还是好的，还是完整的个体。
# 组合关系：属于关联关系中的⼀种特例，写法上差不多，组合关系比聚合还要紧密。比如⼈的⼤脑，⼼脏，各个器官，这些器官组合成⼀个⼈。这时，⼈如果挂了，其他的东⻄也跟着挂了。
class Boy:
    def __init__(self,name,girlfriend = None):
        self.name = name
        self.girlfriend = girlfriend
    def dinner(self):
        if self.girlfriend:
            print("%s is eating with %s" % (self.name,self.girlfriend.name))
        else:
            print("%s is eating alone"% self.name)
class Girl:
    def __init__(self,name):
        self.name = name
boy1 = Boy("boy1")
girl1 = Girl("girl1")
boy1.dinner()
boy2 = Boy("boy2",girl1)
boy2.dinner()

class School:
    def __init__(self,name,address):
        self.name = name
        self.address = address
class Teacher:
    def __init__(self,name,school):
        self.name = name
        self.school = school
s1 = School("迷思海","100m")
s2 = School("荒原","100块")
s3 = School("重返未来","1999")
t1 = Teacher("维尔汀",s1)
t2 = Teacher("星锑",s2)
t3 = Teacher("十四行诗",s3)
print(t1.school.name)
print(t2.school.name)
print(t3.school.name)

class School:

    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.teacher_list = []
    def append_teacher(self,teacher):
        self.teacher_list.append(teacher)


class Teacher:

    def __init__(self,name,school):
        self.name = name
        self.school = school

s1 = School('北京校区','北京')
s2 = School('上海校区','上海')
s3 = School('深圳校区','深圳')

t1 = Teacher('T1',s1)
t2 = Teacher('T2',s2)
t3 = Teacher('T3',s3)

s1.append_teacher(t1.name)
s1.append_teacher(t2.name)
s1.append_teacher(t3.name)

print(s1.teacher_list)

#组合：将一个类 的对象封装到另一个类的对象的属性中
#例：设计一个游戏，让游戏里面的人物互殴，加上一个武器类，让人使用武器攻击。
class Gamerole:
    def __init__(self,name,ad,hp,wea=None):
        self.name = name
        self.ad = ad
        self.hp = hp
        self.wea = wea

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


man = Gamerole('人',10,100)
dog = Gamerole('狗',50,100)
stick = Weapon('木棍',40)

man.equip_weapon(stick)
man.wea.weapon_attack(dog)
# 人利用木棍攻击了狗，狗还剩50血


#重返未来1999战斗
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

xingti = Gamerole("星锑", 20, 500)
yaxain = Gamerole("牙仙", 20, 100)
sanqi = Gamerole("37", 50, 80)
zhixinquaner = Gamerole("纸信圈儿", 20, 100)

Alepha = Gamerole("阿莱夫", 30, 450)
kubohuahuan = Gamerole("库伯花环", 80, 200)
bakaluoer = Gamerole("芭卡洛尔", 60, 150)
huanzhaungshuixing = Gamerole("环状水星", 20, 100)

blue_list = [xingti, yaxain, sanqi, zhixinquaner]
red_list = [Alepha, kubohuahuan, bakaluoer, huanzhaungshuixing]

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