products = [] #大清單
while  Ture:
	name = input('')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	products.append([name, price])
print(products)
