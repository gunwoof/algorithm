answer = list(input())
number = {}


for i  in range(len(answer)):
    if answer[i] == "9" :
        answer[i] = "6"

for i in range(len(answer)) :
    if answer[i] not in number.keys():
        number[answer[i]] =1
    else :
        number[answer[i]] += 1

if "6" in number.keys() :
    if number["6"]%2 == 0 :
        number["6"] = number["6"]//2
    else : 
        number["6"] = (number["6"]//2)+1

print(max(number.values()))


