import csv


stocks_list = []


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
    i = 0
    for row in reader:
        stock = Stock(row[0], row[1], row[2])
        stocks_list.append(stock)
        i += 1
        if i == 10:
            break
