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


def bruteforce_algo(capital, stocks_list, stocks_selection=[]):
    if stocks_list:
        profit_solution1, stocks_list_solution1 = bruteforce_algo(
            capital, stocks_list[1:], stocks_selection
        )
        selected_stock = stocks_list[0]
        if selected_stock.cost <= capital:
            profit_solution2, stocks_list_solution2 = bruteforce_algo(
                capital - selected_stock.cost,
                stocks_list[1:],
                stocks_selection + [selected_stock],
            )
            if profit_solution1 < profit_solution2:
                return profit_solution2, stocks_list_solution2

        return profit_solution1, stocks_list_solution1
    else:
        best_profit = sum([stock.profit * 100 for stock in stocks_selection]) / 100
        return best_profit, stocks_selection


capital = 500

best_profit, stocks_result = bruteforce_algo(capital, stocks_list)
list_to_display = []
for stock in stocks_result:
    list_to_display.append(stock.name)

print(f"Le montant du bénéfice est de {best_profit}€.")
print(f"La liste d'action est : {list_to_display}")

end_timer = datetime.now()

print(f"Temps d'exécution du programme : {end_timer - start_timer}")
