shopping_bag = {}

def buy(lst):
    print('[구입]')
    item = input('상품명? ')
    if item == '':
        return False
    else :
        sh_co= input('수량은? ')
        lst.get(item)
        lst[item] = sh_co
        print(f'장바구니에 {item} {lst[item]}개가(이) 담겼습니다.')
        

def show(lst):
    print('장바구니 보기:',lst)

def find(lst):
    print('[검색]')
    find_sh = input('장바구니에서 확인하고자 하는 상품은? ')
    if find_sh in lst:
        print(f'{find_sh}(는) {lst[find_sh]}개 담겨 있습니다.') 
    else :
        print(f'장바구니에 {find_sh}은(는) 없습니다.')
               
    
while True :
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)




































    



