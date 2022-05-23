def bruteforce_algo(capital, stocks_list, stocks_selection=[]):
    """
    Test all combination of stock to buy and found the best profit.

    Attrs:
    - capital (int): capital to spent.
    - stock_list (list): list of stock object.
    - stocks_selection (list): list of selected stock object.

    Returns:
    - best_profit (float): amount of profit.
    - stocks_selection (list): list of selected stock object.
    """
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
    best_profit, stocks_result = bruteforce_algo(capital, stocks_list)

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
