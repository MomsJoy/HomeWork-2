#Дано целое число N (> 0).
#Используя операции деления нацело и
#взятия остатка от деления,
#найти число, полученное
#при прочтении числа N справа налево.

N = int(input('Введите число: '))
N_mirror = 0
while int(N)>0:
    digit = N % 10
    N_mirror = 10 * N_mirror + digit
    N = N // 10

print("Число справо налево", N_mirror)
