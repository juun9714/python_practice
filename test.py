#20차시 2. 자료구조 – 리스트, 튜플 - 연습문제 22
line=[5, 6, 77, 45, 22, 12, 24]
new=[line[k] for k in range(len(line)) if line[k]%2==1]
print(new)