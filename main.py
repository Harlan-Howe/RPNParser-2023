import cv2
import numpy as np
from NodeFile import Node
from AddNodeFile import AddNode
from NumberNodeFile import NumberNode
from OperatorNodeFile import OperatorNode
from SquareRootNodeFile import SquareRootNode
from UnaryOperatorNodeFile import UnaryOperatorNode

from typing import List

def demo():

    RPN_string = "56 12 34 16 √ + + +"
    root = parse_string(RPN_string)
    print(root.get_value())

    buffer = np.zeros((600, 900, 3), dtype=float)
    root.draw_self_at(buffer,x=450, y = 20, horizontal_spacing=450)

    cv2.imshow("result", buffer)
    cv2.waitKey()
    cv2.destroyAllWindows()

def parse_string(s: str) -> NodeFile.Node:
    """
    generates an RPN tree from the given string
    :param s:  a string of numbers and operators, separated by spaces that should represent a calculation.
    :return: a Node for the root of the RPN tree we generate from the string.
    """
    stack: List[NodeFile.Node] = []
    parts = s.split(" ")
    for p in parts:
        try:
            num = float(p)
            # TODO #1A: if we got here, that means that p was a number. Create a number node from "num" and append it to
            #           the stack.
            pass

        except:
            #TODO #1B: if we got here, that means that p wasn't a number. It should be an operator. Determine which
            #          operator it was, pop one or two values from the stack, generate a new node, and append it to
            #          the stack.
            # Note: to perform the pop, I receommend "stack.pop(-1)" to get the last item in the list.
            pass

    # TODO #1C: return the top (hopefully only) Node on the stack.
    return None


if __name__ == '__main__':
    demo()

