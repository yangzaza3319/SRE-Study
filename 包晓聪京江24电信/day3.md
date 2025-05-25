常用模块：

1序列化模块

①json：将python对象转化为json字符串（str）

#<font style="color:#ED740C;">引入import json</font>

<font style="color:#ED740C;">xxxx = json.dumps(python对象)</font>

<font style="color:#ED740C;"> json.loads（反序列化）</font>

文件操作：

dump/load #用于读取一个json文件并将其中json字符串转化为py/将py转化为json字符串写入一个json文件

自定义序列化

改变序列化之后的json格式

pickle：

<font style="color:rgb(51, 51, 51);">不同的是 json 模块序列化出来的是通用格式，其它编程语言都认识，就是普通的字符串，而 pickle 模块序列化出来的只有python 可以认识，其他编程语言不认识的，表现为乱码。</font>



shelf：

<font style="color:rgb(51, 51, 51);">Python 的 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(247, 247, 247);">shelve</font>`<font style="color:rgb(51, 51, 51);"> 模块提供了一种简单的持久化存储方式，类似于字典，但它可以将数据持久化到文件中。</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(247, 247, 247);">shelve</font>`<font style="color:rgb(51, 51, 51);"> 模块允许将 Python 对象存储在文件中，以便在后续的程序运行中重新加载。</font>

<font style="color:rgb(51, 51, 51);"></font>

<font style="color:rgb(51, 51, 51);">hashlib：</font>

<font style="color:rgb(51, 51, 51);">Python 的 </font>`<font style="background-color:rgb(247, 247, 247);">hashlib</font>`<font style="color:rgb(51, 51, 51);"> 模块提供了多种安全哈希和消息摘要算法的接口。这些算法用于生成数据的唯一哈希值，广泛应用于数据完整性校验、密码存储和数字签名等领域。</font>

<font style="color:rgb(51, 51, 51);">什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。</font>

1. **<font style="color:#ECAA04;">不可逆性</font>**<font style="color:#ECAA04;">：哈希函数是不可逆的，意味着无法从哈希值恢复原始数据。</font>
2. **<font style="color:#ECAA04;">碰撞</font>**<font style="color:#ECAA04;">：不同的输入可能生成相同的哈希值（称为碰撞），但现代的哈希算法力求使碰撞的概率尽量低。</font>
3. **<font style="color:#ECAA04;">安全性</font>**<font style="color:#ECAA04;">：对于密码存储，建议使用更安全的哈希算法（如 SHA-256 或更高版本）和适当的盐值（salt）来增强安全性。</font>

<font style="color:rgb(38, 116, 186);">  
</font><font style="color:rgb(38, 116, 186);">collections 模块</font>

<font style="color:#000000;">namedtuple:</font>

```python
from collections import namedtuple
point = namedtuple('point',['x','y'])
p = point(1,2)
print(p.x)  # 通过名字访问 tuple 元素
```

<font style="color:rgb(51, 51, 51);">使用 list 存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为 list 是线性存储，数据量大的时候，插入和删除效率很低。</font>

<font style="color:rgb(51, 51, 51);">deque 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈。</font>

```python
from collections import deque

q = deque(['a','b','c'])
q.append('x')   # 尾部添加
print(q)    
q.pop()     # 尾部删除
q.appendleft('y')   # 头部添加
print(q)
q.popleft() # 头部删除
```

<font style="color:#000000;">oederedDict:</font>

<font style="color:rgb(51, 51, 51);">OrderedDict会按照插入的顺序排列，不是 key 本身排序。Python 3.6 之前普通字典完全无序，键值顺序由哈希表存储方式决定。</font>

```python
d1 = {'a':1, 'b':2}
d2 = {'b':2, 'a':1}
print(d1 == d2)  # 输出：True（内容相同即视为相等）

from collections import OrderedDict
od1 = OrderedDict([('a',1), ('b',2)])
od2 = OrderedDict([('b',2), ('a',1)])
print(od1 == od2)  # 输出：False（有序字典比较顺序）
```

<font style="color:#000000;">defaultdict:</font>

<font style="color:rgb(51, 51, 51);"></font><font style="color:rgb(51, 51, 51);">键不存在时，自动生成默认值，普通 dict 抛出 KeyError 异常，需要频繁处理缺失键。</font>

**<font style="color:rgb(51, 51, 51);">基本用法</font>**

```python
from collections import defaultdict

