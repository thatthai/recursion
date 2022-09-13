def sorted(l1,l2, n,m): #n is len in list , l is list
    if n == 0:
        return l2
    if n == 1 and len(l2) == 0:
        l2.append(l1[0])
        return l2
    else:
        if len(l2) == 0 :
            l2.append(l1[n-1])
        elif l1[n-1] >= l2[m]:
            l2.insert(m,l1[n-1])
            m = 0            
        elif l1[n-1] > l2[-1]:
            m += 1
            return sorted(l1,l2,n,m)
        else :
            l2.append(l1[n-1])
        return sorted(l1,l2,n-1,m)


inp = input("Enter your List : ").split(',')
l1 = []
l2 = []
for item in inp :
    l1.append(int(item))
print("List after Sorted : {0}".format(sorted(l1,l2,len(l1),0)))