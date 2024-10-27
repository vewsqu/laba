salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

total_shortage = 0

for month in range(10):
    if month > 0:
        spend *= 1.03

    shortage = max(0, spend - salary)
    total_shortage += shortage

money_capital = total_shortage

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital:.0f}")
