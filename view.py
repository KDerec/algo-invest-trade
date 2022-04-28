from controller import create_stocks_name_list
from controller import create_spent_capital


def display_result_information(best_profit, stocks_result, time):
    stocks_name_list = create_stocks_name_list(stocks_result)
    spent_capital = create_spent_capital(stocks_result)

    print(
        f"""
    Le montant du bénéfice est de {best_profit}€.
    La liste d'action est : {stocks_name_list}.
    Le montant de l'investissement est de {spent_capital}€.
    Temps d'exécution du programme : {time}.
    """
    )
