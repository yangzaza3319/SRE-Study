#计算总价
l=[]
with open('a.txt','r',encoding='utf-8') as read_f:
    for t in read_f:
        t1=t.strip('\n').split(' ')
        print(t1)
        if len(t1):
            dic={'name':t1[0],'price':t1[1],'amount':t1[2]}
            l.append(dic)
print(l)
price=0
for i in l:
     price+=int(i['price'])*int(i['amount'])
print(price)