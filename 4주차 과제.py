
def get_fixed_price(prompt) :
    re = int(input(prompt))
    return re

da1 = int(input('할인율은? '))

agfp = get_fixed_price('A 상품의 할인된 가격은? ')
bgfp = get_fixed_price('B 상품의 할인된 가격은? ')
aresult= agfp / (1-(da1/100))
bresult= bgfp / (1-(da1/100))

print('A 상품의 정가는',aresult)
print('B 상품의 정가는',bresult)


