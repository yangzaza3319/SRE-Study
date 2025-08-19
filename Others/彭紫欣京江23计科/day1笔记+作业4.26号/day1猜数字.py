import random
num=random.randint(1,100)
count=0
while True:
    guess=int(input("输入你猜的数字："))
    count+=1
    if guess<num:
        print("猜小了")
        continue
    elif guess>num:
        print("猜大了")
        continue
    break
print("猜对了")
print("一共猜了{count}次".format(count=count))