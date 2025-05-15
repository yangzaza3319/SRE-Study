from urllib.request import urlopen
def func():
    content=urlopen('http://myip.ipip.net').read().decode('utf-8')
    def inner():
        print(content)
    return inner

f=func()
for i in range(5):
    f()