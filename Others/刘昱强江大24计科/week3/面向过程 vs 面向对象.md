### 面向过程编程

- **核心**：步骤分解 + 顺序执行
- **特点**：

- 功能封装为函数
- 数据与操作分离
- 线性流程，适合简单任务

- **示例**：

```plain
def wake_up(): print("起床")
def dress(): print("穿衣")
def wash(): print("洗漱")
def go_to_school(): print("去学校")

# 顺序调用
wake_up()
dress()
wash()
go_to_school()
```

### 面向对象编程

- **核心**：对象 + 交互
- **特点**：

- 封装数据与行为
- 继承实现代码复用
- 多态增强灵活性
- 适合复杂系统

- **示例**：

```plain
class Student:
    def __init__(self, name):
        self.name = name
    
    def morning_routine(self):
        self.wake_up()
        self.dress()
        self.wash()
        self.go_to_school()
    
    def wake_up(self): print(f"{self.name}起床")
    def dress(self): print(f"{self.name}穿衣")
    def wash(self): print(f"{self.name}洗漱")
    def go_to_school(self): print(f"{self.name}去学校")

# 创建对象并调用
xiaoming = Student("小明")
xiaoming.morning_routine()
```