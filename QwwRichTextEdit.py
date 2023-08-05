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
        self._actions: list = []
        self._cB: QAction = None
        self._tb: QToolBar = QToolBar(self)
        self._tb.setIconSize(QSize(24, 24))
        self._ac: QAction = None
        self._ar: QAction = None
        self._al: QAction = None
        self._aj: QAction = None
        self._li: QAction = None
        
        self._fcb: QFontComboBox = QFontComboBox(self)
        self._actions[self.Action.FontFamilyAction] = self._tb.addWidget(self._fcb)
        self._fcb.activated.connect(self.setFont_h)
        self._fsp: QComboBox = QComboBox(self)
        self._actions[self.Action.FontSizeAction] = tb.addWidget(self._fsp)
        self._fsp.activated.connect(self.setFont_h)
        for s: int in QFontDatabase.standardSizes():
            self._fsp.addItem(str(s))
        self._currentList: QTextList = None
        
        self._options: self.Options = (self.Options.Style | 
                                       self.Options.Alignment | 
                                       self.Options.FontFamily |
                                       self.Options.FontSize |
                                       self.Options.Color)
        

    def options() -> self.Option:
        pass

    def toolBarAction(a: self.Action) -> QAction:
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

    @pyqtSlot
    def setUnderline(v: bool) -> None:
        pass
d
    @pyqtSlot
    def setFont_h() -> None:
        pass

    @pyqtSlot
    def setFont(f: QFont) -> None:
        pass

    @pyqtSlot
    def setList(v: bool) -> None:
        pass

    @pyqtSlot
    def setColor(c: QColor) -> None:
        pass

    @pyqtSlot
    def setOptions(opt: self.Options) -> None:
        pass

    @pyqtSlot
    def updateCurrentCharFormat(fmt: QTextCharFormat) -> None:
        pass

    @pyqtSlot
    def updateCurrentBlockFormat() -> None:
        pass

    def event(e: QEvent) -> bool:
        pass

    def contextMenuEvent(event: QContextMenuEvent) -> None:
        pass
