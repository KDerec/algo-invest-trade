from datetime import datetime
from controller import create_stocks_list
from view import display_result_information
from bruteforce import bruteforce_algo
from optimized import optimized_algo


capital = 500
stocks_list = create_stocks_list()


def main():
    start_timer = datetime.now()
    bruteforce_best_profit, bruteforce_stocks_result = bruteforce_algo(
        capital, stocks_list
    )
    end_timer = datetime.now()
    bruteforce_time = end_timer - start_timer
    display_result_information(
        bruteforce_best_profit, bruteforce_stocks_result, bruteforce_time
    )

    start_timer = datetime.now()
    optimized_best_profit, optimized_stocks_result = optimized_algo(
        capital, stocks_list
    )
    end_timer = datetime.now()
    optimized_time = end_timer - start_timer
    display_result_information(
        optimized_best_profit, optimized_stocks_result, optimized_time
    )


if __name__ == "__main__":
    main()
