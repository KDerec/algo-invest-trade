import csv
from stockmodel import Stock


def create_stocks_list():
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

    return spent_capital
