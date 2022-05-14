n = int(input())
'''chess =[[]]*n

for i in range(n) :
    chess[i].append(0)'''
chess = [[0 for i in range(n)] for j in range(n)]
print(chess)
for i in range(n) :

    for j in range(n):
        chess[i][j] = i
        chess[j][i] = i
        if i-j >=0 and i+j <=n-1 :
            chess[i+j][i+j] = i
        if i-j >=0 and i+j <=n-1 :
            chess[i-j][i-j] = i
        if i-j >=0 and i+j <=n-1 :
            chess[i+j][i-j] = i
        if i-j >=0 and i+j <=n-1 :
            chess[i-j][i+j] = i
        




print(chess)
