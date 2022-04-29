import matplotlib.pyplot as plt
from time import perf_counter
import view
from controller import create_stocks_list
from bruteforce import bruteforce_algo
from optimized import optimized_algo


capital = 500 * 100  # * 100 to handle decimal number


def main():
    choice = view.input_choice_plot_or_algo()
    if choice.upper() == "O":
        plot_graphs()
    else:
        choice = view.input_choice_an_algo()
        if choice.upper() == "O":
            run_bruteforce()
        else:
            run_optimized()


def run_bruteforce():
    stocks_list = create_stocks_list()

    start_timer = perf_counter()
    bruteforce_best_profit, bruteforce_stocks_result = bruteforce_algo(
        capital, stocks_list
    )
    end_timer = perf_counter()
    bruteforce_time = end_timer - start_timer
    view.display_result_information(
        bruteforce_best_profit, bruteforce_stocks_result, bruteforce_time
    )


def run_optimized():
    stocks_list = create_stocks_list()
    start_timer = perf_counter()
    optimized_best_profit, optimized_stocks_result = optimized_algo(
        capital, stocks_list
    )
    end_timer = perf_counter()
    optimized_time = end_timer - start_timer
    view.display_result_information(
        optimized_best_profit, optimized_stocks_result, optimized_time
    )


def plot_graphs():
    number_of_stock = []
    bruteforce_times = []
    optimized_times = []

    for i in range(1, 21):
        stocks_list = create_stocks_list(i)

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
    input("Taper pour quitter:")
    exit()
