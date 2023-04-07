
def read_single_digit(data,n):
    if data[n] == '1':
        print('일',end =' ')
    elif data[n] == '2':
        print('이',end =' ')
    elif data[n] == '3':
        print('삼',end =' ')
    elif data[n] == '4':
        print('사',end =' ')
    elif data[n] == '5':
        print('오',end =' ')
    elif data[n] == '6':
        print('육',end =' ')
    elif data[n] == '7':
        print('칠',end =' ')
    elif data[n] == '8':
        print('팔',end =' ')
    elif data[n] == '9':
        print('구',end =' ')
    else :
        print('영',end =' ')


def read_number(num):
    read_single_digit(num,0)
    read_single_digit(num,1)
    read_single_digit(num,2)
    
num = input('세자리 정수 입력: ')
read_number(num)

