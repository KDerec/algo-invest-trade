def optimized_algo(capital, stocks_list):
    """
    Create a matrice of capital and profit to found the best combination of stock to buy.

    Attrs:
    - capital (int): capital to spent.
    - stock_list (list): list of stock object.

    Returns:
    - best_profit (float): amount of profit.
    - stocks_selection (list): list of selected stock object.
    """
    table = [[0 for x in range(capital + 1)] for x in range(len(stocks_list) + 1)]

    for n in range(1, len(stocks_list) + 1):
        for c in range(1, capital + 1):
            if stocks_list[n - 1].cost <= c:
                table[n][c] = max(
                    stocks_list[n - 1].profit
                    + table[n - 1][c - stocks_list[n - 1].cost],
                    table[n - 1][c],
                )
            else:
                table[n][c] = table[n - 1][c]

    best_profit = round(table[-1][-1], 2)

    stocks_selection = []
    c = capital
    n = len(stocks_list)

    while c >= 0 and n >= 0:
        stock = stocks_list[n - 1]
        if table[n][c] == table[n - 1][c - stock.cost] + stock.profit:
            stocks_selection.append(stock)
            c -= stock.cost

        n -= 1

    return best_profit, stocks_selection


if __name__ == "__main__":
    print(
        "Ceci est un exemple pour l'analyse de trois actions (Action 1, 2 et 3) "
        "avec chacune un bénéfice de 300% et un coût respectif de 4€, 3€ et 2€"
        "\nPour une exécution plus intéressante du programme, veuillez consulter : "
        "https://github.com/KDerec/algo-invest-trade"
    )

    class Stock:
        def __init__(self, name, cost, profitability):
            self.name = name
            self.cost = cost
            self.profitability = profitability
            self.profit = self.cost * (self.profitability / 100)

    capital = 5
    stocks_list = [
        Stock("Action-1", 4, 300),
        Stock("Action-2", 3, 300),
        Stock("Action-3", 2, 300),
    ]
    best_profit, stocks_result = optimized_algo(capital, stocks_list)

    stocks_name_list = []
    for stock in stocks_result:
        stocks_name_list.append(stock.name)

    spent_capital = 0
    for stock in stocks_result:
        spent_capital += stock.cost

    print(
        f"""    
    Le montant du bénéfice est de {best_profit}€.
    La liste d'action acheté est : {stocks_name_list}.
    Le montant de l'investissement est de {spent_capital}€.
    """
    )
