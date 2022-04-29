from controller import create_stocks_name_list
from controller import create_spent_capital


def input_choice_plot_or_algo():
    choice = input(
        "Taper 'o' pour afficher un graphique, "
        "sinon, choisir un algorithme avant de trouver le meilleur résultat : "
    )

    return choice


def input_choice_an_algo():
    choice = input(
        "Pour exécuter l'algorithmes bruteforce taper 1, "
        "sinon, l'algorithme optimisé sera exécuter :"
    )

    return choice


def display_result_information(best_profit, stocks_result, time):
    stocks_name_list = create_stocks_name_list(stocks_result)
    spent_capital = create_spent_capital(stocks_result)

    print(
        f"""    
    Le montant du bénéfice est de {best_profit}€.
    La liste d'action est : {stocks_name_list}.
    Le montant de l'investissement est de {spent_capital}€.
    Temps d'exécution du programme : {time} secondes.
    """
    )
