# day04笔记-模块

## json模块

#### 常用功能：

##### 序列化：将Python内容转换为json内容 

##### 反序列化：反过来

```
print(json.dumps(data))   # 序列化

print(json.loads(pickle.dumps(data))) # 反序列化
```



#### 文件相关：

with open(文件地址，读写，编码) as f：

​	json.dump(data,f)	序列化

​	s = json.load(f)		反序列化



#### 相关参数：

| skipkeys     | 用于控制对字典键类型的严格性检查，默认为 False，当字典的键不是 JSON 规范支持的基本类型时，直接抛出 `TypeError` 异常，反之，跳过这些键，不引发错误，但会导致数据丢失。 |
| ------------ | ------------------------------------------------------------ |
| indent       | 控制 JSON 字符串的格式化缩进，默认值 None 会生成最紧凑的 JSON 字符串，无缩进和多余空格。美化作用 |
| ensure_ascii | 控制非 ASCII 字符转义行为，默认为 True，中文会被转义为 Unicode 转义序列。 |
| separators   | 自定义 JSON 字符串中元素间的分隔符和键值对的分隔符。         |
| sort_keys    | 是否将数据根据 key 进行排序                                  |





## pickle模块

#### 基本用法：

将对象转换为字节流，只能够Python识别

```
print(pickle.dumps(data))   # 序列化

print(pickle.loads(pickle.dumps(data))) # 反序列化
```

#### 文件内容相关：

```
import pickle

with open('./data.pkl', "wb") as f:
    pickle.dump(data, f)    # 序列化
    pickle.dump([1,2,3], f) # 多次调用处理多个对象


with open("./data.pkl", "rb") as f:
    print(pickle.load(f))  # 反序列化
    print(pickle.load(f))   # 多次调用处理多个对象
```





## shelve模块

#### 基本内容：

简单的持久化储存方式，类似于字典，**但更多的是它能够将数据持久化到文件中**

```
import shelve

shelf = shelve.open('my_shelf')  # 打开文件

shelf['name'] = 'EaglesLab' # 存储数据
shelf['age'] = 30
shelf['courses'] = ['Math', 'Science']

print(shelf['name'])    # 读取数据

shelf['age'] = 11  # 更新数据

del shelf['courses']    # 删除数据

shelf.close()   # 关闭文件

```



## hashlib模块

#### 基本内容：

多种哈希算法接口，用于密码核对校验。熟悉了就不写了（懒虫上身ciallo）

hashlib.sha256(b'123456')



## collection模块

namedtuple: 生成可以使用名字来访问元素内容的 tuple

deque: 双端队列，可以快速的从另外一侧追加和推出对象

Counter: 计数器，主要用来计数

OrderedDict: 有序字典

defaultdict: 带有默认值的字典



# 时间模块

## time模块

time.sleep()	time.time()	time.strftime('%Y-%m-%d %X')	time.strftime('%Y-%m-%d %H-%M-%S')

time.localtime()

```
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

## random模块：

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



## OS模块：

交互系统的模块（用的时候直接查是最快最准确的Ciallo）



## sys模块：

与Python解释器交互的一个接口

| 方法           | 作用                                                         |
| -------------- | ------------------------------------------------------------ |
| `sys.argv`     | 命令行参数 List，第一个元素是所在代码文件本身路径。其后是命令元素依次 |
| `sys.exit(n)`  | 退出程序，正常退出时 exit(0)，错误退出 sys.exit(1)           |
| `sys.version`  | 获取 Python 解释器 的版本信息                                |
| `sys.path`     | 返回模块的搜索路径，初始化时使用 PYTHONPATH 环境变量的值     |
| `sys.platform` | 返回操作系统平台名称                                         |



## re模块

正则表达式，不会就去菜鸟上练。但是我太懒，豆包是我的第一选择（bushi）

照搬一下课件，笔记完成。

| 元字符 | 匹配内容                                                     |
| ------ | ------------------------------------------------------------ |
| \w     | 匹配字母（包含中文）或数字或下划线                           |
| \W     | 匹配非字母（包含中文）或数字或下划线                         |
| \s     | 匹配任意的空白符                                             |
| \S     | 匹配任意非空白符                                             |
| \d     | 匹配数字                                                     |
| \D     | 匹配非数字                                                   |
| \A     | 匹配字符串的起始，严格匹配字符串的绝对开始                   |
| \Z     | 匹配字符串的结尾，严格匹配字符串的绝对末尾                   |
| \n     | 匹配一个换行符                                               |
| \t     | 匹配一个制表符                                               |
| ^      | 匹配字符串的起始，re.MULTILINE 匹配每一行的起始              |
| $      | 匹配字符串的结尾，末尾或末尾的换行符前的位置，re.MULTILINE 匹配每一行的末尾 |
| .      | 匹配任意字符，除了换行符，当 re.DOTALL 标记被指定时，则可以匹配包括换行符的任意字符 |
| [...]  | 匹配字符组中的字符                                           |
| [^...] | 匹配除了字符组中的字符的所有字符                             |
| *      | 匹配0个或者多个左边的字符。                                  |
| +      | 匹配一个或者多个左边的字符。                                 |
| ？     | 匹配0个或者1个左边的字符，非贪婪方式。                       |
| {n}    | 精准匹配n个前面的表达式。                                    |
| {n,m}  | 匹配n到m次由前面的正则表达式定义的片段，贪婪方式             |
| a      | b                                                            |
| ()     | 匹配括号内的表达式，也表示一个组                             |





























