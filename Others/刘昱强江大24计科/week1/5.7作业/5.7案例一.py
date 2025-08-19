import os
a = open('TEXT.txt', 'w', encoding='utf-8')
a.write("apple 0 3\ntesla 1000000 1\nmac 3000 3\nlenevo 300000 3\nchicken 10 3")
a.close()
with open('TEXT.txt') as read_f, open('newTEXT.txt', 'w') as write_f:
    for line in read_f:
        line = line.replace('hello', 'nihao')
        write_f.write(line)

os.remove('TEXT.txt')
os.rename('newTEXT.txt', 'TEXT.txt')
print("修改成功")
