import ast
from typing import List


class MutationOperator:
    """Базовый класс для операторов мутации"""

    def mutate(self, node: ast.AST) -> List[ast.AST]:
        """Мутирует узел и возращает список возможных мутированных узлов"""
        raise NotImplementedError()