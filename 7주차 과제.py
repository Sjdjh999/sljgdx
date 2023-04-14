def disp_mul_ta(data) :
    count=0
    for n in range(1,10) :
        for i in range(data,data+4) :
            count += 1
            print(f'{i} X {n} = {i*n:2d}', end = '    ')
            if count ==4 :
                count =0
                print()

disp_mul_ta(2)
print()
disp_mul_ta(6)
