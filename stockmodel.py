class Stock:
    def __init__(self, name, cost, profitability):
        self.name = name
        self.cost = int(cost)
        self.profitability = int(profitability)
        self.profit = round(self.cost * (self.profitability / 100), 2)
