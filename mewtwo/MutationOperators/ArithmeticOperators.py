import ast
import random
from abc import ABC

from .MutationOperator import MutationOperator


class ArithmeticMutationOperator(MutationOperator, ast.NodeTransformer, ABC):
    def __init__(self, mutation_rate=0.5):
        self.mutation_rate = mutation_rate

    def visit_BinOp(self, node):
        if isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
            if random.random() < self.mutation_rate:
                if isinstance(node.op, ast.Add):
                    node.op = ast.Sub()
                elif isinstance(node.op, ast.Sub):
                    node.op = ast.Add()
                elif isinstance(node.op, ast.Mult):
                    node.op = ast.Div()
                elif isinstance(node.op, ast.Div):
                    node.op = ast.Mult()

        # просматривает дочерние узлы рекурсивно
        self.generic_visit(node)
        return node
