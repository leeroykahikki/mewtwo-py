import argparse


def parse_args():
    """Функция для парсинга аргументов командной строки

    Returns:
        ArgumentParser: объект, хранящий в себе полученные аргументы
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file')  # файл, который нужно мутировать
    parser.add_argument('-t', '--test')  # файл, который содержит в себе тесты
    parser.add_argument('-c', '--config')  # конфигурация мутационных тестов
    return parser.parse_args()
