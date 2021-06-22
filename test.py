# 35차시 3. 자료구조 – 셋, 딕셔너리 - 연습문제 10
# line=input()
# dic={}
# for k in range(len(line)):
#     if dic.get(line[k])==None:
#         dic[line[k]]=1
#     else:
#         dic[line[k]]+=1

# for k,v in dic.items():
#     print(str(k)+","+str(v))

# 37차시 4. 문자열 - 연습문제 1
# line=input()
# rev_line=line[::-1]
# if line==rev_line:
#     print(rev_line)
#     print("입력하신 단어는 회문(Palindrome)입니다.")

# 38차시 4. 문자열 - 연습문제 2
# line=input()
# li=line.split(' ')
# for k in range(len(li)):
#     print(li[2-k],end=" ")

# 39차시 4. 문자열 - 연습문제 3
# line=input()
# result={}
# result["protocol"]=line.split("://")[0]
# result["host"]=line.split("/")[2]
# result["others"]=line.split("/")[3]
# for k,v in result.items():
#     print(k+": "+str(v))

# 40차시 4. 문자열 - 연습문제 4
# a=input()
# b=input()
# c=input()

# print(">> "+a.upper())
# print(">> "+b.upper())
# print(">> "+c.upper())

# 41차시 4. 문자열 - 연습문제 5
line=input()
tmp=sorted(list(set(line.split(' '))))

for k in range(len(tmp)):
    if k==len(tmp)-1:
        print(tmp[k])
    else:
        print(tmp[k],end=",")
