import ast


class BinOpVisitorToGet(ast.NodeVisitor):
    def __init__(self):
        self.binops = []

    def visit_BinOp(self, node):
        self.binops.append(node)
        self.generic_visit(node)


class BinOpVisitorToReplace(ast.NodeVisitor):
    def __init__(self, binops):
        self.binops = binops
        self.it = 0;

    def visit_BinOp(self, node):
        rep_node = self.binops[self.it]
        self.it += 1
        return rep_node


def get_binops_in_function(node):
    visitor = BinOpVisitorToGet()
    visitor.visit(node)

    return visitor.binops


def replace_binops_in_function(node, binops):
    visitor = BinOpVisitorToReplace(binops)
    visitor.visit(node)

    return node
