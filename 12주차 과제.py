import os
import pickle
scores =[]
filename = 'score.bin'
def input_score():
    count =1
    print('[점수 입력]')
    while True :
        data = int(input(f'#{count}? '))
        if data > 0 :
            scores.append(data)
            count+=1
        else :
            break
def get_average():

    result = sum(scores) / len(scores)
    return result

def show_scores():
    print('\n[점수 출력]')
    print(f'개인 점수: ', end ='')
    temps = scores.copy()
    for i in temps:
              
        print(i,end = ' ')        
    print(f'\n평균:{get_average()}')
   

def find_scores(lst):
    print('\n[검색]')
    find = int(input('찾고자 하는 점수는?'))
    if find in lst :
        print(f'{find}점은 {lst.index(find) +1}번 학생의 점수입니다')
    else :
        print(f'{find}점을 받은 학생은 없습니다.')
        
def save_data(filepath):
    with open (filepath,'wb')as file:
        pickle.dump(scores,file)

def load_data(filepath):
    with open(filepath,'rb')as file:

        global scores
        scores = pickle.load(file)
     
if os.path.exists(filename) :
    print('[파일 읽기]')
    load_data(filename)
    show_scores()
    scores =[]
else :
    scores = []
    
    

input_score()
show_scores()
find_scores(scores)
save_data(filename)
