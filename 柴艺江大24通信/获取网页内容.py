'''假定我们需要多次访问一个静态网站，
但是由于该网站访问较慢，
所以导致每次访问都需要等待，比较浪费时间。
这里我们可以使用闭包函数将第一次访问到的网页内容封装到外部作用域的变量中，
以后我们只需要调用该变量就可以了...
'''



from urllib.request import urlopen
def func():
    con=urlopen('https://www.bilibili.com/').read().decode('utf-8')
    def inner():
        print(con)
    return inner

f=func()
for i in range(5):
    f()