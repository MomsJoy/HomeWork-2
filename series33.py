k = int(input('Введите целое число K: '))
n = int(input('Введите целое число N: '))

listlist = []
a = []
i = 0
j = 1
while i < abs(k):
    print('Введите в список N целых чисел')
    while j <= n:
        b = int(input())
        a.append(b)
        j += 1
    listlist.append(a.copy())
    a.clear()
    i += 1
    j = 1

print(listlist)

for elem in (listlist):
    j = 0
    b = 0
    for j in range(len(elem)):
        if elem[j] == 2:
            b = j+1
        j += 1
    print(b)































