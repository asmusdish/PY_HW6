# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

num = int(input("Введите кол-во элементов: "))
list = []

for _ in range(num):
    list.append(int(input("Введите число: ")))
min = int(input("Введите минимум: "))
max = int(input("Введите максимум: "))
listout = []
for i in range(len(list)):
    if list[i] >= min and list[i] <= max:
        listout.append(i)

print(list)
print(listout)