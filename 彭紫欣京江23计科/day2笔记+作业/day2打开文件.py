import os

with open('a.txt') as read_f,open('a.txt.new','w') as write_f:
    data = read_f.read()
    data = data.replace('hello','nihao')

    write_f.write(data)

os.remove('a.txt')
os.rename('a.txt.new','a.txt')