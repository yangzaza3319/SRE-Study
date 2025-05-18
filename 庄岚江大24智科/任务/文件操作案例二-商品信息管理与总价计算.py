products=[]
with open('b.txt','r',encoding='utf') as f:
    for line in f:
        #去除首尾行空格并分割
        parts = line.strip().split()
        if len(parts) == 3:
            product = {
                'name': parts[0],
                'price': int(parts[1]),
                'amount':  int(parts[2])
            }
            products.append(product)
print("商品列表",products)
total_price = 0
for product in products:
    total_price += product['price'] * product['amount']
print("总价",total_price)