from sys import stdin as s

N,M= map(int,s.readline().split())
S=[]
M_list=[]
cnt=0
for _ in range(N):
    S.append(s.readline().strip())

for i in range(M):
    M_list.append(s.readline().strip())


for i in range(len(M_list)):
    if M_list[i] in S:
        cnt+=1
print(cnt)

