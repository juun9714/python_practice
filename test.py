#29차시 3. 자료구조 – 셋, 딕셔너리 - 연습문제 4
# a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
# b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}
# b.update(a)

# result=set(filter(lambda item:item[1]>=3000, b.items()))
# print(result)


#30차시 3. 자료구조 – 셋, 딕셔너리 - 연습문제 5
# fruit = ['   apple    ','banana','  melon']
# fruit=[fruit[k].strip() for k in range(len(fruit))]

# dic={fruit[k]:len(fruit[k]) for k in range(len(fruit))}
# print(dic)

#31차시 3. 자료구조 – 셋, 딕셔너리 - 연습문제 6
num = int(input())
dic={}
for k in range(1,num+1):
    dic[k]=pow(k,2)

print(dic)