'''from sys import stdin as s

def l_sort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if len(arr[min_index]) > len(arr[j]):
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    
N=int(s.readline())
words = []
for i in range(N):
    word=s.readline().rstrip()
    if word not in words:
        words.append(word)

l_sort(words)

i=0
while i < len(words)-1:
    j=i
    while len(words[j]) == len(words[j+1]) :
        j +=1
        if j > len(words)-2:
            break
    word1=sorted(words[i:j+1])
    
    for k in range(i,j+1):
        words[k] = word1[k-i]

    i = j+1
    
for i in words:
    print(i)'''



# 누군가의 깔끔한 코드
n = int(input())
words = []
for _ in range(n):
	words.append(input())
words = list(set(words))

# 아래의 sort함수를 2번써야 사전적 정의로 정렬하고 길이를 기준으로 정렬
words.sort()
words.sort(key = lambda x : len(x)) 

for i in words:
	print(i)


