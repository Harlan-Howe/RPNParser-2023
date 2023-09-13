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

