alpa={}

for i in range(97,123) :
    alpa[chr(i)] = -1

text = input()
for i in range(len(text)) :
    if text[i] in alpa.keys() and alpa[text[i]] == -1:
        alpa[text[i]]=i

'''a = " ".join(list(map(str,alpa.values())))  
print(a)'''


# 누군가의 깔끔한 코드
# join으로 합치지말고 end=""가 더 깔끔한 듯 하다
for i in alpa.values():
    print(i, end=' ')

