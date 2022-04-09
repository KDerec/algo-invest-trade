import csv
from datetime import datetime


start_timer = datetime.now()


with open("data.csv", newline="") as file:
    has_header = csv.Sniffer().has_header(file.read(1024))
    file.seek(0)
    reader = csv.reader(file)
    if has_header:
        next(reader)
    i = 0
    stocks_list = []
    for row in reader:
        name = row[0]
        cost = int(row[1])
        profitability = int(row[2])
        profit = round(cost * (profitability / 100), 2)

        stock = (name, cost, profit)
        stocks_list.append(stock)
        i += 1
        if i == 20:
            break


def greedy_algo(capital, stocks_list):
    sorted_stocks_list = sorted(stocks_list, key=lambda x: x[2])
    selected_stock = []
    total_cost = 0

    while sorted_stocks_list:
        stock = sorted_stocks_list.pop()
        if stock[1] + total_cost <= capital:
            selected_stock.append(stock)
            total_cost += stock[1]

    total_profit = sum([i[2] * 100 for i in selected_stock]) / 100

    return total_profit, total_cost, selected_stock


total_profit, total_cost, selected_stock = greedy_algo(500, stocks_list)

print(f"Le bénéfice est de {total_profit}€")
print(f"Le coût total est de {total_cost}€")
print(f"Liste des actions sélectionnées :\n{selected_stock}")

end_timer = datetime.now()

print(f"Temps d'exécution du programme : {end_timer - start_timer}")
