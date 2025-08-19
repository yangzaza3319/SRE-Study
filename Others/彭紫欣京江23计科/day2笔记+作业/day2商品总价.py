#定义一个空列表
products = []
with open('a2.txt','r',encoding='utf-8') as file:
    for i in file.readlines():
        products.append(i.strip().split()) # 去除行首尾空白并分割

total_price=0
for j in products:
    single_product_price = int(j[1]) * int(j[2])
    total_price = total_price + single_product_price
print("所有商品的总价是", total_price)