"""编写好的一个python文件可以有两种用途：

脚本，一个文件就是整个程序，用来被执行

模块，文件中存放着一堆功能，用来被导入使用
python为我们内置了全局变量__name__，

当文件被当做脚本执行时：__name__ 等于'__main__'

当文件被当做模块导入时：__name__等于模块名

作用：用来控制.py文件在不同的应用场景下执行不同的逻辑（或者是在模块文件中测试代码）"""
    # 1.当文件被当做脚本执行时，__name__等于'__main__'
if __name__ == '__main__':
    print('hello world')
else:
    # 2.当文件被当做模块导入时，__name__等于模块名
    print('hello module')



def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=',')
        a, b = b, a+b
    print()

if __name__ == "__main__":
    print(__name__)
    num = input('num :')
    fib(int(num))    

print(globals())