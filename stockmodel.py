class Stock:
    def __init__(self, name, cost, profitability):
        self.name = name
        self.cost = cost
        self.profitability = profitability
        self.profit = self.cost * (self.profitability / 100)
