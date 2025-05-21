a = open('a.txt', 'w', encoding='utf-8')
a.write("hello my world")
a.close()
products = []
with open('a.txt','r',encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 3:
            product = {
                'name': parts[0],
                "price": int(parts[1]),
                'amount': int(parts[2])

            }
            products.append(product)

print("商品列表", products)

total = 0
for i in products:
    total += i['price'] * i['amount']

print("总价：", total)
