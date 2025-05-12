def calculator(a,op,b):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        if b==0:
            return '除数不能为0'
        else:
            return a/b
a=int(input('请输入第一个数字：'))
op=input('请输入运算符：')
b=int(input('请输入第二个数字：'))
print(calculator(a,op,b))