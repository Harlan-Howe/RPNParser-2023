import math

import numpy as np
import cv2
from typing import Tuple
from abc import ABC, abstractmethod

display_font = cv2.FONT_HERSHEY_PLAIN

class Node(ABC):
    """
    This class is the abstract class representing all nodes.
    """
    def __init__(self, content, left: "Node" = None, right: "Node" = None):
        self.content = content
        self.left = left
        self.right = right

    @abstractmethod
    def get_value(self) -> float:
        """
        :return: the value of this node and its children
        """
        return -1

    @abstractmethod
    def get_infix_string(self) -> str:
        """
        :return: a string description of this node and its children in infix notation.
        """
        return "Not yet written."

    def draw_self_at(self, buffer: np.ndarray, x: int, y: int, horizontal_spacing: int, vertical_spacing: int = 45):
        """
        draws this node and its children into the OpenCV buffer given
        :param buffer: the nparray representing the drawing space for this tree.
        :param x: the horizontal location of the center of this node
        :param y: the vertical location of the top of this node
        :param horizontal_spacing: the lateral spacing between this node and its children
        :param vertical_spacing: the vertical spacing between this node and its children
        :return: None
        """
        lower_left_point, lower_right_point = self.draw_my_label(buffer,x,y)

        if self.left is not None:
            cv2.line(img=buffer,
                      pt1=lower_left_point,
                      pt2=(int(x-horizontal_spacing/2), y+vertical_spacing),
                      color=(1, 1, 0),
                      thickness = 1)
            self.left.draw_self_at(buffer=buffer,
                                   x=int(x-horizontal_spacing/2),
                                   y=int(y+vertical_spacing),
                                   horizontal_spacing=horizontal_spacing/2,
                                   vertical_spacing=vertical_spacing)
        if self.right is not None:
            cv2.line(img=buffer,
                      pt1=lower_right_point,
                      pt2=(int(x+horizontal_spacing/2), y+vertical_spacing),
                      color=(1, 1, 0),
                      thickness = 1)
            self.right.draw_self_at(buffer=buffer,
                                   x=int(x+horizontal_spacing/2),
                                   y=y+vertical_spacing,
                                   horizontal_spacing=horizontal_spacing/2,
                                   vertical_spacing=vertical_spacing)

    def draw_my_label(self, buffer, x, y) -> Tuple[Tuple[int,int],Tuple[int,int]]:
        """
        draws just the content of this node into the center of the node, returning the coordinates of the lower corners
        of the node that can be used for drawing the lines to the next nodes.
        :param buffer: the nparray representing the drawing space for this tree.
        :param x: the horizontal location of the center of this node
        :param y: the vertical location of the top of this node
        :return: a tuple ((x1, y1,), (x2, y2)) of the coordinates of the lower-left and lower-right "attach points" of
        this node.
        """
        descriptionString = f"{self.content}"
        textSize, baseline = cv2.getTextSize(text = descriptionString,fontFace= display_font, fontScale= 1, thickness=1)

        cv2.putText(img=buffer,
                    text=descriptionString,
                    org=(int(x-textSize[0]/2), y+textSize[1]+2),
                    color=(1, 1, 1),
                    fontFace=display_font,
                    fontScale=1,
                    thickness=1)
        cv2.line(img=buffer,
                 pt1=(int(x-textSize[0]/2-1), y),
                 pt2=(int(x+textSize[0]/2+1), y+textSize[1]+3),
                 color = (0, 0, 1),
                 thickness= 2)
        cv2.line(img=buffer,
                 pt1=(int(x + textSize[0] / 2 - 1), y),
                 pt2=(int(x - textSize[0] / 2 + 1), y + textSize[1] + 3),
                 color=(0, 0, 1),
                 thickness=2)

        lower_left = (int(x-textSize[0]/2-1), y+textSize[1]+3)
        lower_right = (int(x+textSize[0]/2-1), y+textSize[1]+3)

        return lower_left, lower_right

