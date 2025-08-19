#找到嵌套列表中名字含有两个及以上‘a’的所有名字
fruits = [['peach','Lemon','Pear','avocado','cantaloupe','Banana','Grape'],
          ['raisins','plum','apricot','nectarine','orange','papaya']]
print([name for lst in fruits for name in lst if name.count('a') >= 2])

#计算列表中每个值的平方，自带去重功能
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

#计算列表中每个值的平方，自带去重功能
l = [1,2,3,4,1,-1,-2,3]
squared = {i**2 for i in l}
print(squared)

# 生成平方数的字典
dic1 = {i:i**2 for i in range(1,10)}
print(dic1)

#生成字符及其 ascii 值的字典
s = "Eagle"
dic2 = {i:ord(i) for i in s}#ord() 函数返回一个字符的ASCII码值
print(dic2)

#将一个字典的key和value对调
dic5 = {'a':5,'b':4,'c':3}
print({j:i for i,j in dic5.items()})

#合并大小写对应的value值，将k统一成小写
dic3 = {'a':1,'b':2,'c':3,'A':4,'B':5,'C':6}
dic4 = {i.lower():dic3.get(i.lower(),0)+dic3.get(i.upper(),0) for i in dic3}
print(dic4)


#把列表推导式的的[]换成()就变成了生成器表达式，相比于列表表达式，生成器表达式不会直接产生值，而是需要我们手动去迭代它
gen1 = (i for i in range(1,10))
print(gen1)
for i in gen1:
    print(i)


print('\n'.join('\t'.join(f"{i}x{j}={i*j}" for i in range(1,j+1)) for j in range(1,10)))
