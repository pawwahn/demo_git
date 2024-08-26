l1 = [1,2,3,1,5,3]
l2 = []
for i in range(1,len(l1)):
    #print(l1[i], l1[i-1])
    if l1[i] > l1[i-1] and l1[i] > l1[i+1]:
        l2.append(l1[i])
print(l2)