class NumberNode(Node):
    """
    A node that specifically holds a floating point number.
    """
    def __init__(self, number: float = 0):
        super(NumberNode, self).__init__(content=number, left=None, right=None)

    def get_value(self) -> float:
        # TODO 2A: override this method.
        return -1 # replace this line.

    def get_infix_string(self) -> str:
        # TODO 3A: override this method.
        return "Not yet written." # replace this line.

    def draw_my_label(self, buffer, x, y) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        descriptionString = f"{self.content}"
        textSize, baseline = cv2.getTextSize(text=descriptionString, fontFace=display_font, fontScale=1, thickness=1)
        cv2.rectangle(buffer,
                      pt1=(int(x - textSize[0] / 2) - 1, y),
                      pt2=(int(x + textSize[0] / 2) + 1, y + textSize[1] + 3),
                      color=(1, 0.5, 1),
                      thickness=1)
        cv2.putText(img=buffer,
                    text=descriptionString,
                    org=(int(x - textSize[0] / 2), y + textSize[1] + 2),
                    color=(1, 0.5, 1),
                    fontFace=display_font,
                    fontScale=1,
                    thickness=1)
        lower_left = (int(x - textSize[0] / 2 - 1), y + textSize[1] + 3)
        lower_right = (int(x + textSize[0] / 2 - 1), y + textSize[1] + 3)

        return lower_left, lower_right

class OperatorNode(Node):
    """
    an abstract class that respresents a binary operator.
    """
    def __init__(self, content: str = "?", left: Node = None, right: Node = None):
        super(OperatorNode,self).__init__(content=content, left=left, right=right)

    def get_infix_string(self) -> str:
        # TODO 3B: override this method.
        return "Not yet written."

    def draw_my_label(self, buffer, x, y) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        descriptionString = f"{self.content}"
        textSize, baseline = cv2.getTextSize(text=descriptionString, fontFace=display_font, fontScale=1,
                                             thickness=1)

        cv2.ellipse(img = buffer,
                    center=(x, int(y+0.707*textSize[1]+2)),
                    axes = (int(0.707*textSize[0]), int(0.707*(textSize[1])+2)),
                    angle = 0,
                    startAngle=0,
                    endAngle= 360,
                    color=(0, 1, 1),
                    thickness=1,
                    )
        cv2.putText(img=buffer,
                    text=descriptionString,
                    org=(int(x - textSize[0] / 2), int(y + 1.207 *textSize[1] + 2)),
                    color=(0, 1, 1),
                    fontFace=display_font,
                    fontScale=1,
                    thickness=1)
        lower_left = (int(x - textSize[0]/2  - 1), int(y + 1.4 * textSize[1] + 3))
        lower_right = (int(x + textSize[0]/2  - 1), int(y + 1.4 * textSize[1] + 3))

        return lower_left, lower_right

class SingletonOperatorNode(OperatorNode):
    """
    An abstract class that represents a singleton operator
    """
    def __init__(self, content: str ="?", left: Node = None, right: Node = None):
        super(SingletonOperatorNode, self).__init__(content=content, left=left, right=right)

    def get_infix_string(self) -> str:
        # TODO 3B: override this method.
        return "Not yet written."

    def draw_self_at(self, buffer, x:int , y:int, horizontal_spacing:int , vertical_spacing:int = 45) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        left_pt, right_pt = super(SingletonOperatorNode, self).draw_my_label(buffer,x,y)
        bottom_pt = (int(x), int((left_pt[1]-y)*1.207)+y)
        if self.left is not None:
            cv2.line(img=buffer, pt1=(bottom_pt), pt2=(x,y+vertical_spacing), color = (1,1,0),thickness =1)
            self.left.draw_self_at(buffer,x,int(y+vertical_spacing),horizontal_spacing, vertical_spacing)


class AddNode(OperatorNode):
    """
    a class that represents the binary operator for addition, with the sign "+".
    """
    def __init__(self, left: Node = None, right: Node = None):
        super(AddNode, self).__init__(content="+", left=left, right=right)

    def get_value(self) -> float:
        # TODO 2B: override this method!
        return -1 # replace this line.

class SquareRootNode(SingletonOperatorNode):
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


#TODO 4: write other classes for the other operators, including -, *, /, %, 1/x, max, min, x^2, x^y, and any others.