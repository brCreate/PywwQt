from PyQt5.Qt import *


class QwwRichTextEdit(QTextEdit):
    class Option(int):
        NoOptions = 0x0
        Style = 0x1
        Alignment = 0x2
        FontFamily = 0x4
        FontSize = 0x8
        Color = 0x10


    class Action(int):
        BoldAction = 0
        ItalicAction = 1
        UnderlineAction = 2
        LeftAlignAction = 3
        RightAlignAction = 4
        AlignCenterAction = 5
        JustifyAction = 6
        ColorAction = 7
        FontFamilyAction = 8
        FontSizeAction = 9

    
    def __init__(parent: QWidget = None):
        pass

    def options() -> Option:
        pass

    @pyqtSlot
    def changeAlignment(a: QAction) -> None:
        pass

    @pyqtSlot
    def setBold(v: bool) -> None:
        pass

    @pyqtSlot
    def setItalic(v: bool) -> None:
        pass

# Under construction...
