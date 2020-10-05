
a = []
i = 0
print('Введите 4 числа, три из которых равны между собой, а одно всегда отлично от них')
while i < 4:
    b = int(input())
    a.append(b)
    i += 1

print(a)

if a[0] != a[1]:
    if a[0] != a[2]:
       print('1')
    else:
        if a[1] != a[2]:
            print('2')
else:
    if a[3] != a[0]:
        print('4')
    else:
        print('3')

