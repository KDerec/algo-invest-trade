import csv
from stockmodel import Stock


def create_stocks_list(path_to_data, max_number_item=""):
    """
    Return a list of stock object.

    Attrs:
    - path_to_data (str): a path to csv file in data/.
    - max_number_item (str or int): limit the number of items to return.

    Returns:
    - a list of stock object.
    """
    with open(path_to_data, newline="") as file:
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
    """
    Return a list of stock name.

    Attrs:
    - stock_list (list): list of stock object.

    Returns:
    - a list of stock name
    """
    stocks_name_list = []
    for stock in stocks_list:
        stocks_name_list.append(stock.name)

    return stocks_name_list


def create_spent_capital(stocks_list):
    """
    Calculate and return a spent capital.

    Attrs:
    - stock_list (list): list of stock object.

    Returns:
    - spent capital.
    """
    spent_capital = 0

    for stock in stocks_list:
        spent_capital += stock.cost
    spent_capital = spent_capital / 100

    return spent_capital


def create_path_to_data(choice):
    """
    Return a path to data and a boolean.

    Attrs:
    - choice (str): user choice.

    Returns:
    - path to data or None.
    - boolean or None.
    """
    if choice == "1":
        path_to_data = "data/data.csv"
        return path_to_data, True
    if choice == "2":
        path_to_data = "data/dataset1_Python+P7.csv"
        return path_to_data, False
    if choice == "3":
        path_to_data = "data/dataset2_Python+P7.csv"
        return path_to_data, False
    else:
        return None, None
