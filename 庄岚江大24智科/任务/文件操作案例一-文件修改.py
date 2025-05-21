# 文件存在硬盘上，不可修改，模拟文件修改的方法有两种：
# 方法一：将硬盘存放的该文件的内容全部加载到内存（在内存中是可以修改的），修改后再由内存覆盖到硬盘
import os
with open('a.txt') as read_f,open('a.txt.new','w') as write_f:
    data=read_f.read()
    data=data.replace('Aleph','Beth')
    write_f.write(data)
os.remove('a.txt')
os.rename('a.txt.new','a.txt')
print('修改成功')
# 方法二：将硬盘存放的该文件的内容一行一行地读入内容，修改完毕就写入新文件，最后用新文件覆盖原文件
import os
with open('a.txt') as read_f,open('a.txt.new','w') as write_f:
    for line in read_f:
        line=line.replace('Beth','Aleph')
        write_f.write(line)
os.remove('a.txt')
os.rename('a.txt.new','a.txt')
print('修改成功')