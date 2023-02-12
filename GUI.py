from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
import Organism
import World


class Ui_MainWindow(object):

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("Virtual World")
        mainWindow.resize(1600, 1200)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 220, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 173, 143))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 63, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 53))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 191, 167))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 220, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 173, 143))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 63, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 53))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 191, 167))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 63, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 220, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 173, 143))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 63, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 53))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 63, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 63, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        mainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcomeImage = QtWidgets.QLabel(self.centralwidget)
        self.welcomeImage.setGeometry(QtCore.QRect(420, 350, 751, 521))
        self.welcomeImage.setText("")
        self.welcomeImage.setPixmap(QtGui.QPixmap("Background.jpg"))
        self.welcomeImage.setScaledContents(True)
        self.welcomeImage.setObjectName("welcomeImage")
        self.lay = QtWidgets.QHBoxLayout(self.centralwidget)
        self.world = None
        self.boardGraphics = None
        self.komentatorGraphics = None
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionNew_Game = QtWidgets.QAction(mainWindow)
        self.actionNew_Game.setObjectName("actionNew_Game")
        self.actionLoad_Game = QtWidgets.QAction(mainWindow)
        self.actionLoad_Game.setObjectName("actionLoad_Game")
        self.actionSave_Game = QtWidgets.QAction(mainWindow)
        self.actionSave_Game.setObjectName("actionSave_Game")
        self.actionExit = QtWidgets.QAction(mainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionNew_Game)
        self.menuMenu.addAction(self.actionLoad_Game)
        self.menuMenu.addAction(self.actionSave_Game)
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        self.actionNew_Game.triggered.connect(lambda: self.clickedNewGame())
        self.actionLoad_Game.triggered.connect(lambda: self.clickedLoadGame())
        self.actionSave_Game.triggered.connect(lambda: self.clickedSaveGame())
        self.actionExit.triggered.connect(lambda: self.clickedExit(mainWindow))

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("Virtual World", "Virtual World"))
        self.menuMenu.setTitle(_translate("mainWindow", "Menu"))
        self.actionNew_Game.setText(_translate("mainWindow", "New Game"))
        self.actionLoad_Game.setText(_translate("mainWindow", "Load Game"))
        self.actionSave_Game.setText(_translate("mainWindow", "Save Game"))
        self.actionExit.setText(_translate("mainWindow", "Exit"))

    class KomentatorGraphics(QtWidgets.QScrollArea):
        def __init__(self, world):
            super().__init__()
            self.text = world.komentator.getText()
            self.setWidgetResizable(True)
            self.content = QtWidgets.QWidget(self)
            self.setWidget(self.content)
            self.lay = QtWidgets.QVBoxLayout(self.content)
            self.label = QtWidgets.QLabel(self.content)
            self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
            self.label.setWordWrap(True)
            self.label.setText(self.text)
            self.lay.addWidget(self.label)

        def refreshComments(self, world):
            firstComment = "Autor: Sebastian Kutny 188586\n WSAD - controls\n R - use special ability\n Enter - next turn\n"
            newText = firstComment + world.komentator.getText()
            self.label.setText(newText)

    class BoardGraphics(QtWidgets.QGroupBox):
        class BoardField(QtWidgets.QLabel):
            def __init__(self, pozX, pozY):
                super().__init__()
                self.setFrameShape(QtWidgets.QFrame.Panel)
                self.pozX = pozX
                self.pozY = pozY
                self.isEmpty = True
                self.icon = QtGui.QPixmap("Ziemia.png")
                self.setPixmap(self.icon)
                self.setScaledContents(True)

        def __init__(self, world):
            super().__init__("Board")
            self.pozX = world.sizeX
            self.pozY = world.sizeY
            self.boardFields = [[self.BoardField(0, 0) for row in range(self.pozX)] for col in range(self.pozY)]
            self.layBoard = QtWidgets.QGridLayout()
            self.setLayout(self.layBoard)
            for i in range(self.pozX):
                for j in range(self.pozY):
                    self.boardFields[j][i] = self.BoardField(j, i)
                    self.layBoard.addWidget(self.boardFields[j][i], j, i)

        def refreshBoard(self, world):
            for i in range(self.pozX):
                for j in range(self.pozY):
                    if self.boardFields[j][i] is not None:
                        tmpOrganism = world.board[j][i]
                        if tmpOrganism is not None:
                            self.boardFields[j][i].isEmpty = False
                            self.boardFields[j][i].icon = tmpOrganism.icon
                            self.boardFields[j][i].setPixmap(self.boardFields[j][i].icon)
                        else:
                            self.boardFields[j][i].isEmpty = True
                            self.boardFields[j][i].icon = QtGui.QPixmap("Ziemia.png")
                            self.boardFields[j][i].setPixmap(self.boardFields[j][i].icon)

    def refreshWorld(self):
        self.boardGraphics.refreshBoard(self.world)
        self.komentatorGraphics.refreshComments(self.world)

    def startGame(self):
        self.welcomeImage.close()
        self.boardGraphics = self.BoardGraphics(self.world)
        self.boardGraphics.setMinimumSize(1000, 1125)
        self.lay.addWidget(self.boardGraphics)
        self.komentatorGraphics = self.KomentatorGraphics(self.world)
        self.komentatorGraphics.setMinimumSize(350, 1125)
        self.lay.addWidget(self.komentatorGraphics)
        self.refreshWorld()

    def clickedNewGame(self):
        if self.world is not None and self.world.komentator is not None:
            self.world.komentator.eraseComments()
        msgX = QtWidgets.QInputDialog()
        msgY = QtWidgets.QInputDialog()
        sizeX = msgX.getInt(msgX, 'Insert size X', "Enter size of X")[0]
        sizeY = msgY.getInt(msgY, 'Insert size Y', "Enter size of Y")[0]
        self.world = World.World(sizeX, sizeY, self)
        self.world.createWorld()
        if self.boardGraphics is not None:
            self.boardGraphics.close()
        if self.komentatorGraphics is not None:
            self.komentatorGraphics.close()
        self.startGame()

    def clickedLoadGame(self):
        if self.world is not None and self.world.komentator is not None:
            self.world.komentator.eraseComments()
        msgName = QtWidgets.QInputDialog()
        name = msgName.getText(msgName, 'Insert saves name', "Enter saves name")[0]
        self.world = World.World.loadWorld(self.world, name)
        self.world.worldGUI = self
        if self.boardGraphics is not None:
            self.boardGraphics.close()
        if self.komentatorGraphics is not None:
            self.komentatorGraphics.close()
        self.startGame()

    def clickedSaveGame(self):
        msgName = QtWidgets.QInputDialog()
        name = msgName.getText(msgName, 'Insert saves name', "Enter saves name")[0]
        self.world.saveWorld(name)
        self.world.komentator.addComment("World saved")
        self.komentatorGraphics.refreshComments(self.world)

    def clickedExit(self, mainWindow):
        mainWindow.close()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)

    def keyPressEvent(self, event):
        if self.world is not None and self.world.pause is True:
            keyCode = event.key()
            if keyCode == Qt.Key_Enter - 1:
                pass
            elif self.world.human is None or self.world.human.isDead is True and (keyCode == Qt.Key_W or keyCode == Qt.Key_S or keyCode == Qt.Key_A or keyCode == Qt.Key_D or keyCode == Qt.Key_R):
                self.world.komentator.addComment("Human is dead, you can't do any more moves")
                self.komentatorGraphics.refreshComments(self.world)
                return
            elif keyCode == Qt.Key_W:
                self.world.human.moveDirection = Organism.Organism.Direction.up
            elif keyCode == Qt.Key_S:
                self.world.human.moveDirection = Organism.Organism.Direction.down
            elif keyCode == Qt.Key_A:
                self.world.human.moveDirection = Organism.Organism.Direction.left
            elif keyCode == Qt.Key_D:
                self.world.human.moveDirection = Organism.Organism.Direction.right
            elif keyCode == Qt.Key_R:
                if self.world.human.cooldown == 0:
                    self.world.human.strength += 10
                    self.world.human.cooldown = 15
                    self.world.komentator.addComment("Ability 'Magiczny Eliksir' used (Remaining time is " + str(self.world.human.cooldown - 5) + " turns)")
                    self.komentatorGraphics.refreshComments(self.world)
                    return
                elif self.world.human.cooldown > 5:
                    self.world.komentator.addComment("Ability 'Magiczny Eliksir' is already used (Remaining time is " + str(self.world.human.cooldown - 5) + " turns)")
                    self.komentatorGraphics.refreshComments(self.world)
                    return
                else:
                    self.world.komentator.addComment("Ability 'Magiczny Eliksir' can be used after " + str(self.world.human.cooldown) + " turns")
                    self.komentatorGraphics.refreshComments(self.world)
                    return
            else:
                self.world.komentator.addComment("Wrong key word, try again")
                self.komentatorGraphics.refreshComments(self.world)
                return
            self.world.komentator.eraseComments()
            self.world.makeTurn()
            self.refreshWorld()
            self.world.isPaused = True
