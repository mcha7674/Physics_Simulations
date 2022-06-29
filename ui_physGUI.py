# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'physGUIQnGnvY.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QStackedWidget,
    QToolButton, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1193, 672)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color:transparent;\n"
"background:none;\n"
"padding:0;\n"
"margin:0;\n"
"color:#fff;\n"
"}\n"
"#menuSideBar QToolButton{\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"#menuSideBar QToolButton:hover{\n"
"background-color:rgb(95,0,0)\n"
"}\n"
"#menuSideBar QToolButton#menuButton:hover{\n"
"background-color:rgb(95,0,0)\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(150, 0, 0);\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menuSideBar = QFrame(self.centralwidget)
        self.menuSideBar.setObjectName(u"menuSideBar")
        self.menuSideBar.setEnabled(True)
        self.menuSideBar.setMinimumSize(QSize(50, 0))
        self.menuSideBar.setMaximumSize(QSize(50, 16777215))
        self.menuSideBar.setStyleSheet(u"QToolButton{\n"
"background-color:rgb(150,0,0);\n"
"font: 13pt \"Segoe UI\";\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.menuSideBar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuFrame1 = QFrame(self.menuSideBar)
        self.menuFrame1.setObjectName(u"menuFrame1")
        self.menuFrame1.setMaximumSize(QSize(16777215, 80))
        self.menuFrame1.setFrameShape(QFrame.StyledPanel)
        self.menuFrame1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.menuFrame1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 34)
        self.menuButton = QToolButton(self.menuFrame1)
        self.menuButton.setObjectName(u"menuButton")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuButton.sizePolicy().hasHeightForWidth())
        self.menuButton.setSizePolicy(sizePolicy)
        self.menuButton.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/Icons/iconsWhiteSize40/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.menuButton, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.menuFrame1)

        self.menuFrame2 = QFrame(self.menuSideBar)
        self.menuFrame2.setObjectName(u"menuFrame2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menuFrame2.sizePolicy().hasHeightForWidth())
        self.menuFrame2.setSizePolicy(sizePolicy1)
        self.menuFrame2.setStyleSheet(u"QToolButton:hover {\n"
"    background-color: rgb(95,0,0);\n"
"}")
        self.menuFrame2.setFrameShape(QFrame.StyledPanel)
        self.menuFrame2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.menuFrame2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.homeButton = QToolButton(self.menuFrame2)
        self.homeButton.setObjectName(u"homeButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.homeButton.sizePolicy().hasHeightForWidth())
        self.homeButton.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        self.homeButton.setFont(font)
        self.homeButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/iconsWhiteSize40/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon1)
        self.homeButton.setIconSize(QSize(23, 25))
        self.homeButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_4.addWidget(self.homeButton)

        self.launchMenuButton = QToolButton(self.menuFrame2)
        self.launchMenuButton.setObjectName(u"launchMenuButton")
        sizePolicy2.setHeightForWidth(self.launchMenuButton.sizePolicy().hasHeightForWidth())
        self.launchMenuButton.setSizePolicy(sizePolicy2)
        icon2 = QIcon()
        icon2.addFile(u":/Icons/iconsWhiteSize40/dribbble.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.launchMenuButton.setIcon(icon2)
        self.launchMenuButton.setIconSize(QSize(23, 25))
        self.launchMenuButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_4.addWidget(self.launchMenuButton)

        self.statsButton = QToolButton(self.menuFrame2)
        self.statsButton.setObjectName(u"statsButton")
        sizePolicy2.setHeightForWidth(self.statsButton.sizePolicy().hasHeightForWidth())
        self.statsButton.setSizePolicy(sizePolicy2)
        icon3 = QIcon()
        icon3.addFile(u":/Icons/iconsWhiteSize40/table.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.statsButton.setIcon(icon3)
        self.statsButton.setIconSize(QSize(23, 25))
        self.statsButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.statsButton.setAutoRaise(False)

        self.verticalLayout_4.addWidget(self.statsButton)

        self.plotsButton = QToolButton(self.menuFrame2)
        self.plotsButton.setObjectName(u"plotsButton")
        sizePolicy2.setHeightForWidth(self.plotsButton.sizePolicy().hasHeightForWidth())
        self.plotsButton.setSizePolicy(sizePolicy2)
        icon4 = QIcon()
        icon4.addFile(u":/Icons/iconsWhiteSize40/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.plotsButton.setIcon(icon4)
        self.plotsButton.setIconSize(QSize(23, 25))
        self.plotsButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_4.addWidget(self.plotsButton)


        self.verticalLayout_2.addWidget(self.menuFrame2)

        self.menuFrame3 = QFrame(self.menuSideBar)
        self.menuFrame3.setObjectName(u"menuFrame3")
        self.menuFrame3.setStyleSheet(u"QToolButton:hover {\n"
"    background-color: rgb(95,0,0);\n"
"}")
        self.menuFrame3.setFrameShape(QFrame.StyledPanel)
        self.menuFrame3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.menuFrame3)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 50)
        self.settingButton = QToolButton(self.menuFrame3)
        self.settingButton.setObjectName(u"settingButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.settingButton.sizePolicy().hasHeightForWidth())
        self.settingButton.setSizePolicy(sizePolicy3)
        icon5 = QIcon()
        icon5.addFile(u":/Icons/iconsWhiteSize40/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingButton.setIcon(icon5)
        self.settingButton.setIconSize(QSize(23, 25))
        self.settingButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_6.addWidget(self.settingButton)

        self.helpButton = QToolButton(self.menuFrame3)
        self.helpButton.setObjectName(u"helpButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.helpButton.sizePolicy().hasHeightForWidth())
        self.helpButton.setSizePolicy(sizePolicy4)
        icon6 = QIcon()
        icon6.addFile(u":/Icons/iconsWhiteSize40/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpButton.setIcon(icon6)
        self.helpButton.setIconSize(QSize(23, 25))
        self.helpButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_6.addWidget(self.helpButton)


        self.verticalLayout_2.addWidget(self.menuFrame3)


        self.horizontalLayout.addWidget(self.menuSideBar)

        self.mainBodyContainer = QFrame(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        self.mainBodyContainer.setStyleSheet(u"background-color: rgb(139, 139, 139);")
        self.verticalLayout = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QFrame(self.mainBodyContainer)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setStyleSheet(u"background-color: rgb(150, 0, 0);")
        self.headerFrame.setFrameShape(QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fileOutFrame = QFrame(self.headerFrame)
        self.fileOutFrame.setObjectName(u"fileOutFrame")
        self.fileOutFrame.setFrameShape(QFrame.StyledPanel)
        self.fileOutFrame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.fileOutFrame)

        self.windowFrame = QFrame(self.headerFrame)
        self.windowFrame.setObjectName(u"windowFrame")
        sizePolicy1.setHeightForWidth(self.windowFrame.sizePolicy().hasHeightForWidth())
        self.windowFrame.setSizePolicy(sizePolicy1)
        self.windowFrame.setStyleSheet(u"QPushButton#maximizeButton:hover{\n"
"background-color: rgb(95,0,0)\n"
"}\n"
"QPushButton#minimizeButton:hover{\n"
"background-color: rgb(95,0,0)\n"
"}\n"
"QPushButton#closeButton:hover{\n"
"background-color: rgb(60,0,0);\n"
"background-color: rgb(255, 0, 0);\n"
"}")
        self.windowFrame.setFrameShape(QFrame.StyledPanel)
        self.windowFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.windowFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.windowFrame)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setMinimumSize(QSize(50, 0))
        self.minimizeButton.setMaximumSize(QSize(50, 16777215))
        icon7 = QIcon()
        icon7.addFile(u":/Icons/iconsWhiteSize40/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon7)
        self.minimizeButton.setIconSize(QSize(25, 45))

        self.horizontalLayout_4.addWidget(self.minimizeButton)

        self.maximizeButton = QPushButton(self.windowFrame)
        self.maximizeButton.setObjectName(u"maximizeButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.maximizeButton.sizePolicy().hasHeightForWidth())
        self.maximizeButton.setSizePolicy(sizePolicy5)
        self.maximizeButton.setMinimumSize(QSize(50, 0))
        self.maximizeButton.setMaximumSize(QSize(50, 16777215))
        self.maximizeButton.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.maximizeButton.setFont(font1)
        icon8 = QIcon()
        icon8.addFile(u":/Icons/iconsWhiteSize40/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeButton.setIcon(icon8)
        self.maximizeButton.setIconSize(QSize(25, 45))

        self.horizontalLayout_4.addWidget(self.maximizeButton)

        self.closeButton = QPushButton(self.windowFrame)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(50, 0))
        self.closeButton.setMaximumSize(QSize(50, 16777215))
        font2 = QFont()
        font2.setPointSize(12)
        self.closeButton.setFont(font2)
        icon9 = QIcon()
        icon9.addFile(u":/Icons/iconsWhiteSize40/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon9)
        self.closeButton.setIconSize(QSize(25, 45))

        self.horizontalLayout_4.addWidget(self.closeButton)


        self.horizontalLayout_2.addWidget(self.windowFrame, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.headerFrame, 0, Qt.AlignTop)

        self.mainBodyFrame = QFrame(self.mainBodyContainer)
        self.mainBodyFrame.setObjectName(u"mainBodyFrame")
        sizePolicy2.setHeightForWidth(self.mainBodyFrame.sizePolicy().hasHeightForWidth())
        self.mainBodyFrame.setSizePolicy(sizePolicy2)
        self.mainBodyFrame.setStyleSheet(u"background-color: rgb(95, 0, 0);\n"
"")
        self.mainBodyFrame.setFrameShape(QFrame.StyledPanel)
        self.mainBodyFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.mainBodyFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, -1, -1, -1)
        self.stackedWidget = QStackedWidget(self.mainBodyFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.launchPage = QWidget()
        self.launchPage.setObjectName(u"launchPage")
        self.launchPage.setStyleSheet(u"QLineEdit{\n"
"background-color: white;\n"
"color:black;\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.launchPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.launchHeader = QFrame(self.launchPage)
        self.launchHeader.setObjectName(u"launchHeader")
        self.launchHeader.setMaximumSize(QSize(16777215, 16777215))
        self.launchHeader.setFrameShape(QFrame.StyledPanel)
        self.launchHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.launchHeader)
        self.horizontalLayout_6.setSpacing(27)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.mediumLabelFrame = QFrame(self.launchHeader)
        self.mediumLabelFrame.setObjectName(u"mediumLabelFrame")
        self.mediumLabelFrame.setMaximumSize(QSize(122, 16777215))
        self.mediumLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.mediumLabelFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.mediumLabelFrame)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 5)
        self.label_23 = QLabel(self.mediumLabelFrame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(150, 16777215))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.label_23.setFont(font3)

        self.horizontalLayout_18.addWidget(self.label_23, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.mediumLabelFrame)

        self.inputHeader = QFrame(self.launchHeader)
        self.inputHeader.setObjectName(u"inputHeader")
        sizePolicy1.setHeightForWidth(self.inputHeader.sizePolicy().hasHeightForWidth())
        self.inputHeader.setSizePolicy(sizePolicy1)
        self.inputHeader.setFrameShape(QFrame.StyledPanel)
        self.inputHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.inputHeader)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.dragButton = QRadioButton(self.inputHeader)
        self.dragButton.setObjectName(u"dragButton")
        self.dragButton.setMaximumSize(QSize(72, 16777215))
        font4 = QFont()
        font4.setPointSize(10)
        self.dragButton.setFont(font4)

        self.horizontalLayout_8.addWidget(self.dragButton)

        self.vacButton = QRadioButton(self.inputHeader)
        self.vacButton.setObjectName(u"vacButton")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.vacButton.sizePolicy().hasHeightForWidth())
        self.vacButton.setSizePolicy(sizePolicy6)
        self.vacButton.setMaximumSize(QSize(83, 16777215))
        self.vacButton.setFont(font4)

        self.horizontalLayout_8.addWidget(self.vacButton)

        self.compareButton = QRadioButton(self.inputHeader)
        self.compareButton.setObjectName(u"compareButton")

        self.horizontalLayout_8.addWidget(self.compareButton)


        self.horizontalLayout_6.addWidget(self.inputHeader, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.launchHeader)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_17.setSpacing(7)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.frame_3)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_35)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.frame_35)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)

        self.verticalLayout_35.addWidget(self.label_20)


        self.horizontalLayout_17.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_3)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_36)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.typeLabel = QLabel(self.frame_36)
        self.typeLabel.setObjectName(u"typeLabel")
        self.typeLabel.setFont(font3)
        self.typeLabel.setStyleSheet(u"border-bottom : 2px solid white;\n"
"")
        self.typeLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.typeLabel)


        self.horizontalLayout_17.addWidget(self.frame_36)


        self.horizontalLayout_6.addWidget(self.frame_3)

        self.displayHeader = QFrame(self.launchHeader)
        self.displayHeader.setObjectName(u"displayHeader")
        sizePolicy2.setHeightForWidth(self.displayHeader.sizePolicy().hasHeightForWidth())
        self.displayHeader.setSizePolicy(sizePolicy2)
        self.displayHeader.setMinimumSize(QSize(408, 0))
        self.displayHeader.setMaximumSize(QSize(16777215, 16777215))
        self.displayHeader.setStyleSheet(u"QPushButton{\n"
"	border-radius: 12px;\n"
"	background-color: rgb(150, 0,0);\n"
"}")
        self.displayHeader.setFrameShape(QFrame.StyledPanel)
        self.displayHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.displayHeader)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.saveDataButton_3 = QPushButton(self.displayHeader)
        self.saveDataButton_3.setObjectName(u"saveDataButton_3")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.saveDataButton_3.sizePolicy().hasHeightForWidth())
        self.saveDataButton_3.setSizePolicy(sizePolicy7)
        self.saveDataButton_3.setMinimumSize(QSize(85, 25))
        self.saveDataButton_3.setMaximumSize(QSize(85, 100))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.saveDataButton_3.setFont(font5)

        self.horizontalLayout_9.addWidget(self.saveDataButton_3)

        self.saveDataButton_2 = QPushButton(self.displayHeader)
        self.saveDataButton_2.setObjectName(u"saveDataButton_2")
        sizePolicy7.setHeightForWidth(self.saveDataButton_2.sizePolicy().hasHeightForWidth())
        self.saveDataButton_2.setSizePolicy(sizePolicy7)
        self.saveDataButton_2.setMinimumSize(QSize(85, 25))
        self.saveDataButton_2.setMaximumSize(QSize(85, 100))
        self.saveDataButton_2.setFont(font5)

        self.horizontalLayout_9.addWidget(self.saveDataButton_2)

        self.saveDataButton = QPushButton(self.displayHeader)
        self.saveDataButton.setObjectName(u"saveDataButton")
        sizePolicy7.setHeightForWidth(self.saveDataButton.sizePolicy().hasHeightForWidth())
        self.saveDataButton.setSizePolicy(sizePolicy7)
        self.saveDataButton.setMinimumSize(QSize(85, 25))
        self.saveDataButton.setMaximumSize(QSize(85, 100))
        self.saveDataButton.setFont(font5)

        self.horizontalLayout_9.addWidget(self.saveDataButton)

        self.saveAnimButton = QPushButton(self.displayHeader)
        self.saveAnimButton.setObjectName(u"saveAnimButton")
        sizePolicy7.setHeightForWidth(self.saveAnimButton.sizePolicy().hasHeightForWidth())
        self.saveAnimButton.setSizePolicy(sizePolicy7)
        self.saveAnimButton.setMinimumSize(QSize(98, 25))
        self.saveAnimButton.setMaximumSize(QSize(101, 100))
        self.saveAnimButton.setFont(font5)

        self.horizontalLayout_9.addWidget(self.saveAnimButton)


        self.horizontalLayout_6.addWidget(self.displayHeader)


        self.verticalLayout_9.addWidget(self.launchHeader, 0, Qt.AlignTop)

        self.launchBody = QFrame(self.launchPage)
        self.launchBody.setObjectName(u"launchBody")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.launchBody.sizePolicy().hasHeightForWidth())
        self.launchBody.setSizePolicy(sizePolicy8)
        self.launchBody.setStyleSheet(u"QLineEdit{\n"
"background:rgb(255,255,255);\n"
"}\n"
"")
        self.launchBody.setFrameShape(QFrame.StyledPanel)
        self.launchBody.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.launchBody)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.launchGeneral = QFrame(self.launchBody)
        self.launchGeneral.setObjectName(u"launchGeneral")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.launchGeneral.sizePolicy().hasHeightForWidth())
        self.launchGeneral.setSizePolicy(sizePolicy9)
        self.launchGeneral.setMaximumSize(QSize(215, 16777215))
        self.launchGeneral.setFrameShape(QFrame.StyledPanel)
        self.launchGeneral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.launchGeneral)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, -1, 9, -1)
        self.frame_11 = QFrame(self.launchGeneral)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy2.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy2)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_11)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_12.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_11.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.frame_10 = QFrame(self.launchGeneral)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy2.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy2)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, -1, 0, 0)
        self.frame_9 = QFrame(self.frame_10)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_9)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_9)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 13)
        self.frame_16 = QFrame(self.frame_5)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_16)
        self.verticalLayout_17.setSpacing(10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(15, 4, 15, 9)
        self.label_4 = QLabel(self.frame_16)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_16)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 0))
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        self.label_7.setFont(font3)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_7)


        self.horizontalLayout_11.addWidget(self.frame_16, 0, Qt.AlignLeft)

        self.frame_17 = QFrame(self.frame_5)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_17)
        self.verticalLayout_18.setSpacing(15)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(5, -1, 15, -1)
        self.x0LineEdit = QLineEdit(self.frame_17)
        self.x0LineEdit.setObjectName(u"x0LineEdit")
        self.x0LineEdit.setMaximumSize(QSize(70, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.x0LineEdit.setPalette(palette)
        self.x0LineEdit.setMaxLength(5)
        self.x0LineEdit.setClearButtonEnabled(False)

        self.verticalLayout_18.addWidget(self.x0LineEdit)

        self.y0LineEdit = QLineEdit(self.frame_17)
        self.y0LineEdit.setObjectName(u"y0LineEdit")
        self.y0LineEdit.setMaximumSize(QSize(70, 16777215))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.y0LineEdit.setPalette(palette1)
        self.y0LineEdit.setMaxLength(5)

        self.verticalLayout_18.addWidget(self.y0LineEdit)

        self.v0LineEdit = QLineEdit(self.frame_17)
        self.v0LineEdit.setObjectName(u"v0LineEdit")
        self.v0LineEdit.setMaximumSize(QSize(70, 16777215))
        self.v0LineEdit.setMaxLength(4)

        self.verticalLayout_18.addWidget(self.v0LineEdit)

        self.angleLineEdit = QLineEdit(self.frame_17)
        self.angleLineEdit.setObjectName(u"angleLineEdit")
        self.angleLineEdit.setMaximumSize(QSize(70, 16777215))
        self.angleLineEdit.setMaxLength(3)

        self.verticalLayout_18.addWidget(self.angleLineEdit)


        self.horizontalLayout_11.addWidget(self.frame_17, 0, Qt.AlignLeft)


        self.verticalLayout_16.addWidget(self.frame_5)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy3.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy3)
        self.frame_12.setMaximumSize(QSize(16777215, 48))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_12)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, 2, 0, 0)
        self.label_8 = QLabel(self.frame_12)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.verticalLayout_19.addWidget(self.label_8, 0, Qt.AlignHCenter)


        self.verticalLayout_16.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 16777215))
        self.frame_13.setFrameShape(QFrame.Box)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 13, 2)
        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 16777215))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_18)
        self.verticalLayout_21.setSpacing(15)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 27, 7, 19)
        self.label_9 = QLabel(self.frame_18)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMaximumSize(QSize(16777215, 16777215))
        self.label_9.setFont(font3)

        self.verticalLayout_21.addWidget(self.label_9, 0, Qt.AlignRight)

        self.label_10 = QLabel(self.frame_18)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.verticalLayout_21.addWidget(self.label_10)


        self.horizontalLayout_12.addWidget(self.frame_18, 0, Qt.AlignRight)

        self.frame_19 = QFrame(self.frame_13)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_19)
        self.verticalLayout_22.setSpacing(8)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(4, 21, -1, 19)
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_20)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 22)
        self.stepAngleCounter = QLabel(self.frame_20)
        self.stepAngleCounter.setObjectName(u"stepAngleCounter")
        self.stepAngleCounter.setMaximumSize(QSize(16777215, 15))
        font6 = QFont()
        font6.setPointSize(11)
        self.stepAngleCounter.setFont(font6)

        self.verticalLayout_23.addWidget(self.stepAngleCounter, 0, Qt.AlignHCenter)

        self.stepAngleSlider = QSlider(self.frame_20)
        self.stepAngleSlider.setObjectName(u"stepAngleSlider")
        self.stepAngleSlider.setMaximumSize(QSize(80, 15))
        self.stepAngleSlider.setMinimum(0)
        self.stepAngleSlider.setMaximum(20)
        self.stepAngleSlider.setSingleStep(1)
        self.stepAngleSlider.setOrientation(Qt.Horizontal)
        self.stepAngleSlider.setTickPosition(QSlider.NoTicks)
        self.stepAngleSlider.setTickInterval(1)

        self.verticalLayout_23.addWidget(self.stepAngleSlider)


        self.verticalLayout_22.addWidget(self.frame_20)

        self.finalAngleLineEdit = QLineEdit(self.frame_19)
        self.finalAngleLineEdit.setObjectName(u"finalAngleLineEdit")
        self.finalAngleLineEdit.setMaximumSize(QSize(70, 16777215))
        self.finalAngleLineEdit.setMaxLength(3)

        self.verticalLayout_22.addWidget(self.finalAngleLineEdit)


        self.horizontalLayout_12.addWidget(self.frame_19, 0, Qt.AlignHCenter)


        self.verticalLayout_16.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy3.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy3)
        self.frame_14.setMinimumSize(QSize(0, 0))
        self.frame_14.setMaximumSize(QSize(16777215, 35))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_14)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_14)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)

        self.verticalLayout_20.addWidget(self.label_11, 0, Qt.AlignHCenter)


        self.verticalLayout_16.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_9)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, -1)
        self.frame_21 = QFrame(self.frame_15)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 16777215))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_21)
        self.verticalLayout_24.setSpacing(26)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(24, 27, 5, 34)
        self.label_13 = QLabel(self.frame_21)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)

        self.verticalLayout_24.addWidget(self.label_13, 0, Qt.AlignRight)

        self.label_14 = QLabel(self.frame_21)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)

        self.verticalLayout_24.addWidget(self.label_14)


        self.horizontalLayout_13.addWidget(self.frame_21, 0, Qt.AlignRight)

        self.frame_22 = QFrame(self.frame_15)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_22)
        self.verticalLayout_25.setSpacing(4)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.massLineEdit = QLineEdit(self.frame_22)
        self.massLineEdit.setObjectName(u"massLineEdit")
        self.massLineEdit.setMaximumSize(QSize(70, 16777215))
        self.massLineEdit.setMaxLength(4)

        self.verticalLayout_25.addWidget(self.massLineEdit)

        self.radiusLineEdit = QLineEdit(self.frame_22)
        self.radiusLineEdit.setObjectName(u"radiusLineEdit")
        self.radiusLineEdit.setMaximumSize(QSize(70, 16777215))
        self.radiusLineEdit.setMaxLength(5)

        self.verticalLayout_25.addWidget(self.radiusLineEdit)


        self.horizontalLayout_13.addWidget(self.frame_22)


        self.verticalLayout_16.addWidget(self.frame_15)


        self.horizontalLayout_10.addWidget(self.frame_9)


        self.verticalLayout_11.addWidget(self.frame_10)


        self.horizontalLayout_7.addWidget(self.launchGeneral)

        self.launchDrag = QFrame(self.launchBody)
        self.launchDrag.setObjectName(u"launchDrag")
        self.launchDrag.setMaximumSize(QSize(258, 16777215))
        self.launchDrag.setFrameShape(QFrame.StyledPanel)
        self.launchDrag.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.launchDrag)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_25 = QFrame(self.launchDrag)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy2.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy2)
        self.frame_25.setMaximumSize(QSize(16777215, 30))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_25)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_25)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.verticalLayout_13.addWidget(self.label_16, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_33.addWidget(self.frame_25)

        self.frame_6 = QFrame(self.launchDrag)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_6)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_23)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_23)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_12, 0, Qt.AlignRight)

        self.label_15 = QLabel(self.frame_23)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(165, 16777215))
        self.label_15.setFont(font3)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_15, 0, Qt.AlignLeft)


        self.horizontalLayout_14.addWidget(self.frame_23, 0, Qt.AlignRight)

        self.frame_24 = QFrame(self.frame_6)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_24)
        self.verticalLayout_27.setSpacing(28)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(9, 8, 0, 5)
        self.dragCLineEdit = QLineEdit(self.frame_24)
        self.dragCLineEdit.setObjectName(u"dragCLineEdit")
        self.dragCLineEdit.setMaximumSize(QSize(70, 16777215))
        self.dragCLineEdit.setMaxLength(3)

        self.verticalLayout_27.addWidget(self.dragCLineEdit)

        self.seaTemptLineEdit = QLineEdit(self.frame_24)
        self.seaTemptLineEdit.setObjectName(u"seaTemptLineEdit")
        self.seaTemptLineEdit.setMaximumSize(QSize(70, 16777215))
        self.seaTemptLineEdit.setMaxLength(3)

        self.verticalLayout_27.addWidget(self.seaTemptLineEdit)


        self.horizontalLayout_14.addWidget(self.frame_24, 0, Qt.AlignLeft)


        self.verticalLayout_33.addWidget(self.frame_6)

        self.frame_26 = QFrame(self.launchDrag)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(16777215, 49))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_27)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_27)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_18, 0, Qt.AlignRight)


        self.horizontalLayout_15.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_28)
        self.verticalLayout_29.setSpacing(27)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(20, 13, 0, -1)
        self.vWindLineEdit = QLineEdit(self.frame_28)
        self.vWindLineEdit.setObjectName(u"vWindLineEdit")
        self.vWindLineEdit.setMaximumSize(QSize(70, 16777215))
        self.vWindLineEdit.setMaxLength(3)

        self.verticalLayout_29.addWidget(self.vWindLineEdit)


        self.horizontalLayout_15.addWidget(self.frame_28, 0, Qt.AlignLeft)


        self.verticalLayout_33.addWidget(self.frame_26)

        self.frame_33 = QFrame(self.launchDrag)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy2.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy2)
        self.frame_33.setMaximumSize(QSize(16777215, 48))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_33)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 10, 0, 10)
        self.label_21 = QLabel(self.frame_33)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 16777215))
        self.label_21.setFont(font1)

        self.verticalLayout_14.addWidget(self.label_21, 0, Qt.AlignHCenter)


        self.verticalLayout_33.addWidget(self.frame_33)

        self.frame_29 = QFrame(self.launchDrag)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(16777215, 16777215))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 4, 44)
        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(16777215, 16777215))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_30)
        self.verticalLayout_30.setSpacing(15)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 7, 19)
        self.label_19 = QLabel(self.frame_30)
        self.label_19.setObjectName(u"label_19")
        sizePolicy1.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy1)
        self.label_19.setMaximumSize(QSize(16777215, 16777215))
        self.label_19.setFont(font3)

        self.verticalLayout_30.addWidget(self.label_19, 0, Qt.AlignRight)


        self.horizontalLayout_16.addWidget(self.frame_30, 0, Qt.AlignRight)

        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_31)
        self.verticalLayout_31.setSpacing(8)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(4, 4, -1, 29)
        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_32)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 9)
        self.timeStepCounter = QLabel(self.frame_32)
        self.timeStepCounter.setObjectName(u"timeStepCounter")
        self.timeStepCounter.setMaximumSize(QSize(16777215, 15))
        self.timeStepCounter.setFont(font6)

        self.verticalLayout_32.addWidget(self.timeStepCounter, 0, Qt.AlignHCenter)

        self.timeStepSlider = QSlider(self.frame_32)
        self.timeStepSlider.setObjectName(u"timeStepSlider")
        self.timeStepSlider.setMaximumSize(QSize(80, 15))
        self.timeStepSlider.setMinimum(5)
        self.timeStepSlider.setMaximum(100)
        self.timeStepSlider.setOrientation(Qt.Horizontal)
        self.timeStepSlider.setTickPosition(QSlider.NoTicks)
        self.timeStepSlider.setTickInterval(1)

        self.verticalLayout_32.addWidget(self.timeStepSlider)


        self.verticalLayout_31.addWidget(self.frame_32)


        self.horizontalLayout_16.addWidget(self.frame_31, 0, Qt.AlignHCenter)


        self.verticalLayout_33.addWidget(self.frame_29)


        self.horizontalLayout_7.addWidget(self.launchDrag)

        self.launchDisplay = QFrame(self.launchBody)
        self.launchDisplay.setObjectName(u"launchDisplay")
        sizePolicy8.setHeightForWidth(self.launchDisplay.sizePolicy().hasHeightForWidth())
        self.launchDisplay.setSizePolicy(sizePolicy8)
        self.launchDisplay.setMinimumSize(QSize(0, 0))
        self.launchDisplay.setMaximumSize(QSize(629, 16777215))
        self.launchDisplay.setFrameShape(QFrame.StyledPanel)
        self.launchDisplay.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.launchDisplay)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.launchDisplay)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy8.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy8)
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_34)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.displayLabel = QLabel(self.frame_34)
        self.displayLabel.setObjectName(u"displayLabel")
        sizePolicy10 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.displayLabel.sizePolicy().hasHeightForWidth())
        self.displayLabel.setSizePolicy(sizePolicy10)
        self.displayLabel.setMinimumSize(QSize(7, 32))
        self.displayLabel.setScaledContents(True)

        self.verticalLayout_34.addWidget(self.displayLabel)


        self.verticalLayout_10.addWidget(self.frame_34)

        self.frame_4 = QFrame(self.launchDisplay)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 35))
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(150,0,0);\n"
"border-radius: 12px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.launchButton_2 = QPushButton(self.frame_4)
        self.launchButton_2.setObjectName(u"launchButton_2")
        sizePolicy1.setHeightForWidth(self.launchButton_2.sizePolicy().hasHeightForWidth())
        self.launchButton_2.setSizePolicy(sizePolicy1)
        self.launchButton_2.setMinimumSize(QSize(100, 35))
        self.launchButton_2.setMaximumSize(QSize(100, 35))
        self.launchButton_2.setFont(font3)

        self.horizontalLayout_19.addWidget(self.launchButton_2)

        self.launchButton = QPushButton(self.frame_4)
        self.launchButton.setObjectName(u"launchButton")
        sizePolicy1.setHeightForWidth(self.launchButton.sizePolicy().hasHeightForWidth())
        self.launchButton.setSizePolicy(sizePolicy1)
        self.launchButton.setMinimumSize(QSize(150, 35))
        self.launchButton.setMaximumSize(QSize(150, 35))
        self.launchButton.setFont(font1)

        self.horizontalLayout_19.addWidget(self.launchButton)

        self.launchButton_3 = QPushButton(self.frame_4)
        self.launchButton_3.setObjectName(u"launchButton_3")
        sizePolicy1.setHeightForWidth(self.launchButton_3.sizePolicy().hasHeightForWidth())
        self.launchButton_3.setSizePolicy(sizePolicy1)
        self.launchButton_3.setMinimumSize(QSize(100, 35))
        self.launchButton_3.setMaximumSize(QSize(100, 35))
        self.launchButton_3.setFont(font3)

        self.horizontalLayout_19.addWidget(self.launchButton_3)


        self.verticalLayout_10.addWidget(self.frame_4)


        self.horizontalLayout_7.addWidget(self.launchDisplay)


        self.verticalLayout_9.addWidget(self.launchBody)

        self.stackedWidget.addWidget(self.launchPage)
        self.statsPage = QWidget()
        self.statsPage.setObjectName(u"statsPage")
        self.stackedWidget.addWidget(self.statsPage)
        self.plotsPage = QWidget()
        self.plotsPage.setObjectName(u"plotsPage")
        self.stackedWidget.addWidget(self.plotsPage)
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_3 = QVBoxLayout(self.homePage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.homePage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 94))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Title = QLabel(self.frame_2)
        self.Title.setObjectName(u"Title")
        self.Title.setMaximumSize(QSize(16777215, 91))
        font7 = QFont()
        font7.setPointSize(28)
        self.Title.setFont(font7)
        self.Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.Title)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame = QFrame(self.homePage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Description = QLabel(self.frame)
        self.Description.setObjectName(u"Description")
        self.Description.setMaximumSize(QSize(16777215, 100))
        font8 = QFont()
        font8.setPointSize(16)
        self.Description.setFont(font8)
        self.Description.setTextFormat(Qt.RichText)
        self.Description.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.Description.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.Description)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.homePage)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.mainBodyFrame)

        self.footerFrame = QFrame(self.mainBodyContainer)
        self.footerFrame.setObjectName(u"footerFrame")
        sizePolicy1.setHeightForWidth(self.footerFrame.sizePolicy().hasHeightForWidth())
        self.footerFrame.setSizePolicy(sizePolicy1)
        self.footerFrame.setStyleSheet(u"background-color: rgb(150,0,0)")
        self.footerFrame.setFrameShape(QFrame.StyledPanel)
        self.footerFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footerFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 5, 0, 5)
        self.frame_7 = QFrame(self.footerFrame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.footerFrame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.frame_8, 0, Qt.AlignHCenter)

        self.size_grip = QFrame(self.footerFrame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(15, 15))
        self.size_grip.setMaximumSize(QSize(15, 15))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.size_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footerFrame)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuButton.setText("")
