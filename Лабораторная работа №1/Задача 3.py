list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
# индекс середины
middle_index = len(list_players) // 2 #Количество всех игроков делим на 2 чтобы найти середину
first_team = list_players[:middle_index] #Первая команда до середины
second_team = list_players[middle_index:]#Вторая команда после середины
print(first_team)
print(second_team)
