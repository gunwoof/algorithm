number = int(input())
ox = ""

for i in range(number) :
    score = 0 # 총점
    cnt=0 # 연속하면 1오름
    ox = input()
    for j in range(len(ox)) :
        if ox[j] == "O" :
            if cnt == 0 :
                score += 1
                cnt += 1
            elif cnt !=0  :
                score += (1+cnt)
                cnt += 1
        else : 
            cnt = 0
    print(score)
    


