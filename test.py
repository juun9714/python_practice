#22차시 2. 자료구조 – 리스트, 튜플 - 연습문제 24
result=[]
for i in range(2):
    tmp1=[]
    for j in range(3):
        tmp2=[]
        for k in range(4):
            tmp2.append(0) #append zero
        tmp1.append(tmp2)
    result.append(tmp1)
    
print(result)