defaultdict(list)  # 值类型为列表（分组）
defaultdict(set)   # 值类型为集合（去重）
defaultdict(int)   # 值类型为整数（计数）
```

<font style="color:#000000;"></font>

<font style="color:#000000;">counter:</font>

<font style="color:rgb(51, 51, 51);">Counter 类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为 key，其计数作为 value</font>

<h1 id="f3GW4"><font style="color:rgb(38, 116, 186);">时间相关的模块:</font></h1>
time:

<font style="color:rgb(51, 51, 51);">在 Python 中，通常有这三种方式来表示时间：时间戳、结构化时间和格式化时间</font>

+ <font style="color:rgb(51, 51, 51);">时间戳：通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。如 </font>`<font style="background-color:rgb(247, 247, 247);">1747114142.79492</font>`
+ <font style="color:rgb(51, 51, 51);">格式化时间：如 </font>`<font style="background-color:rgb(247, 247, 247);">1999-12-06</font>`<font style="color:#ECAA04;background-color:rgb(247, 247, 247);">（需要看表格）</font>
+ <font style="color:rgb(51, 51, 51);">结构化时间：如 </font>`<font style="background-color:rgb(247, 247, 247);">time.struct_time(tm_year=2025, tm_mon=5, tm_mday=13, tm_hour=13, tm_min=29, tm_sec=54, tm_wday=1, tm_yday=133, tm_isdst=0)</font>`
+ `<font style="background-color:rgb(247, 247, 247);">time.sleep(secs)</font>`<font style="color:rgb(51, 51, 51);">：(线程)推迟指定的时间运行。单位为秒。</font>
+ `<font style="background-color:rgb(247, 247, 247);">time.time()</font>`<font style="color:rgb(51, 51, 51);">：获取当前时间戳。</font>

三种时间的转化：

```python
import time

#  时间戳 <---> 结构化时间
timestamp = time.time()
struct_time = time.localtime(timestamp)
new_timestamp = time.mktime(struct_time)

# 结构化时间 <---> 格式化时间
## struct_time -> format_time
ft = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(1550312090))
## format_time -> struct_time
st = time.strptime("2024/05/14 11:57:30", "%Y/%m/%d %H:%M:%S")
```

datatime：

<font style="color:rgb(51, 51, 51);">某些情况下，我们需要写一个定时的任务，比如几分钟后，几分钟前，这种情况下，用 time 模块就不太好操作。这个时候我们需要 datatime 模块来完成这个操作。</font>

```python
# datatime模块
import datetime

current_time = datetime.datetime.now()  # 当前时间

# 只能调整的字段：weeks days hours minutes seconds
print(datetime.datetime.now() + datetime.timedelta(weeks=3)) # 三周后
print(datetime.datetime.now() + datetime.timedelta(weeks=-3)) # 三周前
print(datetime.datetime.now() + datetime.timedelta(days=-3)) # 三天前
print(datetime.datetime.now() + datetime.timedelta(days=3)) # 三天后
print(datetime.datetime.now() + datetime.timedelta(hours=5)) # 5小时后
print(datetime.datetime.now() + datetime.timedelta(hours=-5)) # 5小时前
print(datetime.datetime.now() + datetime.timedelta(minutes=-15)) # 15分钟前
print(datetime.datetime.now() + datetime.timedelta(minutes=15)) # 15分钟后
print(datetime.datetime.now() + datetime.timedelta(seconds=-70)) # 70秒前
print(datetime.datetime.now() + datetime.timedelta(seconds=70)) # 70秒后

current_time = datetime.datetime.now()
# 可直接调整到指定的 年 月 日 时 分 秒 等

print(current_time.replace(year=1977))  # 直接调整到1977年
print(current_time.replace(month=1))  # 直接调整到1月份
print(current_time.replace(year=1989,month=4,day=25))  # 1989-04-25 18:49:05.898601

# 时间戳 ---> 格式化时间
print(datetime.date.fromtimestamp(1232132131))  # 2009-01-17
```

<h1 id="random-模块"><font style="color:rgb(38, 116, 186);">random 模块:</font></h1>
<font style="color:rgb(51, 51, 51);">用来生成随机数模块</font>

```python
import random

print(random.random())          # 大于0且小于1之间的小数
print(random.uniform(1,3))      # 大于1小于3的小数

print(random.randint(1,5))      # 大于等于1且小于等于5之间的整数
print(random.randrange(1,10,2))   # 大于等于1且小于10之间的奇数

ret = random.choice([1,'23',[4,5]])     # 1或者23或者[4,5]
print(ret)

a,b = random.sample([1,'23',[4,5]],2)   # 列表元素任意2个组合
print(a,b)

item = [1,3,5,7,9]
random.shuffle(item)    # 打乱次序
print(item)
```

<font style="color:rgb(51, 51, 51);">生成随机验证码</font>

```python
import random

def v_code():
    code = ''
    for i in range(5):
        num = random.randint(0,9)
        alf = chr(random.randint(65,90))    # 大写字母
        add = random.choice([num,alf])
        code = "".join([code,str(add)])

    return code

print(v_code())
```



<h1 id="os-模块"><font style="color:rgb(38, 116, 186);">os 模块：</font></h1>
<font style="color:rgb(51, 51, 51);">操作系统交互接口</font>

<font style="color:#000000;"></font>

<font style="color:#000000;">  
</font>

