import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def addition(x, y):
    logging.info(f"Dodaję {x} i {y}")
    return x + y


def subtraction(x, y):
    logging.info(f"Odejmuję {y} od {x}")
    return x - y


def multiplication(x, y):
    logging.info(f"Mnożę {x} razy {y}")
    return x * y


def division(x, y):
    logging.info(f"Dzielę {x} przez {y}")
    return x / y


def calculator(x, y, operation):
    if operation == "1":
        addition(x, y)
    elif operation == "2":
        subtraction(x, y)
    elif operation == "3":
        multiplication(x, y)
    elif operation == "4":
        if y == 0:
            logging.info("Składnik 2. nie może być równy 0")
            y = input("Podaj składnik 2.")
            y = float(y)
            division(x, y)
        else:
            division(x, y)
    else:
        exit(1)


if __name__ == "__main__":
    while True:
        operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
        x = input("Podaj składnik 1.")
        y = input("Podaj składnik 2.")
        x = float(x)
        y = float(y)
        print(f"Wynik to {calculator(x, y, operation)}")
