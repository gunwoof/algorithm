text = input().upper()

cnt = {} # 알파벳:개수 딕셔러니

for i in range(len(text)) :
    if text[i] not in cnt.keys() :
        cnt[text[i]] = 1
    else :
        cnt[text[i]] = cnt[text[i]] +1

check = list(cnt.values()) # 각 알파벳의 개수만 

maxCnt = check.count(max(check)) # 알파벳 최고개수가 한개 인지 여러개 인지 

key=[] # 알파벳(딕셔너리 쪼갬)
item=[] # 개수(딕셔너리 쪼갬)

if maxCnt != 1 :
    print("?")
    exit()
else : 
    for i, j in cnt.items() :
        key.append(i)
        item.append(j)
        
answer = item.index(max(check)) # 개수가 제일 높은 알파벳의 index
print(key[answer])   


# 누군가의 깔끔한 코드
string = input().upper()

count, alphabet = 0, ''
alphabets = {}

for c in string:
    if c in alphabets:
        alphabets[c] += 1
    else:
        alphabets[c] = 1

for k, v in alphabets.items(): # max()에 너무 의존한 나머지 좋은 방법을 놓침
    if v > count:
        alphabet = k
        count = v
    elif v == count:
        alphabet = '?'

print(alphabet)