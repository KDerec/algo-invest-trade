import csv
from stockmodel import Stock


def create_stocks_list(max_number_item=""):
    with open("data/dataset1_Python+P7.csv", newline="") as file:
        has_header = csv.Sniffer().has_header(file.read(1024))
        file.seek(0)
        reader = csv.reader(file)
        if has_header:
            next(reader)
        i = 0
        stocks_list = []
        for row in reader:
            name = row[0]
            cost = int(float(row[1]) * 100)
            profitability = int(float(row[2]) * 100)
            if cost <= 0:
                pass
            else:
                stock = Stock(name, cost, profitability)
                stocks_list.append(stock)
            i += 1
            if i == max_number_item:
                break

    return stocks_list


def create_stocks_name_list(stocks_list):
    stocks_name_list = []
    for stock in stocks_list:
        stocks_name_list.append(stock.name)

    return stocks_name_list


def create_spent_capital(stocks_list):
    spent_capital = 0

    for stock in stocks_list:
        spent_capital += stock.cost
    spent_capital = spent_capital / 100

    return spent_capital
