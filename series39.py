k = int(input('Введите целое число K: '))

listlist = []
a = []
i = 1

while i <= abs(k):
    print('Введите в список минимум два целых числа, отличных от нуля(0 - незначимое число, означающее конец списка)')
    while True:
        b = int(input())
        a.append(b)
        if b == 0:
            if len(a) == 2:
                a.remove(0)
                print('Список не может содержать меньше двух целых чисел, отличных от нуля')
            else:
                break
    listlist.append(a.copy())
    a.clear()
    i += 1

print(listlist)

d = 0

for elem in (listlist):
    j = 0
    for j in range(len(elem)-3):
        if elem[j] > elem[j+1]:
            j += 1
        else:
            break
    if elem[j] > elem[j+1]:
        d = 1

c = 0

for elem in (listlist):
    j = 0
    for j in range(len(elem)-3):
        if elem[j] < elem[j+1]:
            j += 1
        else:
            break
    if elem[j] < elem[j+1]:
        c = 1

if d == 0 and c == 0:
    print('0')
if d == 1:
    print('-1')
if c == 1:
    print('1')






























