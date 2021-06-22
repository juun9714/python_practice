t=int(input())
big=[]
for i in range(t):
    line=input()
    tmp=[]
    for k in range(10):
        tmp.append(int(line.split(" ")[k]))
    big.append(tmp)

for k in range(t):
    sum=0
    for j in range(10):
        if big[k][j]%2==1:
            sum+=big[k][j]
    print("#{0} {1}".format(k+1,sum))