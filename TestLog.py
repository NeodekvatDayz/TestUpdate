from loguru import logger
import time

logger.add("Log.log", format="{time} {level} {message}",
           level="DEBUG", rotation="2 MB", compression="zip")

start_time = time.time()

logger.info("Start")


def sum(a, b):
    try:
        x = a / b
        print(x)
        logger.info("Res:" + " " + str(a) +
                    "/" + str(b) + "=" + " " + str(x))
        timess = time.time() - start_time
        logger.info("Time:" + str(timess))
    except ZeroDivisionError:
        logger.error("ZeroDivisionError: Error na 0 / nelz")
        main()

# @logger.catch()
# ! тест коментов


def main():
    try:
        c = int(input("1:"))
        d = int(input("2:"))
        sum(c, d)
    except ValueError:
        logger.error("ValueError: Вводить можно только цыфры!")
        main()


if __name__ == "__main__":
    main()
