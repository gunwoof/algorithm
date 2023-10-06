from sys import stdin as s

std_number=int(s.readline())
std_arr=list(map(int,s.readline().split()))
count=int(s.readline())
arr=[]

for _ in range(count):
    arr.append(list(map(int,s.readline().split())))

# 반대길로 가능 정답 list만들기
reverse_std_arr=[]
for i in range(len(std_arr)):
    if std_arr[i] == 1:
       reverse_std_arr.append(3) 
    if std_arr[i] == 2:
       reverse_std_arr.append(4)
    if std_arr[i] == 3:
       reverse_std_arr.append(1)
    if std_arr[i] == 4:
       reverse_std_arr.append(2)
reverse_std_arr=list(reversed(reverse_std_arr))

resurt=0
answer=[]
# 정방향
for i in range(count):
    for j in range(len(arr[i])):
        
        if std_arr == arr[i][j:std_number+j+1] or reverse_std_arr == arr[i][j:std_number+j]:
            resurt+=1
            answer.append(arr[i][0:std_number])
            break
        else : 
            arr[i].append(arr[i][j])



print(resurt)
for i in answer:
    for j in i:
        print(j,end=" ")
    print()