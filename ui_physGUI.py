# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'physGUIFSlzcI.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1137, 677)
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
        self.menuSideBar.setMaximumSize(QSize(117, 16777215))
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

        self.plotsButton = QToolButton(self.menuFrame2)
        self.plotsButton.setObjectName(u"plotsButton")
        sizePolicy2.setHeightForWidth(self.plotsButton.sizePolicy().hasHeightForWidth())
        self.plotsButton.setSizePolicy(sizePolicy2)
        icon3 = QIcon()
        icon3.addFile(u":/Icons/iconsWhiteSize40/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.plotsButton.setIcon(icon3)
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
        icon4 = QIcon()
        icon4.addFile(u":/Icons/iconsWhiteSize40/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingButton.setIcon(icon4)
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
        icon5 = QIcon()
        icon5.addFile(u":/Icons/iconsWhiteSize40/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpButton.setIcon(icon5)
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
        self.fileOutFrame.setMaximumSize(QSize(16777215, 16777215))
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
        icon6 = QIcon()
        icon6.addFile(u":/Icons/iconsWhiteSize40/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon6)
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
        icon7 = QIcon()
        icon7.addFile(u":/Icons/iconsWhiteSize40/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeButton.setIcon(icon7)
        self.maximizeButton.setIconSize(QSize(25, 45))

        self.horizontalLayout_4.addWidget(self.maximizeButton)

        self.closeButton = QPushButton(self.windowFrame)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(50, 0))
        self.closeButton.setMaximumSize(QSize(50, 16777215))
        font2 = QFont()
        font2.setPointSize(12)
        self.closeButton.setFont(font2)
        icon8 = QIcon()
        icon8.addFile(u":/Icons/iconsWhiteSize40/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon8)
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
        font3 = QFont()
        font3.setPointSize(28)
        self.Title.setFont(font3)
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
        self.Description.setMaximumSize(QSize(16777215, 400))
        font4 = QFont()
        font4.setPointSize(14)
        self.Description.setFont(font4)
        self.Description.setTextFormat(Qt.RichText)
        self.Description.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.Description.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.Description)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.homePage)
        self.launchPage = QWidget()
        self.launchPage.setObjectName(u"launchPage")
        self.launchPage.setStyleSheet(u"QLineEdit{\n"
"background-color: white;\n"
"color:black;\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.launchPage)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.launchHeader = QFrame(self.launchPage)
        self.launchHeader.setObjectName(u"launchHeader")
        self.launchHeader.setMaximumSize(QSize(16777215, 16777215))
        self.launchHeader.setFrameShape(QFrame.StyledPanel)
        self.launchHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.launchHeader)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 10)
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
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        self.label_23.setFont(font5)

        self.horizontalLayout_18.addWidget(self.label_23, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.mediumLabelFrame)

        self.inputHeader = QFrame(self.launchHeader)
        self.inputHeader.setObjectName(u"inputHeader")
        sizePolicy1.setHeightForWidth(self.inputHeader.sizePolicy().hasHeightForWidth())
        self.inputHeader.setSizePolicy(sizePolicy1)
        self.inputHeader.setFrameShape(QFrame.StyledPanel)
        self.inputHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.inputHeader)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.dragButton = QRadioButton(self.inputHeader)
        self.dragButton.setObjectName(u"dragButton")
        self.dragButton.setMaximumSize(QSize(72, 16777215))
        font6 = QFont()
        font6.setPointSize(10)
        self.dragButton.setFont(font6)

        self.horizontalLayout_8.addWidget(self.dragButton)

        self.vacButton = QRadioButton(self.inputHeader)
        self.vacButton.setObjectName(u"vacButton")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.vacButton.sizePolicy().hasHeightForWidth())
        self.vacButton.setSizePolicy(sizePolicy6)
        self.vacButton.setMaximumSize(QSize(83, 16777215))
        self.vacButton.setFont(font6)

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
        self.horizontalLayout_17.setSpacing(8)
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
        self.label_20.setFont(font5)

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
        self.typeLabel.setFont(font5)
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
        self.displayHeader.setMinimumSize(QSize(360, 0))
        self.displayHeader.setMaximumSize(QSize(16777215, 16777215))
        self.displayHeader.setStyleSheet(u"QPushButton{\n"
"	border-radius: 12px;\n"
"	background-color: rgb(150, 0,0);\n"
"}")
        self.displayHeader.setFrameShape(QFrame.StyledPanel)
        self.displayHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.displayHeader)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 4, 0, 4)
        self.saveInputsButton = QPushButton(self.displayHeader)
        self.saveInputsButton.setObjectName(u"saveInputsButton")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.saveInputsButton.sizePolicy().hasHeightForWidth())
        self.saveInputsButton.setSizePolicy(sizePolicy7)
        self.saveInputsButton.setMinimumSize(QSize(85, 25))
        self.saveInputsButton.setMaximumSize(QSize(85, 100))
        font7 = QFont()
        font7.setPointSize(10)
        font7.setBold(True)
        self.saveInputsButton.setFont(font7)

        self.horizontalLayout_9.addWidget(self.saveInputsButton)

        self.loadInputsButton = QPushButton(self.displayHeader)
        self.loadInputsButton.setObjectName(u"loadInputsButton")
        sizePolicy7.setHeightForWidth(self.loadInputsButton.sizePolicy().hasHeightForWidth())
        self.loadInputsButton.setSizePolicy(sizePolicy7)
        self.loadInputsButton.setMinimumSize(QSize(85, 25))
        self.loadInputsButton.setMaximumSize(QSize(85, 100))
        self.loadInputsButton.setFont(font7)

        self.horizontalLayout_9.addWidget(self.loadInputsButton)

        self.saveDataButton = QPushButton(self.displayHeader)
        self.saveDataButton.setObjectName(u"saveDataButton")
        sizePolicy7.setHeightForWidth(self.saveDataButton.sizePolicy().hasHeightForWidth())
        self.saveDataButton.setSizePolicy(sizePolicy7)
        self.saveDataButton.setMinimumSize(QSize(85, 25))
        self.saveDataButton.setMaximumSize(QSize(85, 100))
        self.saveDataButton.setFont(font7)

        self.horizontalLayout_9.addWidget(self.saveDataButton)


        self.horizontalLayout_6.addWidget(self.displayHeader)


        self.verticalLayout_9.addWidget(self.launchHeader, 0, Qt.AlignTop)

        self.launchBody = QFrame(self.launchPage)
        self.launchBody.setObjectName(u"launchBody")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.launchBody.sizePolicy().hasHeightForWidth())
        self.launchBody.setSizePolicy(sizePolicy8)
        self.launchBody.setMaximumSize(QSize(16777215, 16777215))
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
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(95, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.launchGeneral.setPalette(palette)
        self.launchGeneral.setFrameShape(QFrame.StyledPanel)
        self.launchGeneral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.launchGeneral)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
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
        self.label_4.setFont(font5)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font5)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_16)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 0))
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        self.label_7.setFont(font5)
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
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.x0LineEdit.setPalette(palette1)
        self.x0LineEdit.setMaxLength(5)
        self.x0LineEdit.setFrame(True)
        self.x0LineEdit.setClearButtonEnabled(False)

        self.verticalLayout_18.addWidget(self.x0LineEdit)

        self.y0LineEdit = QLineEdit(self.frame_17)
        self.y0LineEdit.setObjectName(u"y0LineEdit")
        self.y0LineEdit.setMaximumSize(QSize(70, 16777215))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.y0LineEdit.setPalette(palette2)
        self.y0LineEdit.setMaxLength(5)

        self.verticalLayout_18.addWidget(self.y0LineEdit)

        self.v0LineEdit = QLineEdit(self.frame_17)
        self.v0LineEdit.setObjectName(u"v0LineEdit")
        self.v0LineEdit.setMaximumSize(QSize(70, 16777215))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.v0LineEdit.setPalette(palette3)
        self.v0LineEdit.setMaxLength(4)

        self.verticalLayout_18.addWidget(self.v0LineEdit)

        self.angleLineEdit = QLineEdit(self.frame_17)
        self.angleLineEdit.setObjectName(u"angleLineEdit")
        self.angleLineEdit.setMaximumSize(QSize(70, 16777215))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.angleLineEdit.setPalette(palette4)
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
        self.label_8.setFont(font5)

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
        self.label_9.setFont(font5)

        self.verticalLayout_21.addWidget(self.label_9, 0, Qt.AlignRight)

        self.label_10 = QLabel(self.frame_18)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font5)

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
        font8 = QFont()
        font8.setPointSize(11)
        self.stepAngleCounter.setFont(font8)

        self.verticalLayout_23.addWidget(self.stepAngleCounter, 0, Qt.AlignHCenter)

        self.stepAngleSlider = QSlider(self.frame_20)
        self.stepAngleSlider.setObjectName(u"stepAngleSlider")
        self.stepAngleSlider.setMaximumSize(QSize(80, 15))
        self.stepAngleSlider.setMinimum(0)
        self.stepAngleSlider.setMaximum(50)
        self.stepAngleSlider.setSingleStep(1)
        self.stepAngleSlider.setOrientation(Qt.Horizontal)
        self.stepAngleSlider.setTickPosition(QSlider.NoTicks)
        self.stepAngleSlider.setTickInterval(1)

        self.verticalLayout_23.addWidget(self.stepAngleSlider)


        self.verticalLayout_22.addWidget(self.frame_20)

        self.finalAngleLineEdit = QLineEdit(self.frame_19)
        self.finalAngleLineEdit.setObjectName(u"finalAngleLineEdit")
        self.finalAngleLineEdit.setMaximumSize(QSize(70, 16777215))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.finalAngleLineEdit.setPalette(palette5)
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
        self.label_11.setFont(font5)

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
        self.label_13.setFont(font5)

        self.verticalLayout_24.addWidget(self.label_13, 0, Qt.AlignRight)

        self.label_14 = QLabel(self.frame_21)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font5)

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
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Button, brush)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.massLineEdit.setPalette(palette6)
        self.massLineEdit.setMaxLength(4)

        self.verticalLayout_25.addWidget(self.massLineEdit)

        self.radiusLineEdit = QLineEdit(self.frame_22)
        self.radiusLineEdit.setObjectName(u"radiusLineEdit")
        self.radiusLineEdit.setMaximumSize(QSize(70, 16777215))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.radiusLineEdit.setPalette(palette7)
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
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
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
        self.label_12.setMinimumSize(QSize(159, 0))
        self.label_12.setFont(font5)
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_26.addWidget(self.label_12, 0, Qt.AlignRight)

        self.label_15 = QLabel(self.frame_23)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(165, 16777215))
        self.label_15.setFont(font5)
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
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.Button, brush)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.seaTemptLineEdit.setPalette(palette8)
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
        self.horizontalLayout_15.setSpacing(51)
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
        self.label_18.setFont(font5)
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
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.Button, brush)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.vWindLineEdit.setPalette(palette9)
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
        self.verticalLayout_15 = QVBoxLayout(self.frame_29)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_34 = QFrame(self.frame_29)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_16.setSpacing(51)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_34)
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
        self.label_19.setFont(font5)

        self.verticalLayout_30.addWidget(self.label_19)


        self.horizontalLayout_16.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_34)
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
        self.timeStepCounter.setFont(font8)

        self.verticalLayout_32.addWidget(self.timeStepCounter, 0, Qt.AlignHCenter)

        self.timeStepSlider = QSlider(self.frame_32)
        self.timeStepSlider.setObjectName(u"timeStepSlider")
        self.timeStepSlider.setMaximumSize(QSize(80, 15))
        self.timeStepSlider.setMinimum(10)
        self.timeStepSlider.setMaximum(100)
        self.timeStepSlider.setSingleStep(1)
        self.timeStepSlider.setOrientation(Qt.Horizontal)
        self.timeStepSlider.setTickPosition(QSlider.NoTicks)
        self.timeStepSlider.setTickInterval(1)

        self.verticalLayout_32.addWidget(self.timeStepSlider)


        self.verticalLayout_31.addWidget(self.frame_32)


        self.horizontalLayout_16.addWidget(self.frame_31)


        self.verticalLayout_15.addWidget(self.frame_34)

        self.frame_38 = QFrame(self.frame_29)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMaximumSize(QSize(300, 16777215))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(45, 0, 0, 16)
        self.realTimeRadioButton = QRadioButton(self.frame_38)
        self.realTimeRadioButton.setObjectName(u"realTimeRadioButton")

        self.horizontalLayout_20.addWidget(self.realTimeRadioButton)

        self.fastRadioButton = QRadioButton(self.frame_38)
        self.fastRadioButton.setObjectName(u"fastRadioButton")

        self.horizontalLayout_20.addWidget(self.fastRadioButton)


        self.verticalLayout_15.addWidget(self.frame_38)

        self.frame_37 = QFrame(self.frame_29)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(154, 0))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_37)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 13, 0, 0)
        self.launchButton = QPushButton(self.frame_37)
        self.launchButton.setObjectName(u"launchButton")
        sizePolicy1.setHeightForWidth(self.launchButton.sizePolicy().hasHeightForWidth())
        self.launchButton.setSizePolicy(sizePolicy1)
        self.launchButton.setMinimumSize(QSize(150, 35))
        self.launchButton.setMaximumSize(QSize(150, 35))
        self.launchButton.setFont(font1)
        self.launchButton.setStyleSheet(u"background-color: rgb(150, 0, 0);\n"
"border-radius:15px;")

        self.verticalLayout_34.addWidget(self.launchButton)


        self.verticalLayout_15.addWidget(self.frame_37, 0, Qt.AlignHCenter)


        self.verticalLayout_33.addWidget(self.frame_29)


        self.horizontalLayout_7.addWidget(self.launchDrag)

        self.launchDisplay = QFrame(self.launchBody)
        self.launchDisplay.setObjectName(u"launchDisplay")
        sizePolicy8.setHeightForWidth(self.launchDisplay.sizePolicy().hasHeightForWidth())
        self.launchDisplay.setSizePolicy(sizePolicy8)
        self.launchDisplay.setMinimumSize(QSize(0, 0))
        self.launchDisplay.setMaximumSize(QSize(629, 16777215))
        self.launchDisplay.setStyleSheet(u"QLabel #displayLabel{\n"
"border:5px solid white;\n"
"}")
        self.launchDisplay.setFrameShape(QFrame.StyledPanel)
        self.launchDisplay.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.launchDisplay)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.statsFrame = QFrame(self.launchDisplay)
        self.statsFrame.setObjectName(u"statsFrame")
        sizePolicy8.setHeightForWidth(self.statsFrame.sizePolicy().hasHeightForWidth())
        self.statsFrame.setSizePolicy(sizePolicy8)
        self.statsFrame.setMaximumSize(QSize(635, 450))
        self.statsFrame.setStyleSheet(u"#statsFrame{\n"
"border:2px dashed white;\n"
"}\n"
"QLineEdit{\n"
"	background-color: rgb(150, 150, 150);\n"
"}\n"
"")
        self.statsFrame.setFrameShape(QFrame.StyledPanel)
        self.statsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.statsFrame)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.statsFrame)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMaximumSize(QSize(16777215, 18))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_40)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_40)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"border-bottom:1px solid white;")

        self.verticalLayout_38.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.verticalLayout_37.addWidget(self.frame_40)

        self.singleStatsGroup = QGroupBox(self.statsFrame)
        self.singleStatsGroup.setObjectName(u"singleStatsGroup")
        self.singleStatsGroup.setMaximumSize(QSize(16777215, 56))
        font9 = QFont()
        font9.setPointSize(11)
        font9.setBold(False)
        font9.setItalic(True)
        self.singleStatsGroup.setFont(font9)
        self.singleStatsGroup.setStyleSheet(u"QLabel{\n"
"font-size:12px;\n"
"font-weight:bold;\n"
"}")
        self.horizontalLayout_21 = QHBoxLayout(self.singleStatsGroup)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 19, 0, 0)
        self.frame_41 = QFrame(self.singleStatsGroup)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMaximumSize(QSize(170, 16777215))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_17 = QLabel(self.frame_41)
        self.label_17.setObjectName(u"label_17")
        font10 = QFont()
        font10.setBold(True)
        self.label_17.setFont(font10)

        self.horizontalLayout_22.addWidget(self.label_17, 0, Qt.AlignHCenter)

        self.sRangeLE = QLineEdit(self.frame_41)
        self.sRangeLE.setObjectName(u"sRangeLE")
        self.sRangeLE.setMaximumSize(QSize(70, 16777215))
        self.sRangeLE.setReadOnly(True)

        self.horizontalLayout_22.addWidget(self.sRangeLE)


        self.horizontalLayout_21.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.singleStatsGroup)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMaximumSize(QSize(170, 16777215))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_22 = QLabel(self.frame_42)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font10)

        self.horizontalLayout_23.addWidget(self.label_22, 0, Qt.AlignHCenter)

        self.sHeightLE = QLineEdit(self.frame_42)
        self.sHeightLE.setObjectName(u"sHeightLE")
        self.sHeightLE.setMaximumSize(QSize(70, 16777215))
        self.sHeightLE.setReadOnly(True)

        self.horizontalLayout_23.addWidget(self.sHeightLE)


        self.horizontalLayout_21.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.singleStatsGroup)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMaximumSize(QSize(170, 16777215))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_24 = QLabel(self.frame_43)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font10)

        self.horizontalLayout_24.addWidget(self.label_24, 0, Qt.AlignHCenter)

        self.sTimeLE = QLineEdit(self.frame_43)
        self.sTimeLE.setObjectName(u"sTimeLE")
        self.sTimeLE.setMaximumSize(QSize(70, 16777215))
        self.sTimeLE.setReadOnly(True)

        self.horizontalLayout_24.addWidget(self.sTimeLE)


        self.horizontalLayout_21.addWidget(self.frame_43)


        self.verticalLayout_37.addWidget(self.singleStatsGroup)

        self.multiGroupBox = QGroupBox(self.statsFrame)
        self.multiGroupBox.setObjectName(u"multiGroupBox")
        sizePolicy3.setHeightForWidth(self.multiGroupBox.sizePolicy().hasHeightForWidth())
        self.multiGroupBox.setSizePolicy(sizePolicy3)
        self.multiGroupBox.setMaximumSize(QSize(200000, 55))
        self.multiGroupBox.setFont(font9)
        self.multiGroupBox.setStyleSheet(u"QLabel{\n"
"font-size:12px;\n"
"font-weight:bold;\n"
"}")
        self.horizontalLayout_25 = QHBoxLayout(self.multiGroupBox)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 26, 0, 0)
        self.frame_46 = QFrame(self.multiGroupBox)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMaximumSize(QSize(151, 50))
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.frame_46)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font10)

        self.horizontalLayout_27.addWidget(self.label_27, 0, Qt.AlignHCenter)

        self.mRangeLE = QLineEdit(self.frame_46)
        self.mRangeLE.setObjectName(u"mRangeLE")
        self.mRangeLE.setMaximumSize(QSize(70, 16777215))
        self.mRangeLE.setReadOnly(True)

        self.horizontalLayout_27.addWidget(self.mRangeLE)


        self.horizontalLayout_25.addWidget(self.frame_46)

        self.frame_45 = QFrame(self.multiGroupBox)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMaximumSize(QSize(150, 50))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.frame_45)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font10)

        self.horizontalLayout_26.addWidget(self.label_26, 0, Qt.AlignHCenter)

        self.mHeightLE = QLineEdit(self.frame_45)
        self.mHeightLE.setObjectName(u"mHeightLE")
        self.mHeightLE.setMaximumSize(QSize(70, 16777215))
        self.mHeightLE.setReadOnly(True)

        self.horizontalLayout_26.addWidget(self.mHeightLE)


        self.horizontalLayout_25.addWidget(self.frame_45)

        self.frame_47 = QFrame(self.multiGroupBox)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMaximumSize(QSize(173, 50))
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_47)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font10)

        self.horizontalLayout_28.addWidget(self.label_28, 0, Qt.AlignHCenter)

        self.mTimeLE = QLineEdit(self.frame_47)
        self.mTimeLE.setObjectName(u"mTimeLE")
        self.mTimeLE.setMaximumSize(QSize(70, 16777215))
        self.mTimeLE.setReadOnly(True)

        self.horizontalLayout_28.addWidget(self.mTimeLE)


        self.horizontalLayout_25.addWidget(self.frame_47)


        self.verticalLayout_37.addWidget(self.multiGroupBox)

        self.compareGroupBox = QGroupBox(self.statsFrame)
        self.compareGroupBox.setObjectName(u"compareGroupBox")
        self.compareGroupBox.setMaximumSize(QSize(16777215, 186))
        font11 = QFont()
        font11.setPointSize(11)
        font11.setItalic(True)
        self.compareGroupBox.setFont(font11)
        self.compareGroupBox.setStyleSheet(u"QLabel{\n"
"font-size:12px;\n"
"font-weight:bold;\n"
"}\n"
"")
        self.verticalLayout_39 = QVBoxLayout(self.compareGroupBox)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 25, 0, 0)
        self.groupBox_48 = QGroupBox(self.compareGroupBox)
        self.groupBox_48.setObjectName(u"groupBox_48")
        font12 = QFont()
        font12.setBold(False)
        self.groupBox_48.setFont(font12)
        self.groupBox_48.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_33 = QHBoxLayout(self.groupBox_48)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 16, 0, 0)
        self.frame_51 = QFrame(self.groupBox_48)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMaximumSize(QSize(170, 16777215))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_29 = QLabel(self.frame_51)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font10)

        self.horizontalLayout_30.addWidget(self.label_29, 0, Qt.AlignHCenter)

        self.cRangeLE = QLineEdit(self.frame_51)
        self.cRangeLE.setObjectName(u"cRangeLE")
        self.cRangeLE.setMaximumSize(QSize(70, 16777215))
        self.cRangeLE.setReadOnly(True)

        self.horizontalLayout_30.addWidget(self.cRangeLE)


        self.horizontalLayout_33.addWidget(self.frame_51)

        self.frame_52 = QFrame(self.groupBox_48)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMaximumSize(QSize(170, 16777215))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_30 = QLabel(self.frame_52)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font10)

        self.horizontalLayout_31.addWidget(self.label_30, 0, Qt.AlignHCenter)

        self.cHeightLE = QLineEdit(self.frame_52)
        self.cHeightLE.setObjectName(u"cHeightLE")
        self.cHeightLE.setMaximumSize(QSize(70, 16777215))
        self.cHeightLE.setReadOnly(True)

        self.horizontalLayout_31.addWidget(self.cHeightLE)


        self.horizontalLayout_33.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.groupBox_48)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMaximumSize(QSize(170, 16777215))
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_31 = QLabel(self.frame_53)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font10)

        self.horizontalLayout_32.addWidget(self.label_31, 0, Qt.AlignHCenter)

        self.cTimeLE = QLineEdit(self.frame_53)
        self.cTimeLE.setObjectName(u"cTimeLE")
        self.cTimeLE.setMaximumSize(QSize(70, 16777215))
        self.cTimeLE.setReadOnly(True)

        self.horizontalLayout_32.addWidget(self.cTimeLE)


        self.horizontalLayout_33.addWidget(self.frame_53)


        self.verticalLayout_39.addWidget(self.groupBox_48)

        self.groupBox_49 = QGroupBox(self.compareGroupBox)
        self.groupBox_49.setObjectName(u"groupBox_49")
        self.groupBox_49.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_37 = QHBoxLayout(self.groupBox_49)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 16, 0, 0)
        self.frame_54 = QFrame(self.groupBox_49)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMaximumSize(QSize(170, 16777215))
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_32 = QLabel(self.frame_54)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font10)

        self.horizontalLayout_34.addWidget(self.label_32, 0, Qt.AlignHCenter)

        self.cRangeLE_2 = QLineEdit(self.frame_54)
        self.cRangeLE_2.setObjectName(u"cRangeLE_2")
        self.cRangeLE_2.setMaximumSize(QSize(70, 16777215))
        self.cRangeLE_2.setReadOnly(True)

        self.horizontalLayout_34.addWidget(self.cRangeLE_2)


        self.horizontalLayout_37.addWidget(self.frame_54)

        self.frame_55 = QFrame(self.groupBox_49)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMaximumSize(QSize(170, 16777215))
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_33 = QLabel(self.frame_55)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font10)

        self.horizontalLayout_35.addWidget(self.label_33, 0, Qt.AlignHCenter)

        self.cHeightLE_2 = QLineEdit(self.frame_55)
        self.cHeightLE_2.setObjectName(u"cHeightLE_2")
        self.cHeightLE_2.setMaximumSize(QSize(70, 16777215))
        self.cHeightLE_2.setReadOnly(True)

        self.horizontalLayout_35.addWidget(self.cHeightLE_2)


        self.horizontalLayout_37.addWidget(self.frame_55)

        self.frame_56 = QFrame(self.groupBox_49)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMaximumSize(QSize(170, 16777215))
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_34 = QLabel(self.frame_56)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font10)

        self.horizontalLayout_36.addWidget(self.label_34, 0, Qt.AlignHCenter)

        self.cTimeLE_2 = QLineEdit(self.frame_56)
        self.cTimeLE_2.setObjectName(u"cTimeLE_2")
        self.cTimeLE_2.setMaximumSize(QSize(70, 16777215))
        self.cTimeLE_2.setReadOnly(True)

        self.horizontalLayout_36.addWidget(self.cTimeLE_2)


        self.horizontalLayout_37.addWidget(self.frame_56)


        self.verticalLayout_39.addWidget(self.groupBox_49)

        self.groupBox_50 = QGroupBox(self.compareGroupBox)
        self.groupBox_50.setObjectName(u"groupBox_50")
        self.groupBox_50.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_41 = QHBoxLayout(self.groupBox_50)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 16, 0, 0)
        self.frame_57 = QFrame(self.groupBox_50)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMaximumSize(QSize(170, 16777215))
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_35 = QLabel(self.frame_57)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font10)

        self.horizontalLayout_38.addWidget(self.label_35, 0, Qt.AlignHCenter)

        self.cRangeLE_3 = QLineEdit(self.frame_57)
        self.cRangeLE_3.setObjectName(u"cRangeLE_3")
        self.cRangeLE_3.setMaximumSize(QSize(70, 16777215))
        self.cRangeLE_3.setReadOnly(True)

        self.horizontalLayout_38.addWidget(self.cRangeLE_3)


        self.horizontalLayout_41.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.groupBox_50)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMaximumSize(QSize(170, 16777215))
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_36 = QLabel(self.frame_58)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font10)

        self.horizontalLayout_39.addWidget(self.label_36, 0, Qt.AlignHCenter)

        self.cHeightLE_3 = QLineEdit(self.frame_58)
        self.cHeightLE_3.setObjectName(u"cHeightLE_3")
        self.cHeightLE_3.setMaximumSize(QSize(70, 16777215))
        self.cHeightLE_3.setReadOnly(True)

        self.horizontalLayout_39.addWidget(self.cHeightLE_3)


        self.horizontalLayout_41.addWidget(self.frame_58)

        self.frame_59 = QFrame(self.groupBox_50)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMaximumSize(QSize(170, 16777215))
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_37 = QLabel(self.frame_59)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font10)

        self.horizontalLayout_40.addWidget(self.label_37, 0, Qt.AlignHCenter)

        self.cTimeLE_3 = QLineEdit(self.frame_59)
        self.cTimeLE_3.setObjectName(u"cTimeLE_3")
        self.cTimeLE_3.setMaximumSize(QSize(70, 16777215))
        self.cTimeLE_3.setReadOnly(True)

        self.horizontalLayout_40.addWidget(self.cTimeLE_3)


        self.horizontalLayout_41.addWidget(self.frame_59)


        self.verticalLayout_39.addWidget(self.groupBox_50)


        self.verticalLayout_37.addWidget(self.compareGroupBox)

        self.frame_39 = QFrame(self.statsFrame)
        self.frame_39.setObjectName(u"frame_39")
        sizePolicy2.setHeightForWidth(self.frame_39.sizePolicy().hasHeightForWidth())
        self.frame_39.setSizePolicy(sizePolicy2)
        self.frame_39.setMaximumSize(QSize(16777215, 50))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_48 = QFrame(self.frame_39)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(0, 35))
        self.frame_48.setMaximumSize(QSize(16777215, 39))
        self.frame_48.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(150,0,0);\n"
