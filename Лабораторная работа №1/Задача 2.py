# Задаем значения символов, строк, страниц, обьема дискреты и одного символа
symbols = int(25)
strings = int(50)
page = int(100)
volumesymbol = int(4)
volumediskret = float(1.44)
fullvolume = symbols * strings * page * volumesymbol #Считаем обьем в байтах для одной книги
byte = volumediskret * 1024 * 1024#Переводим из Мб в байты обьем дискреты
books = int(byte // fullvolume)#Считаем сколько книг поместиться с целочисленным делением
print("Количество книг, помещающихся на дискету:", books)