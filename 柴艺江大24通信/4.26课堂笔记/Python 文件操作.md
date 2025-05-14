## Python 文件操作

### 文件的类型

1. **文本文件**：包含可读的字符（如 .txt`、`.csv ）。一般使用 UTF-8 编码，可以使用文本编辑器查看。
2. **二进制文件**：包含非文本数据（如图像、音频、视频文件，后缀如 `.jpg`、`.png`、`.mp3`）。以原始字节格式存储。需要使用专用软件查看。

### 文件操作过程

1. 打开文件
2. 读写文件
   - 读文件：将文件内容读入内存
   - 写文件：将内存内容写入文件
3. 关闭文件

## 操作方法

### 打开文件

使用 `open()` 函数打开文件，并且返回文件对象：

1. 第一个参数是文件名（文件名区分大小写），第二个参数是打开方式
2. 如果文件存在返回文件操作对象
3. 如果文件不存在抛出异常

```python
f = open("文件名", "访问方式",encoding="utf-8")
```

#### 文件路径

- 绝对路径：从根路径开始描述文件的位置，例如：`F:\技术文件\课件-笔记\课件修订\Python\01.Python基础语法`，具有唯一性，不会出错，不管写在哪里都可以准确的找到文件的位置
- 相对路径：相对当前位置进行文件定位，容易出错，需要对路径比较熟悉

#### 以不同模式打开

| 访问方式 | 说明                                                         |
| :------- | :----------------------------------------------------------- |
| `r`      | 以**只读**方式打开文件。文件的指针将会放在文件的开头，这是**默认模式**。如果文件不存在，抛出异常 |
| `w`      | 以**只写**方式打开文件。如果文件存在会被覆盖。如果文件不存在，创建新文件 |
| `a`      | 以**追加**方式打开文件。如果该文件已存在，文件指针将会放在文件的结尾。如果文件不存在，创建新文件进行写入 |
| `r+`     | 以**读写**方式打开文件。文件的指针将会放在文件的开头。如果文件不存在，抛出异常 |
| `w+`     | 以**读写**方式打开文件。如果文件存在会被覆盖。如果文件不存在，创建新文件 |
| `a+`     | 以**读写**方式打开文件。如果该文件已存在，文件指针将会放在文件的结尾。如果文件不存在，创建新文件进行写入 |
| `r+b`    | 以**二进制读写**方式打开。文件指针在开头，可读可写，文件必须存在 |
| `w+b`    | 以**二进制读写**方式打开。文件指针在开头，先清空再写入，不存在则创建 |
| `a+b`    | 以**二进制读写**方式打开。文件指针在末尾，追加写入，可读全文，不存在则创建 |

对于非文本文件，我们只能使用 `b` 模式，表示以 `bytes` 方式操作（所有文件本质上最终都是字节存储，使用这种模式无需考虑文本文件的字符编码），读取到的内容是字节类型，写入时也需要提供字节类型，不能指定编码。

#### 文件编码

`f = open()` 是由操作系统打开文件，那么如果我们没有指定编码，那么打开文件的默认编码取决于操作系统，操作系统会用自己的默认编码去打开文件，在 Windows 下是 gbk，在 Linux 下是 utf-8。

### 读取文件

```python
f=open("test.txt","r",encoding='utf-8')

print(f.read(size))#读取指定大小的内容，默认读取所有内容

f.seek(0)#将文件指针移动到文件开头

con=f.readline()#读取一行，返回一个字符串
cons=f.readlines()#读取所有行，返回一个列表

print(con)
print(cons)
```

#### 文件指针

有时候我们想要改变文件指针(光标)的位置，就需要用到 `seek()` 来操作指针

```python
file.seek(offset, whence)
```

- **`offset`**：要移动的字节数

- whence

  （可选）：指定偏移量的基准位置。可以取以下值：

  - `0`：从文件开头开始计算（默认值）
  - `1`：从当前位置开始计算
  - `2`：从文件末尾开始计算

```python
file = open('example.txt', 'r')

content = file.read()          # 读取全部内容
file.seek(0)                # 把光标移到到文件的开头
line = file.readline()      # 读取一行
file.seek(0)                # 再次把光标移动到文件的开头
lines = file.readlines()      # 读取所有行
```

#### 按行读取文件内容

- `read()` 默认会把文件的所有内容一次性读取到内存
- `readline()` 可以一次读取一行内容

```python
# 方式一、通过循环按行读取文件所有内容
file1 = open("example.txt")#默认以"r"模式打开
i = 1
while True:
    text1 = file1.readline().strip()#strip()去掉每行左右两边的换行符
    if text1: #如果这一行的内容不为空
        print("这是第%s行内容" % i)
        i += 1
        print(text1)
    else:
        break
file1.close()


file2 = open("example.txt")
# 通过for遍历按行读取文件所有内容
for i in file2.readlines():#readlines()可以将文件每一行储存在一个列表中
    print(i.strip())

file2.close()
```

