line = input()
lines=list(line.split(", "))
new=sorted(lines)

for k in range(0, len(new)):
    if k==len(new)-1:
        print(new[k])
    else:
        print(new[k],end=", ")