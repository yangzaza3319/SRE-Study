#文件的修改

import os
#将test_txt以只读模式打开，将text_1以只写模式打开（会将其覆盖）
with open("test.txt") as read_f,open("test_1.txt","w") as write_f:
    for l in read_f:#将l放在read_f中迭代
        l=l.replace('hello','nihao')
        write_f.write(l)#将l写入test_1.txt
os.remove("test.txt")#将test.txt删除
os.rename("test_1.txt","test.txt")#将test_1.txt重命名为test.txt