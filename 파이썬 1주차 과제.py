def get_radius(prompt) :
    r = int(input(prompt))
    return r
def get_circle_area(r):
    result = r*r*3.14
    return result

gr = get_radius('넓이를 구하고자 하는 원의 반지름은? ')
print(gr)
gca = get_circle_area(gr)
print('반지름',gr,'인 원의 넓이 = 3.14 X',gr,'X',gr,'=',gca)
