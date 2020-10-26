print("Описаие процедуры SortDec(X, Y)")
X=(int(input ("X = ")))
Y=(int(input ("Y = ")))
if X<Y:
    tmp=X
    X=Y
    Y=tmp
else:
    print("Условие не верно")  
print("X=",X)
print("Y=",Y)

print("Сама процедура")
print('Введите первый набор переменных: ')
A1=(int(input ("A1 = ")))
B1=(int(input ("B1 = ")))
C1=(int(input ("C1 = ")))
a1=A1
b1=B1
c1=C1
sortik1=[a1,b1,c1]
sortik11=sorted(sortik1 , reverse=True)
print(sortik11)

print('Введите второй набор переменных: ')
A2=(int(input ("A2 = ")))
B2=(int(input ("B2 = ")))
C2=(int(input ("C2 = ")))
a2=A2
b2=B2
c2=C2
sortik2=[a2,b2,c2]
sortik22=sorted(sortik2 , reverse=True)
print(sortik22)