# 方法一，全部加载到内存修改，再覆盖到硬盘。

import os       #导入os标准库
with open("1.txt") as f_read, open("2.txt", "w") as f_write:
    data = f_read.read()    #读取1的内容
    data = data.replace('hello', 'nihao')   #修改内容
    f_write.write(data)     #修改后的内容写入2
os.remove('1.txt')      #将1删除
os.rename('2.txt', '1.txt')         #将 2 改名为 1
# 现象：1.txt内容变为nihao，2.txt消失

# #方法二，一行一行实现

# import os
# with open("1.txt") as f_read, open("2.txt", "w") as f_write:
# #for循环会逐行读取文件内容
#     for line in f_read:
#         line = line.replace('hello', 'nihao')
#         f_write.write(line)
# os.remove('1.txt')
# os.rename('2.txt', '1.txt')

