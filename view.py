from controller import create_stocks_name_list
from controller import create_spent_capital


def input_choice_plot_or_algo():
    """Input a choice and return his value."""
    choice = input(
        "Taper 'o' pour afficher un graphique, "
        "sinon, choix d'un algorithme afin de trouver le meilleur résultat : "
    )

    return choice


def input_choice_data():
    """Input a choice and return his value."""
    choice = input(
        """Veuillez choisir les données à analyser : 
       - Taper '1' pour : data (20 actions);
       - Taper '2' pour : dataset1 (1001 actions);
       - Taper '3' pour : dataset2 (1000 actions)."""
        "\nL'algorithme de force brute n'est pas disponible pour le choix 2 et 3."
        "\nChoix du numéro : "
    )

    return choice


def input_choice_an_algo():
    """Input a choice and return his value."""
    choice = input(
        "Pour exécuter l'algorithmes bruteforce taper 'o', "
        "sinon, l'algorithme optimisé sera exécuté :"
    )

    return choice


def input_choice_start_algo():
    """Input a choice and return his value."""
    choice = input(
        "Taper 'o' pour exécuter l'algorithme optimisé, " "sinon, quitter : "
    )

    return choice


def display_result_information(best_profit, stocks_result, time):
    """Display best profit, stocks name list, spent capital and execution time."""
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


def display_exit_message():
    """Input a choice and return his value."""
    print(
        "Tapez la lettre 'q' pour confirmez l'arrêt de l'application,"
        " sinon, recommencer : "
    )

    return input()
