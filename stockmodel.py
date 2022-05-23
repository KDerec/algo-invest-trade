class Stock:
    """
    A class to represent a stock.

    Attributes:
    - name (str) : name of the stock
    - cost (int) : cost of the stock
    - profitability (int) : profitability of the stock
    - profit (float) : calculated profit of the stock
    """

    def __init__(self, name, cost, profitability):
        """
        Constructs all the necessary attributes for the stock object.

        Parameters:
        - name (str) : name of the stock
        - cost (int) : cost of the stock
        - profitability (int) : profitability of the stock
        """
        self.name = name
        self.cost = cost
        self.profitability = profitability
        self.profit = self.cost * (self.profitability / 1000000)
