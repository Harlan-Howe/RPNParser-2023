import cv2
import numpy as np
from NodeFile import Node
from AddNodeFile import AddNode
from NumberNodeFile import NumberNode
from SquareRootNodeFile import SquareRootNode

from typing import List


def demo():
    print("--------------------  RPN 1")  # test creating a NumberNode
    # This requires to-do # 1A, #1C, #2A, and #3A
    RPN_string1 = "12"
    root1: Node = parse_string(RPN_string1)
    print(root1)
    print(f"{root1.get_value() = }")
    print(f"{root1.get_infix_string()}")

    print("--------------------  RPN 2")  # test creating a (Binary) OperatorNode
    # This requires additional to-dos #1B, #2B and #3B
    RPN_string2 = "13 27 +"
    root2: Node = parse_string(RPN_string2)
    print(root2)
    print(f"{root2.get_value() = }")
    print(f"{root2.get_infix_string() = }")

    print("--------------------  RPN 3")  # test creating an UnaryOperatorNode
    # This requires additional to-dos #2C and #3C
    RPN_string3 = "169 √"  # (that symbol is an option-v, or you can just copy/paste it.)
    root3: Node = parse_string(RPN_string3)
    print(root3)
    print(f"{root3.get_infix_string() = }")
    print(f"{root3.get_value() = }")

    print("--------------------  RPN 4")  # test creating a compound statement
    RPN_string4 = "100 21 + √"  # (that symbol is an option-v, or you can just copy/paste it.)
    root4: Node = parse_string(RPN_string4)
    print(root4)
    print(f"{root4.get_infix_string() = }")
    print(f"{root4.get_value() = }")

    # showing graphics
    buffer1 = np.zeros((600, 900, 3), dtype=float)  # make a new black image
    root4.draw_self_at(buffer1, x=450, y=20, horizontal_spacing=450)  # draw the tree in the image.
    cv2.imshow("result 4", buffer1)  # display the image in a window.
    cv2.waitKey()  # pause for the user to press any key.

    print("--------------------  RPN 5")
    RPN_string5 = "56 12 34 16 √ + + +"
    root5 = parse_string(RPN_string5)
    print(root5.get_value())

    buffer2 = np.zeros((600, 900, 3), dtype=float)  # make another new black image.
    root5.draw_self_at(buffer2, x=450, y=20, horizontal_spacing=450)  # draw this tree in the image.

    cv2.imshow("result 5", buffer2)  # display this image in a different window.
    cv2.moveWindow("result 5", 100, 100)  # offset this image from the other one.
    cv2.waitKey()  # wait for the user to press a button

    #  Write code to test out your other operators...

    cv2.destroyAllWindows()  # close the windows.


def parse_string(s: str) -> Node:
    """
    generates an RPN tree from the given string
    :param s:  a string of numbers and operators, separated by spaces that should represent a calculation.
    :return: a Node for the root of the RPN tree we generate from the string.
    """
    stack: List[Node] = []
    parts = s.split(" ")
    for p in parts:
        try:
            num = float(p)  # attempt to interpret this string as a float.
            # TODO #1A: if we got here, that means that p was a number. Create a number node from "num" and append it to
            #           the stack.
            pass

        except ValueError:  # exception for parsing a string with non-numeric content
            # TODO #1B: if we got here, that means that p wasn't a number. It should be an operator. Determine which
            #          operator it was, pop one or two values from the stack, generate a new node, and append it to
            #          the stack.
            # Note: to perform the pop, I recommend "stack.pop(-1)" to get the last item in the list.
            pass

    # TODO #1C: return the top (hopefully only) Node on the stack.
    return None  # replace this!!!!


if __name__ == '__main__':
    demo()
