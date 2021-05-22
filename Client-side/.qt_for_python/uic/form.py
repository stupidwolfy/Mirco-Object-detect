# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_App(object):
    def setupUi(self, App):
        if not App.objectName():
            App.setObjectName(u"App")
        App.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(App.sizePolicy().hasHeightForWidth())
        App.setSizePolicy(sizePolicy)
        self.gridLayoutWidget = QWidget(App)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 20, 741, 551))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.SettingTab = QTabWidget(self.gridLayoutWidget)
        self.SettingTab.setObjectName(u"SettingTab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SettingTab.sizePolicy().hasHeightForWidth())
        self.SettingTab.setSizePolicy(sizePolicy1)
        self.MonitorTab = QWidget()
        self.MonitorTab.setObjectName(u"MonitorTab")
        self.verticalLayoutWidget = QWidget(self.MonitorTab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 0, 661, 491))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(800, 700))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.pushButton_2 = QPushButton(self.MonitorTab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(340, 500, 75, 23))
        self.SettingTab.addTab(self.MonitorTab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setEnabled(True)
        self.formLayoutWidget = QWidget(self.tab_2)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 721, 451))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.checkBox = QCheckBox(self.formLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.checkBox)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_13 = QCheckBox(self.formLayoutWidget)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setEnabled(False)

        self.gridLayout_3.addWidget(self.checkBox_13, 0, 1, 1, 1)

        self.checkBox_12 = QCheckBox(self.formLayoutWidget)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setEnabled(False)

        self.gridLayout_3.addWidget(self.checkBox_12, 0, 0, 1, 1)


        self.formLayout_3.setLayout(2, QFormLayout.FieldRole, self.gridLayout_3)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton = QRadioButton(self.formLayoutWidget)
        self.buttonGroup1 = QButtonGroup(App)
        self.buttonGroup1.setObjectName(u"buttonGroup1")
        self.buttonGroup1.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setEnabled(False)

        self.verticalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup1.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setEnabled(False)

        self.verticalLayout_2.addWidget(self.radioButton_2)


        self.formLayout_3.setLayout(1, QFormLayout.FieldRole, self.verticalLayout_2)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_2 = QCheckBox(self.formLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(False)

        self.gridLayout_2.addWidget(self.checkBox_2, 0, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.formLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setEnabled(False)

        self.gridLayout_2.addWidget(self.checkBox_3, 0, 1, 1, 1)

        self.checkBox_8 = QCheckBox(self.formLayoutWidget)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setEnabled(False)

        self.gridLayout_2.addWidget(self.checkBox_8, 1, 2, 1, 1)

        self.checkBox_9 = QCheckBox(self.formLayoutWidget)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setEnabled(False)

        self.gridLayout_2.addWidget(self.checkBox_9, 1, 3, 1, 1)

        self.checkBox_7 = QCheckBox(self.formLayoutWidget)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setEnabled(False)

        self.gridLayout_2.addWidget(self.checkBox_7, 1, 1, 1, 1)

        self.checkBox_4 = QCheckBox(self.formLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(False)

        self.gridLayout_2.addWidget(self.checkBox_4, 0, 2, 1, 1)

        self.checkBox_6 = QCheckBox(self.formLayoutWidget)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setEnabled(False)

        self.gridLayout_2.addWidget(self.checkBox_6, 1, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.formLayoutWidget)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setEnabled(False)

        self.gridLayout_2.addWidget(self.checkBox_5, 0, 3, 1, 1)

        self.checkBox_10 = QCheckBox(self.formLayoutWidget)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setEnabled(False)

        self.gridLayout_2.addWidget(self.checkBox_10, 0, 4, 1, 1)

        self.checkBox_11 = QCheckBox(self.formLayoutWidget)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setEnabled(False)

        self.gridLayout_2.addWidget(self.checkBox_11, 1, 4, 1, 1)


        self.formLayout_3.setLayout(0, QFormLayout.FieldRole, self.gridLayout_2)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.radioButton_3 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup = QButtonGroup(App)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setEnabled(False)

        self.gridLayout_6.addWidget(self.radioButton_3, 0, 0, 1, 1)

        self.radioButton_4 = QRadioButton(self.formLayoutWidget)
        self.buttonGroup.addButton(self.radioButton_4)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setEnabled(False)

        self.gridLayout_6.addWidget(self.radioButton_4, 0, 1, 1, 1)


        self.formLayout_3.setLayout(3, QFormLayout.FieldRole, self.gridLayout_6)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.formLayout_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scrollArea = QScrollArea(self.formLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 625, 208))
        self.gridLayoutWidget_5 = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 0, 621, 272))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.checkBox_32 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_32.setObjectName(u"checkBox_32")

        self.gridLayout_5.addWidget(self.checkBox_32, 2, 4, 1, 1)

        self.checkBox_69 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_69.setObjectName(u"checkBox_69")

        self.gridLayout_5.addWidget(self.checkBox_69, 7, 6, 1, 1)

        self.checkBox_35 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_35.setObjectName(u"checkBox_35")

        self.gridLayout_5.addWidget(self.checkBox_35, 3, 1, 1, 1)

        self.checkBox_77 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_77.setObjectName(u"checkBox_77")

        self.gridLayout_5.addWidget(self.checkBox_77, 9, 1, 1, 1)

        self.checkBox_41 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_41.setObjectName(u"checkBox_41")

        self.gridLayout_5.addWidget(self.checkBox_41, 3, 6, 1, 1)

        self.checkBox_88 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_88.setObjectName(u"checkBox_88")

        self.gridLayout_5.addWidget(self.checkBox_88, 10, 4, 1, 1)

        self.checkBox_89 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_89.setObjectName(u"checkBox_89")

        self.gridLayout_5.addWidget(self.checkBox_89, 10, 5, 1, 1)

        self.checkBox_87 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_87.setObjectName(u"checkBox_87")

        self.gridLayout_5.addWidget(self.checkBox_87, 10, 3, 1, 1)

        self.checkBox_36 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_36.setObjectName(u"checkBox_36")

        self.gridLayout_5.addWidget(self.checkBox_36, 3, 0, 1, 1)

        self.checkBox_67 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_67.setObjectName(u"checkBox_67")

        self.gridLayout_5.addWidget(self.checkBox_67, 7, 4, 1, 1)

        self.checkBox_51 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_51.setObjectName(u"checkBox_51")

        self.gridLayout_5.addWidget(self.checkBox_51, 5, 2, 1, 1)

        self.checkBox_49 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_49.setObjectName(u"checkBox_49")

        self.gridLayout_5.addWidget(self.checkBox_49, 5, 0, 1, 1)

        self.checkBox_25 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_25.setObjectName(u"checkBox_25")

        self.gridLayout_5.addWidget(self.checkBox_25, 1, 5, 1, 1)

        self.checkBox_27 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_27.setObjectName(u"checkBox_27")

        self.gridLayout_5.addWidget(self.checkBox_27, 1, 6, 1, 1)

        self.checkBox_44 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_44.setObjectName(u"checkBox_44")

        self.gridLayout_5.addWidget(self.checkBox_44, 4, 2, 1, 1)

        self.checkBox_34 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_34.setObjectName(u"checkBox_34")

        self.gridLayout_5.addWidget(self.checkBox_34, 2, 6, 1, 1)

        self.checkBox_70 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_70.setObjectName(u"checkBox_70")

        self.gridLayout_5.addWidget(self.checkBox_70, 8, 1, 1, 1)

        self.checkBox_14 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.gridLayout_5.addWidget(self.checkBox_14, 0, 0, 1, 1)

        self.checkBox_84 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_84.setObjectName(u"checkBox_84")

        self.gridLayout_5.addWidget(self.checkBox_84, 10, 0, 1, 1)

        self.checkBox_83 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_83.setObjectName(u"checkBox_83")

        self.gridLayout_5.addWidget(self.checkBox_83, 9, 6, 1, 1)

        self.checkBox_24 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_24.setObjectName(u"checkBox_24")

        self.gridLayout_5.addWidget(self.checkBox_24, 0, 5, 1, 1)

        self.checkBox_75 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_75.setObjectName(u"checkBox_75")

        self.gridLayout_5.addWidget(self.checkBox_75, 8, 5, 1, 1)

        self.checkBox_21 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_21.setObjectName(u"checkBox_21")

        self.gridLayout_5.addWidget(self.checkBox_21, 1, 3, 1, 1)

        self.checkBox_52 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_52.setObjectName(u"checkBox_52")

        self.gridLayout_5.addWidget(self.checkBox_52, 5, 3, 1, 1)

        self.checkBox_82 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_82.setObjectName(u"checkBox_82")

        self.gridLayout_5.addWidget(self.checkBox_82, 9, 5, 1, 1)

        self.checkBox_63 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_63.setObjectName(u"checkBox_63")

        self.gridLayout_5.addWidget(self.checkBox_63, 7, 0, 1, 1)

        self.checkBox_86 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_86.setObjectName(u"checkBox_86")

        self.gridLayout_5.addWidget(self.checkBox_86, 10, 2, 1, 1)

        self.checkBox_28 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_28.setObjectName(u"checkBox_28")

        self.gridLayout_5.addWidget(self.checkBox_28, 2, 1, 1, 1)

        self.checkBox_53 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_53.setObjectName(u"checkBox_53")

        self.gridLayout_5.addWidget(self.checkBox_53, 5, 4, 1, 1)

        self.checkBox_48 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_48.setObjectName(u"checkBox_48")

        self.gridLayout_5.addWidget(self.checkBox_48, 4, 6, 1, 1)

        self.checkBox_57 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_57.setObjectName(u"checkBox_57")

        self.gridLayout_5.addWidget(self.checkBox_57, 6, 1, 1, 1)

        self.checkBox_79 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_79.setObjectName(u"checkBox_79")

        self.gridLayout_5.addWidget(self.checkBox_79, 9, 2, 1, 1)

        self.checkBox_56 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_56.setObjectName(u"checkBox_56")

        self.gridLayout_5.addWidget(self.checkBox_56, 6, 0, 1, 1)

        self.checkBox_78 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_78.setObjectName(u"checkBox_78")

        self.gridLayout_5.addWidget(self.checkBox_78, 9, 0, 1, 1)

        self.checkBox_46 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_46.setObjectName(u"checkBox_46")

        self.gridLayout_5.addWidget(self.checkBox_46, 4, 4, 1, 1)

        self.checkBox_30 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_30.setObjectName(u"checkBox_30")

        self.gridLayout_5.addWidget(self.checkBox_30, 2, 2, 1, 1)

        self.checkBox_76 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_76.setObjectName(u"checkBox_76")

        self.gridLayout_5.addWidget(self.checkBox_76, 8, 6, 1, 1)

        self.checkBox_26 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_26.setObjectName(u"checkBox_26")

        self.gridLayout_5.addWidget(self.checkBox_26, 0, 6, 1, 1)

        self.checkBox_54 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_54.setObjectName(u"checkBox_54")

        self.gridLayout_5.addWidget(self.checkBox_54, 5, 5, 1, 1)

        self.checkBox_85 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_85.setObjectName(u"checkBox_85")

        self.gridLayout_5.addWidget(self.checkBox_85, 10, 1, 1, 1)

        self.checkBox_80 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_80.setObjectName(u"checkBox_80")

        self.gridLayout_5.addWidget(self.checkBox_80, 9, 3, 1, 1)

        self.checkBox_74 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_74.setObjectName(u"checkBox_74")

        self.gridLayout_5.addWidget(self.checkBox_74, 8, 4, 1, 1)

        self.checkBox_22 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_22.setObjectName(u"checkBox_22")

        self.gridLayout_5.addWidget(self.checkBox_22, 1, 2, 1, 1)

        self.checkBox_55 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_55.setObjectName(u"checkBox_55")

        self.gridLayout_5.addWidget(self.checkBox_55, 5, 6, 1, 1)

        self.checkBox_64 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_64.setObjectName(u"checkBox_64")

        self.gridLayout_5.addWidget(self.checkBox_64, 7, 1, 1, 1)

        self.checkBox_68 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_68.setObjectName(u"checkBox_68")

        self.gridLayout_5.addWidget(self.checkBox_68, 7, 5, 1, 1)

        self.checkBox_31 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_31.setObjectName(u"checkBox_31")

        self.gridLayout_5.addWidget(self.checkBox_31, 2, 3, 1, 1)

        self.checkBox_39 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_39.setObjectName(u"checkBox_39")

        self.gridLayout_5.addWidget(self.checkBox_39, 3, 4, 1, 1)

        self.checkBox_61 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_61.setObjectName(u"checkBox_61")

        self.gridLayout_5.addWidget(self.checkBox_61, 6, 5, 1, 1)

        self.checkBox_59 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_59.setObjectName(u"checkBox_59")

        self.gridLayout_5.addWidget(self.checkBox_59, 6, 3, 1, 1)

        self.checkBox_23 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_23.setObjectName(u"checkBox_23")

        self.gridLayout_5.addWidget(self.checkBox_23, 1, 4, 1, 1)

        self.checkBox_33 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_33.setObjectName(u"checkBox_33")

        self.gridLayout_5.addWidget(self.checkBox_33, 2, 5, 1, 1)

        self.checkBox_58 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_58.setObjectName(u"checkBox_58")

        self.gridLayout_5.addWidget(self.checkBox_58, 6, 2, 1, 1)

        self.checkBox_47 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_47.setObjectName(u"checkBox_47")

        self.gridLayout_5.addWidget(self.checkBox_47, 4, 5, 1, 1)

        self.checkBox_81 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_81.setObjectName(u"checkBox_81")

        self.gridLayout_5.addWidget(self.checkBox_81, 9, 4, 1, 1)

        self.checkBox_60 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_60.setObjectName(u"checkBox_60")

        self.gridLayout_5.addWidget(self.checkBox_60, 6, 4, 1, 1)

        self.checkBox_45 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_45.setObjectName(u"checkBox_45")

        self.gridLayout_5.addWidget(self.checkBox_45, 4, 3, 1, 1)

        self.checkBox_73 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_73.setObjectName(u"checkBox_73")

        self.gridLayout_5.addWidget(self.checkBox_73, 8, 3, 1, 1)

        self.checkBox_40 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_40.setObjectName(u"checkBox_40")

        self.gridLayout_5.addWidget(self.checkBox_40, 3, 5, 1, 1)

        self.checkBox_72 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_72.setObjectName(u"checkBox_72")

        self.gridLayout_5.addWidget(self.checkBox_72, 8, 2, 1, 1)

        self.checkBox_50 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_50.setObjectName(u"checkBox_50")

        self.gridLayout_5.addWidget(self.checkBox_50, 5, 1, 1, 1)

        self.checkBox_20 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_20.setObjectName(u"checkBox_20")

        self.gridLayout_5.addWidget(self.checkBox_20, 0, 4, 1, 1)

        self.checkBox_29 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_29.setObjectName(u"checkBox_29")

        self.gridLayout_5.addWidget(self.checkBox_29, 2, 0, 1, 1)

        self.checkBox_42 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_42.setObjectName(u"checkBox_42")

        self.gridLayout_5.addWidget(self.checkBox_42, 4, 1, 1, 1)

        self.checkBox_65 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_65.setObjectName(u"checkBox_65")

        self.gridLayout_5.addWidget(self.checkBox_65, 7, 2, 1, 1)

        self.checkBox_18 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_18.setObjectName(u"checkBox_18")

        self.gridLayout_5.addWidget(self.checkBox_18, 0, 2, 1, 1)

        self.checkBox_43 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_43.setObjectName(u"checkBox_43")

        self.gridLayout_5.addWidget(self.checkBox_43, 4, 0, 1, 1)

        self.checkBox_71 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_71.setObjectName(u"checkBox_71")

        self.gridLayout_5.addWidget(self.checkBox_71, 8, 0, 1, 1)

        self.checkBox_38 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_38.setObjectName(u"checkBox_38")

        self.gridLayout_5.addWidget(self.checkBox_38, 3, 3, 1, 1)

        self.checkBox_16 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.gridLayout_5.addWidget(self.checkBox_16, 0, 1, 1, 1)

        self.checkBox_15 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.gridLayout_5.addWidget(self.checkBox_15, 1, 0, 1, 1)

        self.checkBox_17 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_17.setObjectName(u"checkBox_17")

        self.gridLayout_5.addWidget(self.checkBox_17, 1, 1, 1, 1)

        self.checkBox_90 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_90.setObjectName(u"checkBox_90")

        self.gridLayout_5.addWidget(self.checkBox_90, 10, 6, 1, 1)

        self.checkBox_66 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_66.setObjectName(u"checkBox_66")

        self.gridLayout_5.addWidget(self.checkBox_66, 7, 3, 1, 1)

        self.checkBox_62 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_62.setObjectName(u"checkBox_62")

        self.gridLayout_5.addWidget(self.checkBox_62, 6, 6, 1, 1)

        self.checkBox_37 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_37.setObjectName(u"checkBox_37")

        self.gridLayout_5.addWidget(self.checkBox_37, 3, 2, 1, 1)

        self.checkBox_19 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_19.setObjectName(u"checkBox_19")

        self.gridLayout_5.addWidget(self.checkBox_19, 0, 3, 1, 1)

        self.checkBox_91 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_91.setObjectName(u"checkBox_91")

        self.gridLayout_5.addWidget(self.checkBox_91, 11, 1, 1, 1)

        self.checkBox_92 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_92.setObjectName(u"checkBox_92")

        self.gridLayout_5.addWidget(self.checkBox_92, 11, 0, 1, 1)

        self.checkBox_93 = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_93.setObjectName(u"checkBox_93")

        self.gridLayout_5.addWidget(self.checkBox_93, 11, 2, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 0, 1, 1, 1)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.gridLayout_4)

        self.pushButton = QPushButton(self.tab_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(624, 482, 91, 31))
        self.SettingTab.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.SettingTab, 0, 0, 1, 1)


        self.retranslateUi(App)

        self.SettingTab.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(App)
    # setupUi

    def retranslateUi(self, App):
        App.setWindowTitle(QCoreApplication.translate("App", u"App", None))
        self.label.setText(QCoreApplication.translate("App", u"Camera 1", None))
        self.pushButton_2.setText(QCoreApplication.translate("App", u"Start", None))
        self.SettingTab.setTabText(self.SettingTab.indexOf(self.MonitorTab), QCoreApplication.translate("App", u"Monitor", None))
        self.label_2.setText(QCoreApplication.translate("App", u"Object Target", None))
        self.label_4.setText(QCoreApplication.translate("App", u"Trigger IO", None))
        self.checkBox.setText("")
        self.label_6.setText(QCoreApplication.translate("App", u"Trigger Option", None))
        self.checkBox_13.setText(QCoreApplication.translate("App", u"Random trigger one from selected", None))
        self.checkBox_12.setText(QCoreApplication.translate("App", u"Keep last trigger vlaue", None))
        self.label_3.setText(QCoreApplication.translate("App", u"Trigger Mode", None))
        self.radioButton.setText(QCoreApplication.translate("App", u"High on Trigger", None))
        self.radioButton_2.setText(QCoreApplication.translate("App", u"Low on Trigger", None))
        self.label_5.setText(QCoreApplication.translate("App", u"IO Select (BCM)", None))
        self.checkBox_2.setText(QCoreApplication.translate("App", u"4", None))
        self.checkBox_3.setText(QCoreApplication.translate("App", u"5", None))
        self.checkBox_8.setText(QCoreApplication.translate("App", u"25", None))
        self.checkBox_9.setText(QCoreApplication.translate("App", u"26", None))
        self.checkBox_7.setText(QCoreApplication.translate("App", u"24", None))
        self.checkBox_4.setText(QCoreApplication.translate("App", u"12", None))
        self.checkBox_6.setText(QCoreApplication.translate("App", u"23", None))
        self.checkBox_5.setText(QCoreApplication.translate("App", u"13", None))
        self.checkBox_10.setText(QCoreApplication.translate("App", u"22", None))
        self.checkBox_11.setText(QCoreApplication.translate("App", u"27", None))
        self.label_7.setText(QCoreApplication.translate("App", u"Trigger Mode", None))
        self.radioButton_3.setText(QCoreApplication.translate("App", u"On found on item", None))
        self.radioButton_4.setText(QCoreApplication.translate("App", u"On found all item", None))
        self.checkBox_32.setText(QCoreApplication.translate("App", u"sheep", None))
        self.checkBox_69.setText(QCoreApplication.translate("App", u"cake", None))
        self.checkBox_35.setText(QCoreApplication.translate("App", u"zebra", None))
        self.checkBox_77.setText(QCoreApplication.translate("App", u"mouse", None))
        self.checkBox_41.setText(QCoreApplication.translate("App", u"tie", None))
        self.checkBox_88.setText(QCoreApplication.translate("App", u"clock", None))
        self.checkBox_89.setText(QCoreApplication.translate("App", u"vase", None))
        self.checkBox_87.setText(QCoreApplication.translate("App", u"book", None))
        self.checkBox_36.setText(QCoreApplication.translate("App", u"bear", None))
        self.checkBox_67.setText(QCoreApplication.translate("App", u"pizza", None))
        self.checkBox_51.setText(QCoreApplication.translate("App", u"surfboard", None))
        self.checkBox_49.setText(QCoreApplication.translate("App", u"baseball glove", None))
        self.checkBox_25.setText(QCoreApplication.translate("App", u"parking meter", None))
        self.checkBox_27.setText(QCoreApplication.translate("App", u"bench", None))
        self.checkBox_44.setText(QCoreApplication.translate("App", u"skis", None))
        self.checkBox_34.setText(QCoreApplication.translate("App", u"elephant", None))
        self.checkBox_70.setText(QCoreApplication.translate("App", u"couch", None))
        self.checkBox_14.setText(QCoreApplication.translate("App", u"person", None))
        self.checkBox_84.setText(QCoreApplication.translate("App", u"toaster", None))
        self.checkBox_83.setText(QCoreApplication.translate("App", u"oven", None))
        self.checkBox_24.setText(QCoreApplication.translate("App", u"bus", None))
        self.checkBox_75.setText(QCoreApplication.translate("App", u"toilet", None))
        self.checkBox_21.setText(QCoreApplication.translate("App", u"fire hydrant", None))
        self.checkBox_52.setText(QCoreApplication.translate("App", u"tennis racket", None))
        self.checkBox_82.setText(QCoreApplication.translate("App", u"microwave", None))
        self.checkBox_63.setText(QCoreApplication.translate("App", u"orange", None))
        self.checkBox_86.setText(QCoreApplication.translate("App", u"refrigerator", None))
        self.checkBox_28.setText(QCoreApplication.translate("App", u"cat", None))
        self.checkBox_53.setText(QCoreApplication.translate("App", u"bottle", None))
        self.checkBox_48.setText(QCoreApplication.translate("App", u"baseball bat", None))
        self.checkBox_57.setText(QCoreApplication.translate("App", u"knife", None))
        self.checkBox_79.setText(QCoreApplication.translate("App", u"remote", None))
        self.checkBox_56.setText(QCoreApplication.translate("App", u"fork", None))
        self.checkBox_78.setText(QCoreApplication.translate("App", u"laptop", None))
        self.checkBox_46.setText(QCoreApplication.translate("App", u"sports ball", None))
        self.checkBox_30.setText(QCoreApplication.translate("App", u"dog", None))
        self.checkBox_76.setText(QCoreApplication.translate("App", u"tv", None))
        self.checkBox_26.setText(QCoreApplication.translate("App", u"train", None))
        self.checkBox_54.setText(QCoreApplication.translate("App", u"wine glass", None))
        self.checkBox_85.setText(QCoreApplication.translate("App", u"sink", None))
        self.checkBox_80.setText(QCoreApplication.translate("App", u"keyboard", None))
        self.checkBox_74.setText(QCoreApplication.translate("App", u"dining table", None))
        self.checkBox_22.setText(QCoreApplication.translate("App", u"traffic light", None))
        self.checkBox_55.setText(QCoreApplication.translate("App", u"cup", None))
        self.checkBox_64.setText(QCoreApplication.translate("App", u"broccoli", None))
        self.checkBox_68.setText(QCoreApplication.translate("App", u"donut", None))
        self.checkBox_31.setText(QCoreApplication.translate("App", u"horse", None))
        self.checkBox_39.setText(QCoreApplication.translate("App", u"umbrella", None))
        self.checkBox_61.setText(QCoreApplication.translate("App", u"apple", None))
        self.checkBox_59.setText(QCoreApplication.translate("App", u"bowl", None))
        self.checkBox_23.setText(QCoreApplication.translate("App", u"stop sign", None))
        self.checkBox_33.setText(QCoreApplication.translate("App", u"cow", None))
        self.checkBox_58.setText(QCoreApplication.translate("App", u"spoon", None))
        self.checkBox_47.setText(QCoreApplication.translate("App", u"kite", None))
        self.checkBox_81.setText(QCoreApplication.translate("App", u"cell phone", None))
        self.checkBox_60.setText(QCoreApplication.translate("App", u"banana", None))
        self.checkBox_45.setText(QCoreApplication.translate("App", u"snowboard", None))
        self.checkBox_73.setText(QCoreApplication.translate("App", u"bed", None))
        self.checkBox_40.setText(QCoreApplication.translate("App", u"handbag", None))
        self.checkBox_72.setText(QCoreApplication.translate("App", u"potted plant", None))
        self.checkBox_50.setText(QCoreApplication.translate("App", u"skateboard", None))
        self.checkBox_20.setText(QCoreApplication.translate("App", u"airplane", None))
        self.checkBox_29.setText(QCoreApplication.translate("App", u"bird", None))
        self.checkBox_42.setText(QCoreApplication.translate("App", u"frisbee", None))
        self.checkBox_65.setText(QCoreApplication.translate("App", u"carrot", None))
        self.checkBox_18.setText(QCoreApplication.translate("App", u"car", None))
        self.checkBox_43.setText(QCoreApplication.translate("App", u"suitcase", None))
        self.checkBox_71.setText(QCoreApplication.translate("App", u"chair", None))
        self.checkBox_38.setText(QCoreApplication.translate("App", u"backpack", None))
        self.checkBox_16.setText(QCoreApplication.translate("App", u"bicycle", None))
        self.checkBox_15.setText(QCoreApplication.translate("App", u"truck", None))
        self.checkBox_17.setText(QCoreApplication.translate("App", u"boat", None))
        self.checkBox_90.setText(QCoreApplication.translate("App", u"scissors", None))
        self.checkBox_66.setText(QCoreApplication.translate("App", u"hot dog", None))
        self.checkBox_62.setText(QCoreApplication.translate("App", u"sandwich", None))
        self.checkBox_37.setText(QCoreApplication.translate("App", u"giraffe", None))
        self.checkBox_19.setText(QCoreApplication.translate("App", u"motorcycle", None))
        self.checkBox_91.setText(QCoreApplication.translate("App", u"hair drier", None))
        self.checkBox_92.setText(QCoreApplication.translate("App", u"teddy bear", None))
        self.checkBox_93.setText(QCoreApplication.translate("App", u"toothbrush", None))
        self.pushButton.setText(QCoreApplication.translate("App", u"Save", None))
        self.SettingTab.setTabText(self.SettingTab.indexOf(self.tab_2), QCoreApplication.translate("App", u"Setting", None))
    # retranslateUi

