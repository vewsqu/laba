money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен


months = 0

while True:
    budget = salary + money_capital
    if budget < spend:
        break
    months += 1
    money_capital -= (spend - salary)
    spend *= 1.05

print("Количество месяцев, которое можно протянуть без долгов:", months)