### 写入内容

可以对文件对象调用 `write()` 实现写入内容

```python
file.write()
```

```python
#日记记录
#以追加的方式打开文件，文件指针在文件末尾

file = open('diary.txt', 'a',encoding='utf-8')

# 获取用户输入的日记内容
content = input("请输入今天的日记：")

# 将日记内容写入文件
file.write(content + "\n")
print("日记已保存！")

# 关闭文件
file.close()
```

### 关闭文件

使用 `close()` 方法关闭文件，释放系统资源，防止文件被一直占用

```python
file.close()
```

### with 结构

使用 `with` 语句可以自动管理文件的打开和关闭，避免忘记关闭文件的情况。

```python
with open('example.txt', 'r') as file:        # 获取file文件对象
    content = file.read()
```

**案例：简单的备份程序**

```python
# 简单备份小程序
source = 'a.txt'
destination = 'b.txt'

with open(source, 'r',encoding='utf-8') as src:
    content = src.read()

with open(destination, 'w',encoding='utf-8') as dest:
    dest.write(content)

print(f"备份成功！'{source}' 的内容已复制到 '{destination}'")
```

### 其他文件操作

```python
class CustomFile:
    def __init__(self, *args, **kwargs):
        """初始化文件对象."""
        pass

    @staticmethod
    def __new__(*args, **kwargs):
        """创建并返回一个新的对象."""
        pass

    def close(self, *args, **kwargs):
        """关闭文件."""
        pass

    def fileno(self, *args, **kwargs):
        """返回文件描述符."""
        pass

    def flush(self, *args, **kwargs):
        """刷新文件内部缓冲区."""
        pass

    def isatty(self, *args, **kwargs):
        """判断文件是否是一个终端设备."""
        pass

    def read(self, *args, **kwargs):
        """读取指定字节的数据."""
        pass

    def readable(self, *args, **kwargs):
        """检查文件是否可读."""
        pass

    def readline(self, *args, **kwargs):
        """仅读取一行数据."""
        pass

    def seek(self, *args, **kwargs):
        """移动文件指针到指定位置."""
        pass

    def seekable(self, *args, **kwargs):
        """检查指针是否可操作."""
        pass

    def tell(self, *args, **kwargs):
        """获取当前指针位置."""
        pass

    def truncate(self, *args, **kwargs):
        """截断文件，仅保留指定之前的数据."""
        pass

    def writable(self, *args, **kwargs):
        """检查文件是否可写."""
        pass

    def write(self, *args, **kwargs):
        """写入内容到文件."""
        pass

    def __next__(self, *args, **kwargs):
        """实现迭代器的 next() 方法."""
        pass

    def __repr__(self, *args, **kwargs):
        """返回文件对象的字符串表示."""
        pass

    def __getstate__(self, *args, **kwargs):
        """自定义对象的序列化状态."""
        pass
    ...
```

### 解释

| 方法名         | 说明                                                         |
| :------------- | :----------------------------------------------------------- |
| `__init__`     | 初始化文件对象的方法。通常在这里设置文件的基本属性           |
| `__new__`      | 静态方法，用于创建新的对象实例                               |
| `close`        | 关闭文件，释放系统资源                                       |
| `fileno`       | 返回文件描述符，通常用于与底层操作系统交互                   |
| `flush`        | 刷新文件的内部缓冲区，将未写入的数据写入文件                 |
| `isatty`       | 判断文件是否是一个终端设备（tty），用于检查文件是否连接到一个用户界面 |
| `read`         | 读取指定字节的数据，可以用来读取文件内容                     |
| `readable`     | 检查文件对象是否可读                                         |
| `readline`     | 读取文件中的一行数据，常用于逐行读取文件内容                 |
| `seek`         | 移动文件指针到指定位置，允许在文件中随机访问                 |
| `seekable`     | 检查文件指针是否可操作，确定文件是否支持随机访问             |
| `tell`         | 返回当前文件指针的位置                                       |
| `truncate`     | 截断文件，只保留指定位置之前的数据                           |
| `writable`     | 检查文件对象是否可写                                         |
| `write`        | 向文件写入内容                                               |
| `__next__`     | 实现迭代器的 `next()` 方法，用于支持迭代访问文件的内容       |
| `__repr__`     | 返回文件对象的字符串表示，通常用于调试                       |
| `__getstate__` | 自定义对象的序列化状态，用于存储和恢复对象的状态             |