"border-radius: 12px;\n"
"}")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 20, 22)
        self.saveStatsButton = QPushButton(self.frame_48)
        self.saveStatsButton.setObjectName(u"saveStatsButton")
        sizePolicy1.setHeightForWidth(self.saveStatsButton.sizePolicy().hasHeightForWidth())
        self.saveStatsButton.setSizePolicy(sizePolicy1)
        self.saveStatsButton.setMinimumSize(QSize(100, 34))
        self.saveStatsButton.setMaximumSize(QSize(100, 23))
        self.saveStatsButton.setFont(font5)

        self.horizontalLayout_42.addWidget(self.saveStatsButton)

        self.openStatsButton = QPushButton(self.frame_48)
        self.openStatsButton.setObjectName(u"openStatsButton")
        sizePolicy1.setHeightForWidth(self.openStatsButton.sizePolicy().hasHeightForWidth())
        self.openStatsButton.setSizePolicy(sizePolicy1)
        self.openStatsButton.setMinimumSize(QSize(90, 35))
        self.openStatsButton.setMaximumSize(QSize(98, 23))
        self.openStatsButton.setFont(font5)

        self.horizontalLayout_42.addWidget(self.openStatsButton)


        self.horizontalLayout_43.addWidget(self.frame_48)


        self.verticalLayout_37.addWidget(self.frame_39)


        self.verticalLayout_10.addWidget(self.statsFrame)

        self.frame_4 = QFrame(self.launchDisplay)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 35))
        self.frame_4.setMaximumSize(QSize(16777215, 30))
        self.frame_4.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(150,0,0);\n"
