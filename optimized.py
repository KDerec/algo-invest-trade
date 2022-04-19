import csv
from datetime import datetime


start_timer = datetime.now()


class Stock:
    def __init__(self, name, cost, profitability):
        self.name = name
        self.cost = int(cost)
        self.profitability = int(profitability)
        self.profit = round(self.cost * (self.profitability / 100), 2)


with open("data.csv", newline="") as file:
    has_header = csv.Sniffer().has_header(file.read(1024))
    file.seek(0)
    reader = csv.reader(file)
    if has_header:
        next(reader)
    stocks_list = []
    for row in reader:
        name = row[0]
        cost = row[1]
        profitability = row[2]
        stock = Stock(name, cost, profitability)
        stocks_list.append(stock)


def optimized_algo(capital, stocks_list):
    table = [[0 for x in range(capital + 1)] for x in range(len(stocks_list) + 1)]

    for i in range(1, len(stocks_list) + 1):
        for w in range(1, capital + 1):
            if stocks_list[i - 1].cost <= w:
                table[i][w] = max(
                    stocks_list[i - 1].profit
                    + table[i - 1][w - stocks_list[i - 1].cost],
                    table[i - 1][w],
                )
            else:
                table[i][w] = table[i - 1][w]

    w = capital
    n = len(stocks_list)
    stocks_selection = []

    while w >= 0 and n >= 0:
        stock = stocks_list[n - 1]
        if table[n][w] == table[n - 1][w - stock.cost] + stock.profit:
            stocks_selection.append(stock)
            w -= stock.cost

        n -= 1

    return round(table[-1][-1], 2), stocks_selection


capital = 500

best_profit, stocks_result = optimized_algo(capital, stocks_list)
list_to_display = []
capital_depense = 0

for stock in stocks_result:
    list_to_display.append(stock.name)
    capital_depense += stock.cost

print(f"Le montant du bénéfice est de {best_profit}€.")
print(f"La liste d'action est : {list_to_display}")
print(f"Le montant de l'investissement est de {capital_depense}€.")

end_timer = datetime.now()

print(f"Temps d'exécution du programme : {end_timer - start_timer}")
