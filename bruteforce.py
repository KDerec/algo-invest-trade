from datetime import datetime
import csv
import itertools


start_timer = datetime.now()

stocks_list = []


with open("data.csv", newline="") as file:
    has_header = csv.Sniffer().has_header(file.read(1024))
    file.seek(0)
    reader = csv.reader(file)
    if has_header:
        next(reader)
    i = 0
    for row in reader:
        name = row[0]
        cost = int(row[1])
        profitability = int(row[2])
        profit = round(cost * (profitability / 100), 2)

        stock = (name, cost, profit)
        stocks_list.append(stock)
        i += 1
        if i == 10:
            break

max_result = 0

for arrangement in itertools.permutations(stocks_list):
    capital = 500
    result = 0
    # list_to_display = []
    for stock in arrangement:
        capital -= stock[1]
        if capital < 0:
            break
        # stock_name = stock.name.replace("Action-", "")
        # list_to_display.append(stock[0])
        result += stock[2] * 100

    if max_result < result:
        max_result = result
        print(f"Le nouveau meilleur résultat est {max_result / 100} €")

        # print(f"L'arrangement correspondant est {list_to_display}")

end_timer = datetime.now()

print(end_timer - start_timer)
