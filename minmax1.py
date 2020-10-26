print("Введите n")
n = int(input())
print("Введите числа")
n_list = [int(input()) for _ in range(n)]
a=n_list
print("Max value is:" , max(a))
print("Min value is:" , min(a))