# mewtwo-py

## Библиотека мутационного тестирования на python

## Возможности

### Реализовано

- Проверка покрытия кода валидными тестами
- Использование стратегии случайной мутации
- Мутации бинарных операторов
- Поддержка библиотеки тестирования unittest

### Планируется реализовать

- Стратегия единичной мутации
- Добавление большего количества мутаторов
- Использование файла конфигурации для управления мутаторами и стратегиями

## Скриншоты выполнения тестирования

- Базовый файл:\
  ![Base file](https://i.imgur.com/e3ITn7c.png 'Базовый файл')
- Мутированный файл:\
  ![Mutated file](https://i.imgur.com/aRrzFwt.png 'Мутированный файл')
- Файл с тестами:\
   ![Test file](https://i.imgur.com/P8ETUN9.png 'Файл с тестами')
- Выходной текст:\
  ![Test output](https://i.imgur.com/oJVKOfm.png 'Выходной текст')

## Технологии

- [AST] - библиотека для работы с Abstract Syntax Tree
- [unittest] - библиотека тестирования, поставляемая с python

## Запуск

Для работы необходимо предустановить [Python](https://www.python.org/downloads/)

Клонирование проекта

```sh
git clone git@github.com:leeroykahikki/cyberzone.git
cd mewtwo-py
```

Скрипт запуска

```sh
python main.py -f "absolute_path_to_dir/mewtwo/example/example.py" -t "absolute_path_to_dir/mewtwo/example/test_example.py" -c "config"
```

## Примечания

Конфигурационный файл
: на данный момент конфигурационный файл не поддерживается, поэтому указываем любой путь в данном аргументе

Запуск проекта
: в связи с проблемами, связанными с импортами, на данный момент библиотека запускается лишь в среде выполнения IDE PyCharm

## Лицензия

MIT

[ast]: https://docs.python.org/3/library/ast.html
[unittest]: https://docs.python.org/3/library/unittest.html