"border-radius: 12px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(15, 2, 0, 14)
        self.createPlotsButton = QPushButton(self.frame_4)
        self.createPlotsButton.setObjectName(u"createPlotsButton")
        sizePolicy1.setHeightForWidth(self.createPlotsButton.sizePolicy().hasHeightForWidth())
        self.createPlotsButton.setSizePolicy(sizePolicy1)
        self.createPlotsButton.setMinimumSize(QSize(100, 30))
        self.createPlotsButton.setMaximumSize(QSize(100, 23))
        self.createPlotsButton.setFont(font5)

        self.horizontalLayout_19.addWidget(self.createPlotsButton)

        self.resetButton = QPushButton(self.frame_4)
        self.resetButton.setObjectName(u"resetButton")
        sizePolicy1.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy1)
        self.resetButton.setMinimumSize(QSize(90, 30))
        self.resetButton.setMaximumSize(QSize(98, 23))
        self.resetButton.setFont(font5)

        self.horizontalLayout_19.addWidget(self.resetButton)

        self.recentAnimButton = QPushButton(self.frame_4)
        self.recentAnimButton.setObjectName(u"recentAnimButton")
        sizePolicy1.setHeightForWidth(self.recentAnimButton.sizePolicy().hasHeightForWidth())
        self.recentAnimButton.setSizePolicy(sizePolicy1)
        self.recentAnimButton.setMinimumSize(QSize(182, 30))
        self.recentAnimButton.setMaximumSize(QSize(140, 29))
        self.recentAnimButton.setFont(font5)

        self.horizontalLayout_19.addWidget(self.recentAnimButton)


        self.verticalLayout_10.addWidget(self.frame_4)


        self.horizontalLayout_7.addWidget(self.launchDisplay)


        self.verticalLayout_9.addWidget(self.launchBody)

        self.stackedWidget.addWidget(self.launchPage)
        self.plotsPage = QWidget()
        self.plotsPage.setObjectName(u"plotsPage")
        self.verticalLayout_40 = QVBoxLayout(self.plotsPage)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.plotsPage)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_29 = QHBoxLayout(self.page)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.frame_50 = QFrame(self.page)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMaximumSize(QSize(150, 16777215))
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_50)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.prevPlotButton = QPushButton(self.frame_50)
        self.prevPlotButton.setObjectName(u"prevPlotButton")
        self.prevPlotButton.setMinimumSize(QSize(86, 26))
        self.prevPlotButton.setMaximumSize(QSize(113, 16777215))
        self.prevPlotButton.setFont(font7)
        self.prevPlotButton.setStyleSheet(u"border-radius:5px;\n"
"background-color: rgb(150, 0, 0);")

        self.verticalLayout_41.addWidget(self.prevPlotButton, 0, Qt.AlignHCenter)


        self.horizontalLayout_29.addWidget(self.frame_50)

        self.plotDisplayLabel = QLabel(self.page)
        self.plotDisplayLabel.setObjectName(u"plotDisplayLabel")
        self.plotDisplayLabel.setMinimumSize(QSize(667, 500))
        self.plotDisplayLabel.setMaximumSize(QSize(667, 500))
        font13 = QFont()
        font13.setPointSize(16)
        font13.setBold(True)
        self.plotDisplayLabel.setFont(font13)
        self.plotDisplayLabel.setScaledContents(True)
        self.plotDisplayLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.plotDisplayLabel)

        self.frame_49 = QFrame(self.page)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMaximumSize(QSize(150, 16777215))
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_49)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.nextPlotButton = QPushButton(self.frame_49)
        self.nextPlotButton.setObjectName(u"nextPlotButton")
        self.nextPlotButton.setMinimumSize(QSize(75, 25))
        self.nextPlotButton.setFont(font7)
        self.nextPlotButton.setStyleSheet(u"border-radius:5px;\n"
"background-color: rgb(150, 0, 0);")

        self.verticalLayout_42.addWidget(self.nextPlotButton, 0, Qt.AlignHCenter)


        self.horizontalLayout_29.addWidget(self.frame_49)

        self.stackedWidget_2.addWidget(self.page)

        self.verticalLayout_40.addWidget(self.stackedWidget_2)

        self.frame_44 = QFrame(self.plotsPage)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(0, 75))
        self.frame_44.setMaximumSize(QSize(16777215, 16777215))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.savePlotsButton = QPushButton(self.frame_44)
        self.savePlotsButton.setObjectName(u"savePlotsButton")
        self.savePlotsButton.setMaximumSize(QSize(103, 41))
        self.savePlotsButton.setFont(font1)
        self.savePlotsButton.setStyleSheet(u"border-radius:5px;\n"
"background-color: rgb(150, 0, 0);")

        self.horizontalLayout_44.addWidget(self.savePlotsButton)


        self.verticalLayout_40.addWidget(self.frame_44)

        self.stackedWidget.addWidget(self.plotsPage)

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

        self.stackedWidget.setCurrentIndex(1)


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
        self.Title.setText(QCoreApplication.translate("MainWindow", u"Projectile Motion Physics Simulator", None))
        self.Description.setText(QCoreApplication.translate("MainWindow", u"In this Sim, you will be able to determine how each parameter (initial height, initial angle, initial speed, mass, diameter, and altitude) affects the trajectory of an object, with and without air resistance.\n"
"\n"
"Predict how varying the initial conditions will affect a projectile\u2019s path, and provide an explanation for the prediction.\n"
"\n"
"Estimate where an object will land, given its initial conditions.\n"
"\n"
"Determine that the x and y motion of a projectile are independent.\n"
"\n"
"Investigate the variables that affect the drag force.\n"
"\n"
"Describe the the effect that the drag force has on the velocity and acceleration.\n"
"\n"
"Discuss projectile motion using common vocabulary (such as: launch angle, initial speed, initial height, range, time).", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Select Medium: ", None))
        self.dragButton.setText(QCoreApplication.translate("MainWindow", u"Air", None))
        self.vacButton.setText(QCoreApplication.translate("MainWindow", u"Vaccum", None))
        self.compareButton.setText(QCoreApplication.translate("MainWindow", u"Compare", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Trajectory Type:", None))
        self.typeLabel.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.saveInputsButton.setText(QCoreApplication.translate("MainWindow", u"Save Inputs", None))
        self.loadInputsButton.setText(QCoreApplication.translate("MainWindow", u"Load Inputs", None))
        self.saveDataButton.setText(QCoreApplication.translate("MainWindow", u"Save Data", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Initial Condition Inputs", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"x0:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"y0:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"v0:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Angle:", None))
        self.x0LineEdit.setText("")
        self.x0LineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(meters)", None))
        self.y0LineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(meters)", None))
        self.v0LineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(m/s)", None))
        self.angleLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(degrees)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Multi-Trajectory Inputs", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Step angle:\n"
"(degrees)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Final angle:", None))
        self.stepAngleCounter.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.finalAngleLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(degrees)", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Projectile Inputs", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Mass:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Radius:", None))
        self.massLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(kg)", None))
        self.radiusLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(meters)", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Drag Condition Inputs", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Drag Coefficient:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Sea Level Temperature:\n"
"(Air density variance)", None))
        self.seaTemptLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(kelvin)", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Wind Velocity:", None))
        self.vWindLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(+- m/s)", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Simulation Inputs", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Time Step:\n"
