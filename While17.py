import math
print('Введите число: ')
N = int(input())

while 0 < int(N):
    print(int(math.fmod(N, 10)))
    N /= 10