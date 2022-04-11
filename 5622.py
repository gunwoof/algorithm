text = list(input())
numstr = {
    2:["A","B","C"],
    3:["D","E","F"],
    4:["G","H","I"],
    5:["J","K","L"],
    6:["M","N","O"],
    7:["P","Q","R","S"],
    8:["T","U","V"],
    9:["W","X","Y","Z"]
}
time = 0

for i in range(len(text)) :
    for j in range(2,10) :
        if text[i] in list(numstr.values())[j-2] :
            time += j+1
            break
print(time)


# 누군가의 깔끔한 코드
'''str = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
str_a = input()
res = 0
for j in range(0,len(str_a)):
    for i in str: # in 연산자는 문자열도 가능
        if str_a[j] in i:
            res += str.index(i)+3
print(res)'''