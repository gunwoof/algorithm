from sys import stdin as s

def man(num,switch,switch_num):
    for i in range(num,switch_num+1,num):
        #print(switch[i])
        if switch[i-1] == 1:
            switch[i-1] = 0
        else :
            switch[i-1] = 1
        
def woman(num,switch,switch_num):

    if switch[num-1] ==1:
        switch[num-1] = 0
    else :
        switch[num-1] = 1
    # switch가 처음이거나 마지막이면 그 스위치만 바꾸로 함수 종료
    if num == 1 or num == switch_num:
        return
    
    i,j = 2,0
    while 1:
        if switch[num-i] == switch[num+j]:
            if switch[num-i] ==1:
                switch[num-i] = 0
            else :
                switch[num-i] = 1

            if switch[num+j] ==1:
                switch[num+j] = 0
            else :
                switch[num+j] = 1

            i += 1
            j += 1
        else :
            return
        

        # 끝에 다달으면 함수 마무리
        if num-i == -1 or num+j == switch_num:
            return


switch_num=int(s.readline())
switch=list(map(int,s.readline().split()))
human_num=int(s.readline())

for _ in range(human_num):
    command=list(map(int,s.readline().split()))
    if command[0] == 1:
        man(command[1],switch,switch_num)
    else :
        woman(command[1],switch,switch_num)


for i in range(len(switch)):
    print(switch[i],end=" ")
    # 20개 넘으면 줄바꿈
    if (i+1) % 20 ==0:
        print()