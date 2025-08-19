import os
with open('a.txt','r') as file1,open('anew.txt','w')as file2:
    data=file1.read()
    data=data.replace('nihao','hello')
    file2.write(data)

    os.remove('a.txt')
    os.rename('anew.txt','a.txt')