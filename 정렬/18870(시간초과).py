from sys import stdin as s

N=int(s.readline())
numbers=list(map(int,s.readline().split()))

# 중복제거하고 정렬
numbers_not_dupl=list(set(numbers))
numbers_not_dupl.sort()

# 딕셔너리의 key와 value를 이용하여 본래 입렬된 순서대로 출력
numbers_dic={numbers_not_dupl[i]:i for i in range(len(numbers_not_dupl))}
for i in numbers:
    print(numbers_dic[i],end=" ")



'''# 시간초과 코드
from sys import stdin as s

N=int(s.readline())
numbers=[[],[0 for i in range(N)]]
numbers[0]=list(map(int,s.readline().split()))

for i in range(N):
    for j in range(i+1,N):
        if numbers[0][i]>numbers[0][j] :
            if (numbers[0]).count(numbers[0][j]) != 1:
                numbers[1][i] += 1/(numbers[0]).count(numbers[0][j])
            else:
                numbers[1][i] +=1

for i in range(N-1,-1,-1):
    for j in range(i-1,-1,-1):
        if numbers[0][i]>numbers[0][j] :
            if (numbers[0]).count(numbers[0][j]) != 1:
                numbers[1][i] += 1/(numbers[0]).count(numbers[0][j])
            else:
                numbers[1][i] +=1

print_cnt=list(map(int,numbers[1]))
for i in print_cnt:
    print(i,end=" ")'''
