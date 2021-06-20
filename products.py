products = []
while True:
	name = input('輸入商品名稱:')
	if name == 'q':
		break
	price = input('輸入商品價格:')
	products.append([name,price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])