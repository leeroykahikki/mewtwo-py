import ast

from mewtwo import Visitors
from mewtwo.MutationOperators import ArithmeticMutationOperator
from mewtwo.utils import parse_args


def main():
    args = parse_args()  # парсим аргументы командной строки

    with open(args.target, 'r') as source:
        target_ast = ast.parse(source.read())

    functions_list = Visitors.get_function_definitions(target_ast)
    mutated_functions_list = []

    for func in functions_list:
        binops_list = Visitors.get_binops_in_function(func)

        for binop in binops_list:
            ArithmeticMutationOperator().visit_BinOp(binop)

        mutated_func = Visitors.replace_binops_in_function(func, binops_list)
        mutated_functions_list.append(mutated_func)

    mutated_ast = Visitors.replace_function_definition(target_ast, mutated_functions_list)
    print(ast.unparse(mutated_ast))


if __name__ == "__main__":
    main()
