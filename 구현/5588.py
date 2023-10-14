# 브루트 포스로 한 번씩 다 빼기
# counter로 개수파악
# most_common으로 가장 높은 것 출력
# Tip : comprehension이 for문 시간이 빠름

from sys import stdin as s
from collections import Counter as c

# 입력
m=int(s.readline())
key=[list(map(int,s.readline().split())) for _ in range(m)]

n=int(s.readline())
challange=[list(map(int,s.readline().split())) for _ in range(n)]


arr=[(challange[j][0]-key[i][0],challange[j][1]-key[i][1]) for i in range(m) for j in range(n)]
arr_dic=c(arr)
print(arr_dic.most_common()[0][0][0],arr_dic.most_common()[0][0][1])



