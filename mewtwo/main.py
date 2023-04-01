import ast
import importlib

from mewtwo import Visitors
from mewtwo.MutationOperators import ArithmeticMutationOperator

from mewtwo.utils import parse_args


def mutate_imports(tree, mutated_module):
    for node in ast.walk(tree):
        if isinstance(node, ast.Import) and node.names[0].name == mutated_module:
            node.names[0].name = node.names[0].name + "_mut"

        elif isinstance(node, ast.ImportFrom) and node.module == mutated_module:
            node.module = node.module + "_mut"

    return tree


def dynamic_import(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            # Импортируем модуль
            for module in node.names:
                importlib.import_module(module.name)

        elif isinstance(node, ast.ImportFrom):
            # Импортируем модуль
            module = importlib.import_module(node.module)

            # Импортируем объекты из модуля
            for name in node.names:
                if name.name == '*':
                    # Импортируем все объекты из модуля
                    globals().update(module.__dict__)
                else:
                    # Импортируем конкретный объект из модуля
                    globals()[name.asname or name.name] = getattr(module, name.name)


def mutate(tree):
    functions_list = Visitors.get_function_definitions(tree)
    mutated_functions_list = []

    for func in functions_list:
        binops_list = Visitors.get_binops_in_function(func)

        for binop in binops_list:
            ArithmeticMutationOperator().visit_BinOp(binop)

        mutated_func = Visitors.replace_binops_in_function(func, binops_list)
        mutated_functions_list.append(mutated_func)

    mutated_tree = Visitors.replace_function_definition(tree, mutated_functions_list)

    return mutated_tree


def main():
    args = parse_args()  # парсим аргументы командной строки

    with open(args.file, 'r') as source:
        target_tree = ast.parse(source.read())

    mutated_target_tree = mutate(target_tree)

    with open(args.file[0:-3] + "_mut.py", 'w') as f:
        f.write(ast.unparse(mutated_target_tree))

    with open(args.test, 'r') as f:
        test_tree = ast.parse(f.read())

        mutated_test_tree = mutate_imports(test_tree, "mewtwo.example.example")
        dynamic_import(mutated_test_tree)

        exec(compile(mutated_test_tree, filename="main", mode="exec"))


if __name__ == "__main__":
    main()
