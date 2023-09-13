import math

from NodeFile import Node
from UnaryOperatorNodeFile import UnaryOperatorNode


class SquareRootNode(UnaryOperatorNode):
    """
    a class that represents the singleton operator for square root. The user might type this in as "√" (option-v),
    but since this won't display right in openCV, we will display it in the graphic as "sqrt"
    """
    def __init__(self, child: Node = None):
        super(SquareRootNode, self).__init__(content="sqrt", left=child, right=None)

    def get_value(self) -> float:
        # TODO 2C: override this method!
        if self.left is None:
            raise RuntimeError("Attempting to evaluate node, but child is None.")
        return math.sqrt(self.left.get_value())
