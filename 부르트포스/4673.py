numbers = []
for i in range(1,10000) :
   numbers.append(i)

for n in numbers : # 1~10000까지의 완전 탐색
    while n < 10001 : # 하나의 생성자로 부터 나오는 숫자를 삭제(~10000까지)
        conNumber = n
        sharenumber =n
        while sharenumber >= 1 : # 생성자 만들기
            remain = sharenumber%10
            sharenumber= sharenumber//10

            conNumber += remain
        
        if conNumber in numbers :
            numbers.remove(conNumber)
        
        n = conNumber 

for i in numbers :
    print(i)



# 누군가의 깔끔한 코드(각 자리를 더하는 코드)
# 숫자->문자열로 쪼갬->각 인덱스별로 더함
for num in numbers :
    for n in str(num):
        num += int(n)
        




