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
