### super()工作原理

```plain
class A:
    def method(self):
        print("A的方法")

class B(A):
    def method(self):
        super().method()  # 调用父类方法
        print("B的方法")

class C(A):
    def method(self):
        print("C的方法")

class D(B, C):
    def method(self):
        super().method()  # 按MRO顺序调用
        print("D的方法")

d = D()
d.method()
"""
输出:
C的方法  # 注意不是A的方法！
B的方法
D的方法
"""
print(D.__mro__)  # 查看方法解析顺序
```

### super()指定起点

```plain
class D(B, C):
    def method(self):
        super(B, self).method()  # 从B之后开始查找
        print("D的方法")

d = D()
d.method()
"""
输出:
C的方法
D的方法
"""
```

## 综合案例：支付系统设计

```plain
from abc import ABCMeta, abstractmethod
from typing import List

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, amount: float) -> bool: pass

class PaymentLogger:
    def log_payment(self, amount: float, success: bool):
        status = "成功" if success else "失败"
        print(f"支付记录: 金额{amount}元, 状态{status}")

class Alipay(Payment, PaymentLogger):
    def __init__(self, account: str):
        self.account = account
    
    def pay(self, amount: float) -> bool:
        print(f"支付宝账户{self.account}支付{amount}元")
        return True  # 模拟支付成功

class WechatPay(Payment, PaymentLogger):
    def __init__(self, openid: str):
        self.openid = openid
    
    def pay(self, amount: float) -> bool:
        print(f"微信用户{self.openid}支付{amount}元")
        return True

class PaymentProcessor:
    def __init__(self):
        self.payments: List[Payment] = []
    
    def add_payment(self, payment: Payment):
        self.payments.append(payment)
    
    def process_payments(self, amount: float):
        for payment in self.payments:
            success = payment.pay(amount)
            if isinstance(payment, PaymentLogger):
                payment.log_payment(amount, success)

# 使用示例
processor = PaymentProcessor()
processor.add_payment(Alipay("123@alipay.com"))
processor.add_payment(WechatPay("wx_abcd1234"))

processor.process_payments(100.50)
```

## 设计模式实践：策略模式

```plain
class ExportStrategy(metaclass=ABCMeta):
    @abstractmethod
    def export(self, data): pass

class PDFExport(ExportStrategy):
    def export(self, data):
        print(f"导出PDF: {data}")

class ExcelExport(ExportStrategy):
    def export(self, data):
        print(f"导出Excel: {data}")

class ReportGenerator:
    def __init__(self, strategy: ExportStrategy):
        self.strategy = strategy
    
    def generate(self, data):
        print("准备报告数据...")
        self.strategy.export(data)
        print("报告生成完成")

# 客户端代码
report = ReportGenerator(PDFExport())
report.generate("销售数据")

# 动态切换策略
report.strategy = ExcelExport()
report.generate("财务数据")
```