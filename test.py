# 17차시 2. 자료구조 – 리스트, 튜플 - 연습문제 19
# line = input()
# lines=list(line.split(", "))
# new=sorted(lines)

# for k in range(0, len(new)):
#     if k==len(new)-1:
#         print(new[k])
#     else:
#         print(new[k],end=", ")

#18차시 2. 자료구조 – 리스트, 튜플 - 연습문제 20

#split
# line=input()
# lines=list(map(int,line.split(", ")))

# new=[k for k in lines if k%2==1]
# print(str(new)[1:-1])

#19차시 2. 자료구조 – 리스트, 튜플 - 연습문제 21

t=(1,2,3,4,5,6,7,8,9,10)
t1=t[:(len(t)//2)]
t2=t[(len(t)//2):]

print(t1)
print(t2)