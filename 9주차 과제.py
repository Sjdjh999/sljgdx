shopping_bag = []
sh_count ={}
count=-1
while True:
    item = input('상품명? ')
    if item == '':
        print('장바구니 보기:',sh_count)
        break
    else :
        sh_co= input('수량은? ')
        count+=1
        shopping_bag.append(item)
        sh_count.get(item)
        sh_count[item] = sh_co
        print('장바구니에', shopping_bag[count],sh_count[item],'개 가(이) 담겼습니다.')
        



