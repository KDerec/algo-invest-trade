def optimized_algo(capital, stocks_list):
    table = [[0 for x in range(capital + 1)] for x in range(len(stocks_list) + 1)]

    for i in range(1, len(stocks_list) + 1):
        for c in range(1, capital + 1):
            if stocks_list[i - 1].cost <= c:
                table[i][c] = max(
                    stocks_list[i - 1].profit
                    + table[i - 1][c - stocks_list[i - 1].cost],
                    table[i - 1][c],
                )
            else:
                table[i][c] = table[i - 1][c]

    c = capital
    n = len(stocks_list)
    stocks_selection = []

    while c >= 0 and n >= 0:
        stock = stocks_list[n - 1]
        if table[n][c] == table[n - 1][c - stock.cost] + stock.profit:
            stocks_selection.append(stock)
            c -= stock.cost

        n -= 1

    return round(table[-1][-1], 2), stocks_selection
