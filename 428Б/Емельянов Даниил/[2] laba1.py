import datetime as dt
import random
import queue

#исходные данные (Чего надо, хозяин?)

#1) предметы в школьном аттестате (не меньше 14), как словарь (dictionary) из названия и оценки (можно выдумать)

attest = {"Русский язык" : 5,
          "Литература" : 4,
          "Алгебра" : 5,
          "Геометрия" : 3,
          "Физика" : 5,
          "Химия" : 3,
          "География" : 4,
          "История" : 4,
          "Обществознание" : 4,
          "ОБЖ" : 5,
          "Иностранный язык" : 4,
          "Физическая культура" : 5,
          "ИЗО" : 3,
          "Технология" : 5}

#2) полное имя с фамилией и дату рождения любого актера из вестерна 1960х годов как кортеж (tuple);

western = ('Джон', 'Уэйн', dt.datetime(1907, 5, 26)) #КОРТЕЖ ЖЕ! РАЗНЫЕ ТИПЫ ДАННЫХ!

#3) список (list) из имени и фамилии, составленные случайно по таблице из самых популярных (с сайта http://topnamesinrussia.tilda.ws), свой город взять по номеру равному дню в месяце вашего рождения,длина списка не меньше 30 элементов (имя + фамилия);

# №1 - Москва
name = ["Иван",
        "Александр",
        "Сергей",
        "Андрей",
        "Дмитрий",
        "Алексей",
        "Максим",
        "Михаил"
        ]
surname = ["Иванов",
          "Петров",
          "Смирнов",
          "Сергеев",
          "Волков",
          "Кузнецов",
          "Васильев",
          "Романов"
          ]

fullname = []

for i in range(0, 30):
    randomname = random.choice(name)
    randomsurname = random.choice(surname)
    fullname.append(randomname)
    fullname.append(randomsurname)


#4) имя из прилагательного и существительного, которое вы бы дали своему домашнему тамандуа (строка).
creature = "Evil Dog"

#Работа (готов вкалывать)

print("Готов вкалывать!")

#1) вывести среднюю оценку в аттестате;
suma = sum(attest.values())
count = len(attest)
average = round(suma/count,2)
print("1) Средний балл равен", average)

#2) вывести уникальные имена среди взятых из таблицы популярных;

uniquenames = []

for i in range(1, len(fullname)):
    name1 = fullname[i-1]
    surname1 = fullname[i] 
    fullname1 = name1 + " " + surname1
    #print(fullname1)
    if fullname1 not in uniquenames and fullname1 != ' ':
        uniquenames.append(fullname1)
    else:
        continue
    
print("2) Список уникальных имён:", uniquenames)

#3) общая длина всех названий предметов;
fullength = 0
for i in attest.keys(): #цикл завязан на 'ключах' словаря
    fullength += len(i)
print("3) Полная длина равна", fullength, "символов")

#4) уникальные буквы в названиях предметов;

res = []
for key in attest.keys():
    for i in range(len(key)):
        if key[i].upper() not in res and key[i] != ' ':
           res.append(key[i].upper())
        else:
            continue 
print("4) Уникальные буквы: \n", res)

#5) имя вашего домашнего тамандуа в бинарном виде;
string = ""
for i in creature:
    da_ascii = ord(i)
    da_bin = format(da_ascii, "08b")
    string += da_bin
print("5) Имя в двоичном виде:", string)

#6) количество дней от даты рождения актера вестерна до текущей даты (должна быть всегда актуальной);

timer = dt.datetime.today() - western[2]
print("6) Разница в днях:", timer)

#7) FIFO очередь, в которую можно добавлять строковые названия стройматериалов, вводимые с клавиатуры (до команды остановки), после введения - вывести все;

print("Введите 'СТОП' для остановки")

matlist = []
matqueue = queue.Queue()
GAR = True

while GAR == True:
    material = input()
    if material == 'СТОП':
        GAR = False
    matqueue.put(material) 
    matlist.append(material)
    #print(matlist)
if len(matlist) > 1:
    print("7) Получи и распишись!")
    print(matlist[:len(matlist)-1])

else:
    print("7) Ничего строить не собираешься? Странно...")
    print(matlist[:len(matlist)-1])
    
#8) по введеному с клавиатуры индексу, поменять имя в отсортированном списке популярных имен и фамилий на имя, под которым наиболее известен, китайский император династии Чжоу (смотреть по списку всех на странице императоров Китая) под номером, получаемым из даты рождения актера вестерна: number = (day + month**2 + year) % 39 + 1;
#16 Чжоу Чжуан-Ван
print("Введите номер элемента, который вы хотите заменить, от 1 до", len(name))
choose1 = int(input())
name[choose1-1] = "Чжоу Чжуан-Ван"
surname[choose1-1] = "Чжоу Чжуан-Ван"
print("8) Ваши изменения приняты:\n", name,"\n", surname, "\n")

#9) создать и напечатать связный список странных названий населенных пунктов любым способом (например, как словарь, где ключ - имя, а значение -- ссылка на индекс следующего элемента), удалить элемент по введеному с клавиатуры названию, вставить город "Конец" в указанное с клавиатуры место по индексу (города можно взять, например, тут).
towns = ["Шейди Сэндс",
         "Джанктаун",
         "Хаб",
         "Могильник",
         "Арройо",
         "Кламат",
         "Дыра",
         "Модок",
         "Гекко",
         "Город Убежища",
         "Брокен-Хиллс",
         "Реддинг",
         "Нью-Рино",
         "Наварро"]

print("Введите номер элемента, который вы хотите убрать, от 1 до", len(towns))
choose2 = int(input())
towns.pop(choose2-1)
print("9.1) Ваши изменения приняты:\n", towns,"\n")

print("Введите номер элемента, который вы хотите заменить, от 1 до", len(towns))
choose3 = int(input())
towns[choose3-1] = "Конец"
print("9.2) Ваши изменения приняты:\n", towns,"\n")

print("Дело сделано!")
