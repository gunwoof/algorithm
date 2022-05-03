from sys import stdin as s

N=int(s.readline())
numbers=[]

for i in range(N):
    numbers.append(int(s.readline()))
numbers.sort()

mean = round(sum(numbers)/N) # 산술평균
median= numbers[int(N/2)] # 중앙값
ran = numbers[N-1]-numbers[0] # 범위

# 최빈값 구하기
cntnumbers=[[],[]] # 값과 개수를 함께 받기
for i in range(len(numbers)):
    if numbers[i] not in cntnumbers[0] :
        cntnumbers[0].append(numbers[i])
        cntnumbers[1].append(1)
    else :
        idx=cntnumbers[0].index(numbers[i])
        cntnumbers[1][idx] +=1

max_of_idx=max(cntnumbers[1]) # 가장 큰 개수의 값
maxidx=cntnumbers[1].index(max_of_idx)
mode=cntnumbers[0][maxidx]
if cntnumbers[1].count(max_of_idx) != 1: # 가장 큰 개수의 값이 2개라면 두번째로 작은수 뽑기
    maxidx_list=list(filter(lambda x:cntnumbers[1][x]==max_of_idx,range(len(cntnumbers[1]))))
    maxidx_minus = maxidx_list[1]
    mode = cntnumbers[0][maxidx_minus]


print(mean)
print(median)
print(mode)
print(ran)