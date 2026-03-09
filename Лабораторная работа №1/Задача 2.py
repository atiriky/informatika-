# Задаем значения символов, строк, страниц, обьема дискреты и одного символа
symbols = 25
strings = 50
page = 100
volumesymbol = 4
volumediskret = 1.44
fullvolume = symbols * strings * page * volumesymbol #Считаем обьем в байтах для одной книги
byte = volumediskret * 1024 * 1024#Переводим из Мб в байты обьем дискреты
books = int(byte / fullvolume)#Считаем сколько книг поместиться с целочисленным делением
print("Количество книг, помещающихся на дискету:", books)