#if QT_CONFIG(tooltip)
        self.homeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u" Home", None))
#if QT_CONFIG(tooltip)
        self.launchMenuButton.setToolTip(QCoreApplication.translate("MainWindow", u"Launch Trajectory", None))
#endif // QT_CONFIG(tooltip)
        self.launchMenuButton.setText(QCoreApplication.translate("MainWindow", u" Launch", None))
#if QT_CONFIG(tooltip)
        self.statsButton.setToolTip(QCoreApplication.translate("MainWindow", u"Trajectory Statistics", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.statsButton.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.statsButton.setText(QCoreApplication.translate("MainWindow", u" Stats", None))
#if QT_CONFIG(tooltip)
        self.plotsButton.setToolTip(QCoreApplication.translate("MainWindow", u"Trajectory Plots", None))
#endif // QT_CONFIG(tooltip)
        self.plotsButton.setText(QCoreApplication.translate("MainWindow", u" Plots", None))
#if QT_CONFIG(tooltip)
        self.settingButton.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingButton.setText(QCoreApplication.translate("MainWindow", u"  Settings", None))
#if QT_CONFIG(tooltip)
        self.helpButton.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpButton.setText(QCoreApplication.translate("MainWindow", u"   Help", None))
        self.minimizeButton.setText("")
        self.maximizeButton.setText("")
        self.closeButton.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Select Medium: ", None))
        self.dragButton.setText(QCoreApplication.translate("MainWindow", u"Air", None))
        self.vacButton.setText(QCoreApplication.translate("MainWindow", u"Vaccum", None))
        self.compareButton.setText(QCoreApplication.translate("MainWindow", u"Compare", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Trajectory Type:", None))
        self.typeLabel.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.saveDataButton_3.setText(QCoreApplication.translate("MainWindow", u"Save Inputs", None))
        self.saveDataButton_2.setText(QCoreApplication.translate("MainWindow", u"Load Inputs", None))
        self.saveDataButton.setText(QCoreApplication.translate("MainWindow", u"Save Data", None))
        self.saveAnimButton.setText(QCoreApplication.translate("MainWindow", u"Save Animation", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Initial Conditions", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"x0:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"y0:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"v0:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Angle:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Multi-Trajectory Inputs", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Step angle:\n"
"(degrees)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Final angle:", None))
        self.stepAngleCounter.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Projectile Inputs", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Mass:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Radius:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Drag Conditions", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Drag Coefficient:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Sea Level Temperature:\n"
"(height variance)", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Wind Velocity:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Simulation Inputs", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Time Step:\n"
"(seconds)", None))
        self.timeStepCounter.setText(QCoreApplication.translate("MainWindow", u"0.05", None))
        self.displayLabel.setText("")
        self.launchButton_2.setText(QCoreApplication.translate("MainWindow", u"Plots", None))
        self.launchButton.setText(QCoreApplication.translate("MainWindow", u"LAUNCH", None))
        self.launchButton_3.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"Projectile Motion Physics Simulator", None))
        self.Description.setText(QCoreApplication.translate("MainWindow", u"Description Goes Here. Introduce some projectile motion physics, equations used, conditions available dsfg sdfg sdfg sf g ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Github", None))
    # retranslateUi

