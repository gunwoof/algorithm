number = []
for i in range(3) :
    number.append(int(input()))

mulnumber = number[0]*number[1]*number[2]

listnumber=[]
for i in str(mulnumber):
    listnumber.append(i)  

cntnumber = {}
for i in range(10) :
    cntnumber[i] = listnumber.count(str(i))
    print(cntnumber[i])
