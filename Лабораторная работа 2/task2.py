salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
dolg = 0 # Долг за каждый месяц
money_capital = 0 # Требуемая подушка безопастности
while months != 0:
    if months == 10:
        spend = spend
    else:
        spend = spend + (spend * increase)
    months = months - 1
    dolg = salary - spend
    money_capital = money_capital - dolg
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
months = 10
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
