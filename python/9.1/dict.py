# 字典
## 字典的定义
dic = {"name":'cs',"age":'18',"job":'IT'}
print(dic) # 输出 {'name': 'cs', 'age': '18', 'job': 'IT'}
print("名字是"+dic["name"]) # 输出 名字是cs
print("年龄是"+dic["age"]) # 输出 年龄是18
print("工作是"+dic["job"]) # 输出 工作是IT

## 字典的增删改查
## 通过键值对来增加
dic["兴趣爱好"]="打羽毛球"
print(dic) # 输出 {'name': 'cs', 'age': '18', 'job': 'IT', '兴趣爱好': '打羽毛球'}
dic["job"]="后端开发" # 若键存在，则直接对其原来的值进行修改
print(dic) # 输出 {'name': 'cs', 'age': '18', 'job': '后端开发', '兴趣爱好': '打羽毛球'}

## 删除键值
name = {'name': 'cs', 'age': '18', 'job': '后端开发', '兴趣爱好': '打羽毛球'}
### 1.删除指定的键
name = dic.pop("兴趣爱好","查无此项") # 删除指定的键，并返回该键对应的值
print(name) # 输出 打羽毛球
print(dic) # 输出 {'name': 'cs', 'age': '18', 'job': '后端开发'}
