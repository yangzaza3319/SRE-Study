### 经典类 vs 新式类

```plain
# 经典类（Python 2.x默认，Python 3.x已移除）
class ClassicClass: pass

# 新式类（Python 3.x默认）
class ModernClass(object): pass
```

### C3算法解析

C3算法决定了多继承时的方法查找顺序，遵循三个原则：

1. **局部优先**：子类先于父类
2. **单调性**：继承顺序保持一致
3. **一致性**：父类方法解析顺序被保留

```plain
class D: pass
class E: pass
class F: pass
class B(D,E): pass
class C(E,F): pass
class A(B,C): pass

print(A.__mro__)  # 查看方法解析顺序
# 输出: (A, B, D, C, E, F, object)
```