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
    # __init__: 初始化文件对象的方法。通常在这里设置文件的基本属性。
    # __new__: 静态方法，用于创建新的对象实例。
    # close: 关闭文件，释放系统资源。
    # fileno: 返回文件描述符，通常用于与底层操作系统交互。
    # flush: 刷新文件的内部缓冲区，将未写入的数据写入文件。
    # isatty: 判断文件是否是一个终端设备（tty），用于检查文件是否连接到一个用户界面。
    # read: 读取指定字节的数据，可以用来读取文件内容。
    # readable: 检查文件对象是否可读。
    # readline: 读取文件中的一行数据，常用于逐行读取文件内容。
    # seek: 移动文件指针到指定位置，允许在文件中随机访问。
    # seekable: 检查文件指针是否可操作，确定文件是否支持随机访问。
    # tell: 返回当前文件指针的位置。
    # truncate: 截断文件，只保留指定位置之前的数据。
    # writable: 检查文件对象是否可写。
    # write: 向文件写入内容。
    # __next__: 实现迭代器的 next() 方法，用于支持迭代访问文件的内容。
    # __repr__: 返回文件对象的字符串表示，通常用于调试。
    # __getstate__: 自定义对象的序列化状态，用于存储和恢复对象的状态。

file = open('example.txt', 'r')

content = file.read()          # 读取全部内容
file.seek(0)                # 把光标移到到文件的开头
line = file.readline()      # 读取一行
file.seek(0)                # 再次把光标移动到文件的开头
lines = file.readlines()      # 读取所有行

print(content)
print('-----------')
print(line)
print('-----------')
print(lines)

file = open('example.txt', 'r')

content = file.read()          # 读取全部内容
line = file.readline()      # 读取一行
lines = file.readlines()      # 读取所有行

print(content)
print('-----------')
print(line)
print('-----------')
print(lines)

# 思考?
# 为什么后面两个print读取不到东西呢？

"""file.seek(offset, whence)
offset：要移动的字节数。
whence

（可选）：指定偏移量的基准位置。可以取以下值：

0：从文件开头开始计算（默认值）。
1：从当前位置开始计算。
2：从文件末尾开始计算


r	以只读方式打开文件。文件的指针将会放在文件的开头，这是默认模式。如果文件不存在，抛出异常
w	以只写方式打开文件。如果文件存在会被覆盖。如果文件不存在，创建新文件
a	以追加方式打开文件。如果该文件已存在，文件指针将会放在文件的结尾。如果文件不存在，创建新文件进行写入
r+	以读写方式打开文件。文件的指针将会放在文件的开头。如果文件不存在，抛出异常
w+	以读写方式打开文件。如果文件存在会被覆盖。如果文件不存在，创建新文件
a+	以读写方式打开文件。如果该文件已存在，文件指针将会放在文件的结尾。如果文件不存在，创建新文件进行写入
文件操作的过程
打开文件；

读写文件；

读文件：将文件内容读入内存；

写文件：将内存内容写入文件；

关闭文件；

"""

# 案例一
import os
with open('example.txt', 'r') as read_file ,open ('exampleNew.txt', 'w') as write_f:
    # 读取文件内容
    content = read_file.read()
    # 将内容写入新文件
    content = content.write(content)

os.remove('example.txt')  # 删除原文件
os.rename('exampleNew.txt', 'example.txt')  # 重命名新文件为原文件名

# 案例二
import os
products = []
# 新建商品列表

with open('a.txt','r', encoding = 'utf-8') as file:
    for line in file:
        # write_f.write(line)
        for line in file:
        # 去除行首尾空白并分割
            parts = line.strip().split()
            if len(parts) == 3:  # 确保有三个部分
                product = {
                    'name': parts[0],
                    'price': int(parts[1]),  # 转换为整数
                    'amount': int(parts[2])   # 转换为整数
                }
            products.append(product)

# 输出商品列表
print("商品列表", products)

total_price = 0
# 计算总价
for i in products:
    total_price += i['price'] * i['amount']

# 输出总价
print("总价:", total_price)

# # Output:
# [{'name': 'apple', 'price': 10, 'amount': 3}, {'name': 'tesla', 'price': 100000, 'amount': 1}, {'name': 'mac', 'price': 3000, 'amount': 2}, {'name': 'lenovo', 'price': 30000, 'amount': 3}, {'name': 'chicken', 'price': 10, 'amount': 3}]
# 总价: 196060

# 案例三
def load_db(filename="sql.txt"):
    db = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            ret = line.strip().split("|")
            if len(ret) == 3:
                db[ret[0]] = {'password': ret[1], 'status': ret[2]}
    return db

def save_db(db, filename="sql.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for user, info in db.items():
            f.write(f"{user}|{info['password']}|{info['status']}\n")

def register(db, filename="sql.txt"):
    username = input("请输入要注册的用户名：")
    if username in db:
        print("用户名已存在，注册失败！")
        return
    password = input("请输入密码：")
    db[username] = {'password': password, 'status': 'active'}
    save_db(db, filename)
    print("注册成功！")

def login(db, filename="sql.txt"):
    username = input("请输入用户名：")
    if username not in db:
        print("用户名不存在")
        return
    if db[username]['status'] == 'locked':
        print("该账号已被封号，请联系管理员！")
        return
    count = 0
    while count < 3:
        password = input("请输入密码：")
        if password == db[username]['password']:
            print("登录成功")
            return
        else:
            count += 1
            print(f"密码错误，剩余尝试次数：{3-count}")
    db[username]['status'] = 'locked'
    save_db(db, filename)
    print("密码错误3次，账号已被封号！")

def main():
    filename = "sql.txt"
    # 若文件不存在则创建
    import os
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            pass
    while True:
        print("1. 注册  2. 登录  3. 退出")
        choice = input("请选择操作：")
        db = load_db(filename)
        if choice == '1':
            register(db, filename)
        elif choice == '2':
            login(db, filename)
        elif choice == '3':
            print("退出程序")
            break
        else:
            print("无效选择，请重新输入！")

if __name__ == "__main__":
    main()