import ast


class FunctionDefVisitorToGet(ast.NodeVisitor):
    def __init__(self):
        self.function_defs = []

    def visit_FunctionDef(self, node):
        self.function_defs.append(node)


class FunctionDefVisitorToReplace(ast.NodeVisitor):
    def __init__(self, name):
        self.function_def_to_replace = None
        self.function_name = name

    # возможно это можно заменить обычным перебором по имени в древе
    # или же вовсе убрать поиск по функции и сделать поиск по всему древу
    def visit_FunctionDef(self, node):
        if node.name == self.function_name:
            self.function_def_to_replace = node


def get_function_definitions(tree):
    visitor = FunctionDefVisitorToGet()
    visitor.visit(tree)

    return visitor.function_defs


def replace_function_definition(tree, func_list):
    for func in func_list:
        visitor = FunctionDefVisitorToReplace(func.name)
        visitor.visit(tree)

        index = tree.body.index(visitor.function_def_to_replace)
        tree.body[index] = func

    return tree
