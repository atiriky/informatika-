money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05
mounth = 0
ostatok = 0
while True:#Так как у нас нет конечного месяца, используем бесконечный цикл
    ostatok = spend - salary #Считаем разницу затрат и зарплаты
    if money_capital < ostatok: #Создаем условия для остановки бесконечного цикла
        break

    mounth += 1
    spend *= (1 + increase)
    money_capital -= ostatok

print("Количество месяцев, которое можно протянуть без долгов:", mounth)