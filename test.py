# 32차시 3. 자료구조 – 셋, 딕셔너리 - 연습문제 8
# line=input()
# lower=0
# upper=0
# for k in range(len(line)):
#     if 97<=ord(line[k])<=122:
#         lower+=1
#     elif 65<=ord(line[k])<=90:
#         upper+=1

# print("UPPER CASE "+str(upper))
# print("LOWER CASE "+str(lower))

#34차시 3. 자료구조 – 셋, 딕셔너리 - 연습문제 9

beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
print(beer)
beer={k:v*1.05 for k,v in beer.items()}
print(beer)
