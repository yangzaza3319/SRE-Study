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