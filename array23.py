lst = list(range(15))
k = int(input('k='))
l = int(input('l='))

del lst[k:l+1: ]
print(lst)
print(sum(lst)/len(lst))
