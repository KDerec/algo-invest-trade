import matplotlib.pyplot as plt
import view
from time import perf_counter
from controller import create_stocks_list
from controller import create_path_to_data
from bruteforce import bruteforce_algo
from optimized import optimized_algo


capital = 500 * 100  # * 100 to handle decimal number


def main():
    """Manage the running of the program."""
    while True:
        choice = view.input_choice_data()
        path_to_data, ok_for_bruteforce = create_path_to_data(choice)
        if ok_for_bruteforce:
            choice = view.input_choice_plot_or_algo()
            if choice.upper() == "O":
                plot_graphs(path_to_data)
            else:
                choice = view.input_choice_an_algo()
                if choice.upper() == "O":
                    run_bruteforce(path_to_data)
                else:
                    run_optimized(path_to_data)
        else:
            choice = view.input_choice_start_algo()
            if choice.upper() == "O":
                run_optimized(path_to_data)

        choice = view.display_exit_message()
        if choice.upper() == "Q":
            exit()


def run_bruteforce(path_to_data):
    """Call functions to run bruteforce algorithm and display information."""
    stocks_list = create_stocks_list(path_to_data)

    start_timer = perf_counter()
    bruteforce_best_profit, bruteforce_stocks_result = bruteforce_algo(
        capital, stocks_list
    )
    end_timer = perf_counter()
    bruteforce_time = end_timer - start_timer
    view.display_result_information(
        bruteforce_best_profit, bruteforce_stocks_result, bruteforce_time
    )


def run_optimized(path_to_data):
    """Call functions to run optimized algorithm and display information."""
    stocks_list = create_stocks_list(path_to_data)
    start_timer = perf_counter()
    optimized_best_profit, optimized_stocks_result = optimized_algo(
        capital, stocks_list
    )
    end_timer = perf_counter()
    optimized_time = end_timer - start_timer
    view.display_result_information(
        optimized_best_profit, optimized_stocks_result, optimized_time
    )


def plot_graphs(path_to_data):
    """
    Plot a graph to show relationship between number of stock and execution time
    for bruteforce and optimized algorithms.
    """
    number_of_stock = []
    bruteforce_times = []
    optimized_times = []

    for i in range(1, 21):
        stocks_list = create_stocks_list(path_to_data, i)

        start_timer = perf_counter()
        bruteforce_best_profit, bruteforce_stocks_result = bruteforce_algo(
            capital, stocks_list
        )
        end_timer = perf_counter()

        bruteforce_times.append(end_timer - start_timer)

        start_timer = perf_counter()
        optimized_best_profit, optimized_stocks_result = optimized_algo(
            capital, stocks_list
        )
        end_timer = perf_counter()

        optimized_times.append(end_timer - start_timer)

        number_of_stock.append(i)

    plt.figure().canvas.manager.set_window_title("Time Complexity")
    plt.xlabel("Number of stock")
    plt.ylabel("Execution Time (s)")
    plt.plot(number_of_stock, bruteforce_times, label="bruteforce_algo()")
    plt.plot(number_of_stock, optimized_times, label="optimized_algo()")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