"(seconds)", None))
        self.timeStepCounter.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.realTimeRadioButton.setText(QCoreApplication.translate("MainWindow", u"Real Time", None))
        self.fastRadioButton.setText(QCoreApplication.translate("MainWindow", u"Fast", None))
        self.launchButton.setText(QCoreApplication.translate("MainWindow", u"LAUNCH", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Trajectory Stats", None))
        self.singleStatsGroup.setTitle(QCoreApplication.translate("MainWindow", u"Single Trajectory Stats", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Range:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Flight Time:", None))
        self.multiGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Multi-Trajectory Maximum Stats", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Max Range:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Max Height:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Max Flight Time:", None))
        self.compareGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Compare Trajectory Stats", None))
        self.groupBox_48.setTitle(QCoreApplication.translate("MainWindow", u"Non-Adiabatic Drag Trajectory", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Range:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Flight Time:", None))
        self.groupBox_49.setTitle(QCoreApplication.translate("MainWindow", u"Adiabatic-Drag Trajectory", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Range:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Flight Time:", None))
        self.groupBox_50.setTitle(QCoreApplication.translate("MainWindow", u"Vaccum Trajecory", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Range:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Flight Time:", None))
        self.saveStatsButton.setText(QCoreApplication.translate("MainWindow", u"Save Stats", None))
        self.openStatsButton.setText(QCoreApplication.translate("MainWindow", u"Open Stats", None))
        self.createPlotsButton.setText(QCoreApplication.translate("MainWindow", u"Create Plots", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.recentAnimButton.setText(QCoreApplication.translate("MainWindow", u"Show Recent Animation", None))
        self.prevPlotButton.setText(QCoreApplication.translate("MainWindow", u"Previous Plot", None))
        self.plotDisplayLabel.setText(QCoreApplication.translate("MainWindow", u"No Plots Created to Display", None))
        self.nextPlotButton.setText(QCoreApplication.translate("MainWindow", u"Next Plot", None))
        self.savePlotsButton.setText(QCoreApplication.translate("MainWindow", u"Save Plots", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Github", None))
    # retranslateUi

