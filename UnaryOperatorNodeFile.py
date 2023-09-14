import cv2

from NodeFile import Node
from OperatorNodeFile import OperatorNode


class UnaryOperatorNode(OperatorNode):
    """
    An abstract class that represents a singleton operator
    """

    def __init__(self, content: str = "?", left: Node = None, right: Node = None):
        super(UnaryOperatorNode, self).__init__(content=content, left=left, right=right)

    def get_infix_string(self) -> str:
        # TODO 3C: override this method.
        return "Not yet written."

    def draw_self_at(self, buffer, x: int, y: int, horizontal_spacing: int, vertical_spacing: int = 45):
        left_pt, right_pt = super(UnaryOperatorNode, self).draw_my_label(buffer, x, y)
        bottom_pt = (int(x), int((left_pt[1]-y)*1.207)+y)
        if self.left is not None:
            cv2.line(img=buffer, pt1=bottom_pt, pt2=(x, y+vertical_spacing), color=(1, 1, 0), thickness=1)
            self.left.draw_self_at(buffer, x, int(y+vertical_spacing), horizontal_spacing, vertical_spacing)
