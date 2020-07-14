#Задание 1
name = 'Анна'
period = '10'
number = '5,3'
result= 'True'
report = 'None'

print(name)
print(period)
print(number)
print(result)
print(report)


name = str(input('Введите Ваше имя: '))
print(name)

age = int(input('Сколько Вам лет? '))
print(age)

city = str(input('В каком городе Вы живете? '))
print(city)

#Задание 2
second=int(input('Введите секунды: '))
hour=((second//3600))%24
minute=(second//60)%60
second=second%60
print('{0}:{1:02}:{2:02}'.format(hour,minute,second))

#Задание 3
n=int(input('Введите n: '))
num=str(n)
n1=num+num
n2=num+num+num
total=n+int(n1)+int(n2)
print('Результат равен: ',total)

#Задание 4
a=int(input('Введите целое положительное число: '))
m=a%10
a=a//10
while a>10:
    if a%10>m:
        m=a%10
    a=a//10
print(m)
