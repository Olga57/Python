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

#Задание 5
revenue=float(input('Введите выручку фирмы: '))
costs=float(input('Введите издержки фирмы: '))
profit=revenue-costs
if revenue>costs:
    print(f'Фирма работает с прибылью. Рентабельность выручки составила {profit/costs: .2f}')
    number_staff=int(input('Введите количество сотрудников фирмы: '))
    print(f'Прибыль на одного сотрудника составила {profit/number_staff:.2f}')
elif revenue==costs:
    print('Фирма работает в ноль')
else:
    print('Фирма работает с убытком')

#Задание 6
a=int(input('Введите результаты пробежки первого дня в км: '))
b=int(input('Введите общий желаемый результат в км: ' ))
i=0
while a<=b:
    print(f'{i}-ый день:{a:2f}')
    a=a+(a*0.1)
    i=i+1
else:
    print(f'{i}-ый день:{a:2f}')
    print(f'Ответ:на {i}-ый день спортсмен достиг результата - не менее {b}км.')






