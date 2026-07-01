n = int(input())
k = int(input())
l2 = [i+1 for i in range(n)]
while len(l2)>1:
    for i in range(k-1):
        temp=l2.pop(0)
        l2.append(temp)
    l2.pop(0)
    print(l2[0])