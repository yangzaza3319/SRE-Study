from urllib.request import urlopen

def func():
    content = urlopen('https://myip.ipip.net').read().decode('utf-8')
    def inner():
        print(content)
    return inner

f = func()
for i in range(5):
    f()

print(f.__code__.co_freevars)