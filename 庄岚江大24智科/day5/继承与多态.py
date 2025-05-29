#继承，子类可复用父类的属性和方法，并扩展新功能
class Aniaml(object):
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}吃东西..")

class Dog(Aniaml):
    pass

xiaotianquan = Dog("哮天犬",5)
xiaotianquan.eat()
"""
继承的优点：

增加了类的耦合性（耦合性不宜多，宜精）。
减少了重复代码。
使得代码更加规范化，合理化。
继承分类
上面的那个例子，涉及到的专业术语：

Dog类是Animal 类的子类， Animal类是 Dog类的父类， Dog类从Animal 类继承 
Dog类是Animal 类的派生类， Animal类是 Dog类的基类， Dog类从 Animal类派生 
继承：可以分单继承，多继承。
"""
class Aniaml(object):
    type_name = '动物类'

    def __init__(self,name,sex,age):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print('吃',self)

class Person(Aniaml):
    pass

class Cat(Aniaml):
    pass

class Dog(Aniaml):
    pass

print(Person.type_name)
Person.eat('东西')
print(Person.type_name)

p1 = Person('aaron','男',18)
print(p1.__dict__)
print(p1.type_name)
p1.type_name = '666'
print(p1)
p1.eat()

class Aniaml(object):
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}吃东西..")
    def run(self):
        print(f"{self.name}跑跑跑..")

class person(Aniaml):
    def eat(self):
        print('%s 用筷子吃饭' % self.name)

class Dog(Aniaml):
    def run(self):
        # 调用父类的方法
        Aniaml.run(self)
        print('%s 跑的快' % self.name)

class Cat(Aniaml):
    pass


person1 = person('张三',18)
person1.eat()
dog1 = Dog('旺财',3)
dog1.run()


class Aniaml(object):
    type_name = '动物类'
    def __init__(self,name,sex,age):
            self.name = name
            self.age = age
            self.sex = sex

    def eat(self):
        print('吃东西')

class Person(Aniaml):
    def __init__(self,name,sex,age,mind):
        # super(Person,self).__init__(name,sex,age)
        super().__init__(name,sex,age)
        self.mind = mind

    def eat(self):
        super().eat()
        print('%s 吃饭' % self.name)

class Cat(Aniaml):
    pass

class Dog(Aniaml):
    pass

p1 = Person('aaron','男',18,'想吃东西')
p1.eat()


class D:
    pass
class E:
    pass
class F:
    pass
class B(D,E):
    pass
class C(E,F):
    pass
class A(B,C):
    pass
print(A.__mro__)