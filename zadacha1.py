#Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

num = input('Введите вещественное число: ')
count=0
for i in range(0,len(num)):
    if num[i]!=',':
        count+=int(num[i])

print(f'{num} -> {count}')