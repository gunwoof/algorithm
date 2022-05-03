number = int(input())
cfnumber=[] # 숫자의 자리를 쪼개서 각 방에 넣음
cnt =0
ox=1 # 한수인지 체크

for i in range(1,number+1) :
    
    if i <100 : # 99까지는 모두 한수
        cnt +=1
        continue
    
    a = str(i)
    for j in a: # 숫자의 자리를 쪼개서 각 방에 넣음
        cfnumber.append(int(j))
    
    for j in range(len(cfnumber)-2) : # 각 자리가 등차수열인지 체크
        if cfnumber[j] - cfnumber[j+1] != cfnumber[j+1] - cfnumber[j+2] :
            ox=0

    if ox==1 : # 한수 체크
        cnt +=1
    else :
        ox=1

    cfnumber.clear() # 다음 수를 위해 리셋

print(cnt)
    
    

