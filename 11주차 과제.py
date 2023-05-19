class point :
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(f'({self.x},{self.y})')
    def set(self,x,y) :
        self.x = x
        self.y = y
    def get(self):
        return (self.x,self.y)

class Rectengle :
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1 #좌측 상단
        self.x2 = x2
        self.y2 = y2 #우측 하단
        it = point(x1,y2)
        rb = point(x2,y2)
    def show(self):
        print('좌측 상단 꼭지점이 ',end='')
        print(f'({self.x1},{self.y1})이고 ',end ='')
        print('우측 하단 꼭지점이 ',end ='')
        print(f'({self.x2},{self.y2})인 사각형입니다.')
    def getWidth(self) :
        width = self.x2 - self.x1
        return width
    def getHeight(self):
        height = self.y2 - self.y1
        return height
    def getArea(self) :
        w = self.getWidth()
        h = self.getHeight()
        result = w * h
        return result
    def getPerimeter(self) :
        w = self.getWidth()
        h = self.getHeight()
        result = (w*2) + (h*2)
        return result

r1 = Rectengle(5,5,20,10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
   
