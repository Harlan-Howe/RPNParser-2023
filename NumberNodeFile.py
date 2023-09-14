from typing import Tuple

import cv2

from NodeFile import Node, display_font


class NumberNode(Node):
    """
    A node that specifically holds a floating point number.
    """
    def __init__(self, number: float = 0):
        super(NumberNode, self).__init__(content=number, left=None, right=None)

    def get_value(self) -> float:
        # TODO 2A: override this method.
        return -1  # replace this line.

    def get_infix_string(self) -> str:
        # TODO 3A: override this method.
        return "Not yet written."  # replace this line.

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
