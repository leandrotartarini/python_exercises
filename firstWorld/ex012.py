p = float(input('What is the price of the product? R$ '))
n = p - (p * 5/100)
print(f'Product used to cost {p}, with 5% discount, it will cost {n:.2f}')