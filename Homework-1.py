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
