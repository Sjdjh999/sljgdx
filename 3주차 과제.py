def exchange(data) :
    f = data // 500
    data %= 500
    print('500원 동전의 개수:',f)
    o = data // 100
    data %= 100
    print('100원 동전의 개수:',o)
    ff = data // 50
    data %=50
    print('50원 동전의 개수:',ff)
    oo = data // 10
    data %=10
    print('10원 동전의 개수:',oo)

def get_integer(prompt) :
    data = int(input(prompt))
    return data

prompt = '동전으로 교환하고자 하는 금액은? '
gi = get_integer(prompt)

print(gi)
print(exchange(gi))
