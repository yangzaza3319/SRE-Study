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