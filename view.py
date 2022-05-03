from controller import create_stocks_name_list
from controller import create_spent_capital


def input_choice_plot_or_algo():
    choice = input(
        "Taper 'o' pour afficher un graphique, "
        "sinon, choix d'un algorithme afin de trouver le meilleur résultat : "
    )

    return choice


def input_choice_an_algo():
    choice = input(
        "Pour exécuter l'algorithmes bruteforce taper 'o', "
        "sinon, l'algorithme optimisé sera exécuté :"
    )

    return choice


def display_result_information(best_profit, stocks_result, time):
    stocks_name_list = create_stocks_name_list(stocks_result)
    spent_capital = create_spent_capital(stocks_result)

    print(
        f"""    
    Montant du bénéfice : {best_profit}€.
    Liste d'action acheté : {stocks_name_list}.
    Montant de l'investissement : {spent_capital}€.
    Temps d'exécution du programme : {time} secondes.
    """
    )
