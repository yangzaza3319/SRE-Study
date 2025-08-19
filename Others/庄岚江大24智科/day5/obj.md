"""
面向过程：函数式编程
以步骤和过程为核心，本质是将复杂问题分解为一系列可执行的函数或过程

核心思想：
     -步骤分解
     -顺序执行
     -数据与操作分离
典型特征：
    -模块化函数
    -高效性
    -线性流程


面向对象：以对象为核心的编程范式，核心思想是将数据和操作数据的方法封装成独立的程序
    通过对象之间的协作完成复杂工作
核心概念：
    -类（Class）：定义对象的模板
    -对象(Object)：类的具体实例
    -封装：将数据和方法捆绑在对象内部，仅暴露接口与外界交互
    -继承：子类可复用父类的属性和方法
    -多态：同一方法在不同对象中呈现不同行为
    -抽象：提取共性特征成为接口


python
`class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.gender = "男"
        self.height = 180
        self.weight = 80
        self.hobby = ["打球","看电影"]

    def eat(self):
        print(f"{self.name}正在吃东西")
    def sleep(self):
        print(f"{self.name}正在睡觉")
class Student(Human):#继承Human类(默认继承自object,所有类的顶层)
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
        self.grade = 1
        self.score = 0
        self.course = ["数学","语文","英语"]
    def study(self):
        print(f"{self.name}正在学习")
obj = Student("张三",18,"清华大学")#创建对象
obj.eat()#调用对象的方法
obj.sleep()
print(obj.name)#访问对象的属性
print(obj.school)
print(obj.__dict__)#查看访问对象的所有属性`
# 其实实例化一个对象总共发生了三件事：
#
# 在内存中开辟了一个对象空间。
# 自动执行类中的 方法，并将这个对象空间（内存地址）传给了 方法的第一个位置参数 self。__init____init__
# 在 方法中通过 self 给对象空间添加属性。__init__
#类名调用动态方法
Human.eat(obj)#调用类方法

print(Human.__dict__)

python
`class Human(object):  # 默认继承自 object
    """
    此类用来构造人类
    """
    mind = "思考问题.."

    def __init__(self, name, age, height):
        # 在__init__中，通过self给对象封装属性
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        print('高高兴兴的跑步')

    def eat(self):
        print('大口大口的吃饭')

print(Human.mind)
Human.mind = '高智慧'
print(Human.mind)

del Human.mind#删除类属性
Human.run = '慢慢悠悠的走路'
print(Human.run)
# 通过万能的点 可以增删改查类中的单个属性
print('大口大口的吃饭')`

类的内置方法
方法名	作用
__new__	创建对象时，会被自动调用
__init__	对象被初始化时，会被自动调用
__del__	对象被从内存中销毁前，会被自动调用
__str__	返回对象的描述信息，print 函数输出使用
__dir__	查看对象内所有属性以及方法

先有类才有对象，类是模版，对象是通过类实例化出来的。
一个类可以实例化很多个对象。
类中包含静态属性和动态方法，包括内置方法，自定义方法。
实例化对象的时候，会自动调用 __init__ 来初始化，我们可以在 __init__ 中定义对象初始化的属性
实例化好的对象可以调用类中的方法或者是静态属性