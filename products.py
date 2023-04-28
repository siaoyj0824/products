products = [] #大清單
while  Ture:
	name = input('')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = [] #小清單 
	p.append(name) #小清單裡裝的東西
	p.append(price)
	products.append(name)
print(products)

products[0][0]