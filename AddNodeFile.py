from NodeFile import Node
from OperatorNodeFile import OperatorNode


class AddNode(OperatorNode):
    """
    a class that represents the binary operator for addition, with the sign "+".
    """
    def __init__(self, left: Node = None, right: Node = None):
        super(AddNode, self).__init__(content="+", left=left, right=right)

    def get_value(self) -> float:
        # TODO 2B: override this method!
        return -1 # replace this line.
