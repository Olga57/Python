# Задание 1 - создание списков
info_list=[]
info_list.append('Anna')
info_list.append(123)
info_list.append(50.5)
info_list.append(True)
print(info_list)
print(type(info_list[0]))
print(type(info_list[1]))
print(type(info_list[2]))
print(type(info_list[3]))

# Задание 2 обмен элементов
number_count=int(input('Введите количество элементов: '))
my_list=[]
i=0
while i<number_count:
    my_list.append(int(input('Введите число: ')))
    i+=1
print(my_list)
for number in range(int(len(my_list)/2)):
    my_list[number],my_list[number+1]=my_list[number+1],my_list[number]
    number+=2
print(my_list)

#Задание 3 Месяц в виде числа - время года
month=int(input("Введите номер месяца от 1 до 12: "))
seasons=['winter','spring','summer','autumn']
seasons_dict={1:'winter',2:'spring',3:'summer',4:'autumn'}
if month>=3 and month<=5:
    print('Seasons:',seasons[1])
    print('Seasons:',seasons_dict.get(2))
elif month>=6 and month<=8:
    print('Seasons:',seasons[2])
    print('Seasons:', seasons_dict.get(3))
elif month>=9 and month<=11:
    print('Seasons:',seasons[3])
    print('Seasons:', seasons_dict.get(4))
else:
    print('Seasons:',seasons[0])
    print('Seasons:', seasons_dict.get(1))

#Задание 4 - ввод строки, разбиение строки
my_str=(input('Введите строку:'))
my_words=[]
i=1
for word in range (my_str.count('')+1):
    my_words=my_str.split()
    if len(str(my_words))<=10:
        print(f"{i} {my_words[word]}")
        i+=1
    else:
        print(f"{i} {my_words[word][0:10]}")
        i+=1

#Задание 5 Рейтинг - список

digit=int(input("Введите число: "))
my_list=[4,5,9,8]
while True:
    for el in range(len(my_list)):
      if my_list[el] == digit:
          my_list.insert(el + 1, digit)
          break
      elif my_list[0] < digit:
            my_list.insert(0, digit)
      elif my_list[-1] > digit:
            my_list.append(digit)
      elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
print(f"текущий список {my_list}")

#Задание 6

goods = []
features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
num = 0
feature_ = None
control = None
while True:
    control = input("For quit press 'Q', for continue press 'Enter', for analytics press 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Current analytics \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Input feature "{f}"')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))

goods = int(input("Введите количество товара "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= goods:
    my_dict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
                    'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict(
        {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
         'ед': my_dict.get('ед')})
print(my_list)
print(my_analys)
