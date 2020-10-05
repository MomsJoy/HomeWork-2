# Даны два целых числа A и B (A<B).
# Найти произведение всех целых чисел от A до B включительно.

a = int(input("А:"))
b = int(input("В:"))
s=0
for i in range(a,b+1):
    s += i
    print(s)