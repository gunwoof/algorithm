from sys import stdin as s

form = list(s.readline().rstrip())
temstge=[]
N_extraction=[] # 숫자 저장
S_extraction = ["x"] # 부호 저장
sum=0
minus=0 # -"-"시점부터 끝까지 더할 변수

for i in range(len(form)):
    if form[i] != "-" and form[i] != "+" :
        temstge.append(form[i])
        if i == len(form)-1:
            N_extraction.append(int("".join(temstge)))
    else :
        N_extraction.append(int("".join(temstge)))
        temstge.clear()
        S_extraction.append(form[i])


S_index=S_extraction.index("-")
if "-" in S_extraction: # 식에 "-"가 있는것과 없는 것을 구분
    for i in range(S_index):
        sum += N_extraction[i]
    for i in range(S_index,len(N_extraction)) : # "-"가 있다면 "-"시점부터 끝까지 더해서 한번에 뺌
        minus += N_extraction[i]
    sum -= minus
else : # "-"가 없다면 그냥 끝까지 더함
    for i in range(len(N_extraction)) :
        sum += N_extraction[i]

print(sum)



# 누군가의 깔끔한 코드
arr = input().split('-')
hap = 0
for i in arr[0].split('+'): # "-"가 나온 시점까지 더하기
    hap += int(i)

for i in arr[1:]:
    for j in i.split('+'): # "-"가 나온 시점부터 끝까지 더해서 한번에 빼기
        hap -= int(j)

print(hap)