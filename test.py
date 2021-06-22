#23차시 2. 자료구조 – 리스트, 튜플 - 연습문제 25
# line=[12, 24, 35, 70, 88, 120, 155]
# new=[line[k] for k in range(len(line)) if k!=0 and k!=4 and k!=5]
# print(new)



#24차시 2. 자료구조 – 리스트, 튜플 - 연습문제 26
# one=set([1,3,6,78,35,55])
# two=set([12,24,35,24,88,120,155])
# result=list(one&two)
# print(result)



#25차시 2. 자료구조 – 리스트, 튜플 - 연습문제 27
# def re(data):
#     no_re=set(data)
#     return list(no_re)

# data=[12,24,35,24,88,120,155,88,120,155]
# new=re(data)
# print(sorted(new))



#27차시 3. 자료구조 – 셋, 딕셔너리 - 연습문제 2

# student={"홍길동": "010-1111-1111","이순신": "010-1111-2222","강감찬": "010-1111-3333"}

# print("아래 학생들의 전화번호를 조회할 수 있습니다.")
# for k in student.keys():
#     print(k)
# print("전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.")
# name=input()

# for k,v in student.items():
#     if name==k:
#         print("{0}의 전화번호는 {1}입니다.".format(name,v))



# 28차시 3. 자료구조 – 셋, 딕셔너리 - 연습문제 3

product={"TV": 2000000, "냉장고": 1500000, "책상": 350000, "노트북": 1200000, "가스레인지": 200000, "세탁기": 1000000}
new=sorted(product.items(),key=(lambda x : x[1]), reverse=True)
for k in range(len(new)):
    print(new[k][0]+": "+str(new[k][1]))

    