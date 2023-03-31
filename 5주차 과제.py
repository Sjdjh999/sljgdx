def rep_char(a,b) :
    print(a * b)


def draw_line_string(prompt):
    print(prompt)

name = input(' input his/her name:')
msg1 = '  Hello ' + name
msg2 ='  Welcome to seoul'

if (len(msg1)>len(msg2)) :
    nstr = len(msg1)
else :
    nstr = len(msg2)

rep_char('-',nstr+5)
draw_line_string(msg1)
draw_line_string(msg2)
rep_char('-',nstr+5)

