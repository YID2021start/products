import os #operating system作業系統
products = []
if os.path.isfile('products.csv'):
	print('水唷!找到了!')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:         #去除/n
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('裝肖偉喔?找不到啊!')


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


with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + '的價格是' + p[1] + '\n')

price = int(price)
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')