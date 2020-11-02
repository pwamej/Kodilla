import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def calculator(x, y, operation):
    if operation == "1":
        logging.info(f"Dodaję {x} i {y}")
        return x + y
    elif operation == "2":
        logging.info(f"Odejmuję {y} od {x}")
        return x - y
    elif operation == "3":
        logging.info(f"Mnożę {x} razy {y}")
        return x * y
    elif operation == "4":
        logging.info(f"Dzielę {x} przez {y}")
        return x / y
    else:
        exit(1)


if __name__ == "__main__":
    operation = input(
        "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    x = input("Podaj składnik 1.")
    y = input("Podaj składnik 2.")
    x = float(x)
    y = float(y)
    print(f"Wynik to {calculator(x, y, operation)}")
