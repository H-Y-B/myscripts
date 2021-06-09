import sys

tmp   = []
num   = 0
isthis= True

with open(sys.argv[1]) as f:
    lines = f.readlines()

for line in lines:
    isthis = True
    for look in sys.argv[2:]:
        if look.find(r"-")>=0:
            isthis = isthis and not (look[1:] in line)
        else:
            isthis = isthis and (look in line)

    if isthis:
        tmp.append(line)

for t in tmp:
    num+=1
    print(t),

print(num)
            

