from typing import Tuple

import cv2

from NodeFile import Node, display_font


class OperatorNode(Node):
    """
    an abstract class that represents a binary operator.
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
