print("Описаие процедуры Swap(X, Y)")
X=(int(input ("X = ")))
Y=(int(input ("Y = ")))
tmp=X
X=Y
Y=tmp
print("X=",X)
print("Y=",Y)
print("Сама процедура")
A=(int(input ("A = ")))
B=(int(input ("B = ")))
C=(int(input ("C = ")))
D=(int(input ("D = ")))
print(A,B,C,D)
A,B=B,A
C,D=D,C
B,C=C,B
print("A=",A)
print("B=",B)
print("C=",C)
print("D=",D)
