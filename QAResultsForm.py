# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QAResultsForm.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(887, 1040)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/book_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_9 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.lineEdit_PatName = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_PatName.setObjectName("lineEdit_PatName")
        self.horizontalLayout_6.addWidget(self.lineEdit_PatName)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.lineEdit_DOB = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_DOB.setObjectName("lineEdit_DOB")
        self.horizontalLayout_7.addWidget(self.lineEdit_DOB)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.lineEdit_PatID = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_PatID.setObjectName("lineEdit_PatID")
        self.horizontalLayout_8.addWidget(self.lineEdit_PatID)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        self.gridLayout_3.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ComboBox_RadCalcResults = QtWidgets.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ComboBox_RadCalcResults.setFont(font)
        self.ComboBox_RadCalcResults.setMinimum(-5.0)
        self.ComboBox_RadCalcResults.setMaximum(5.0)
        self.ComboBox_RadCalcResults.setSingleStep(0.1)
        self.ComboBox_RadCalcResults.setObjectName("ComboBox_RadCalcResults")
        self.verticalLayout_2.addWidget(self.ComboBox_RadCalcResults)
        self.ComboBox_RadCalcTol = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ComboBox_RadCalcTol.setFont(font)
        self.ComboBox_RadCalcTol.setStyleSheet("")
        self.ComboBox_RadCalcTol.setObjectName("ComboBox_RadCalcTol")
        self.ComboBox_RadCalcTol.addItem("")
        self.ComboBox_RadCalcTol.setItemText(0, "")
        self.ComboBox_RadCalcTol.addItem("")
        self.ComboBox_RadCalcTol.addItem("")
        self.verticalLayout_2.addWidget(self.ComboBox_RadCalcTol)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_17.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ComboBox_LA = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ComboBox_LA.setFont(font)
        self.ComboBox_LA.setObjectName("ComboBox_LA")
        self.ComboBox_LA.addItem("")
        self.ComboBox_LA.addItem("")
        self.ComboBox_LA.addItem("")
        self.horizontalLayout_2.addWidget(self.ComboBox_LA)
        spacerItem = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.lineEdit_PlanName = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_PlanName.setObjectName("lineEdit_PlanName")
        self.verticalLayout_4.addWidget(self.lineEdit_PlanName)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.dateEdit_CurDate = QtWidgets.QDateEdit(self.groupBox_2)
        self.dateEdit_CurDate.setCalendarPopup(True)
        self.dateEdit_CurDate.setDate(QtCore.QDate(2017, 8, 4))
        self.dateEdit_CurDate.setObjectName("dateEdit_CurDate")
        self.verticalLayout_6.addWidget(self.dateEdit_CurDate)
        self.lineEdit_Trial = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Trial.setObjectName("lineEdit_Trial")
        self.verticalLayout_6.addWidget(self.lineEdit_Trial)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_3)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setFrameShape(QtWidgets.QFrame.Box)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.ComboBox_Site = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ComboBox_Site.setFont(font)
        self.ComboBox_Site.setObjectName("ComboBox_Site")
        self.ComboBox_Site.addItem("")
        self.ComboBox_Site.addItem("")
        self.ComboBox_Site.addItem("")
        self.ComboBox_Site.addItem("")
        self.ComboBox_Site.addItem("")
        self.ComboBox_Site.addItem("")
        self.ComboBox_Site.addItem("")
        self.ComboBox_Site.addItem("")
        self.horizontalLayout_4.addWidget(self.ComboBox_Site)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setFrameShape(QtWidgets.QFrame.Box)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.ComboBox_Technique = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ComboBox_Technique.setFont(font)
        self.ComboBox_Technique.setObjectName("ComboBox_Technique")
        self.ComboBox_Technique.addItem("")
        self.ComboBox_Technique.addItem("")
        self.horizontalLayout_5.addWidget(self.ComboBox_Technique)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_16.addLayout(self.verticalLayout_9)
        self.gridLayout_2.addLayout(self.horizontalLayout_16, 0, 0, 1, 1)
        self.horizontalLayout_17.addWidget(self.groupBox_2)
        self.gridLayout_8.addLayout(self.horizontalLayout_17, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.gridLayout_4.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButtonOK = QtWidgets.QPushButton(self.groupBox_6)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonOK.setIcon(icon1)
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.gridLayout_7.addWidget(self.pushButtonOK, 1, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButtonDeliveryDone = QtWidgets.QPushButton(self.groupBox_6)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons/burn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDeliveryDone.setIcon(icon2)
        self.pushButtonDeliveryDone.setObjectName("pushButtonDeliveryDone")
        self.gridLayout_6.addWidget(self.pushButtonDeliveryDone, 0, 1, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_13 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setFrameShape(QtWidgets.QFrame.Box)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_13.addWidget(self.label_13)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.comboBox_MeasuredBy = QtWidgets.QComboBox(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_MeasuredBy.setFont(font)
        self.comboBox_MeasuredBy.setEditable(True)
        self.comboBox_MeasuredBy.setObjectName("comboBox_MeasuredBy")
        self.comboBox_MeasuredBy.addItem("")
        self.comboBox_MeasuredBy.addItem("")
        self.comboBox_MeasuredBy.addItem("")
        self.comboBox_MeasuredBy.addItem("")
        self.comboBox_MeasuredBy.addItem("")
        self.comboBox_MeasuredBy.addItem("")
        self.comboBox_MeasuredBy.addItem("")
        self.comboBox_MeasuredBy.addItem("")
        self.comboBox_MeasuredBy.addItem("")
        self.comboBox_MeasuredBy.addItem("")
        self.horizontalLayout_13.addWidget(self.comboBox_MeasuredBy)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_13)
        self.dateTimeEdit_ApprovedBy = QtWidgets.QDateTimeEdit(self.groupBox_6)
        self.dateTimeEdit_ApprovedBy.setEnabled(False)
        self.dateTimeEdit_ApprovedBy.setObjectName("dateTimeEdit_ApprovedBy")
        self.horizontalLayout_15.addWidget(self.dateTimeEdit_ApprovedBy)
        self.verticalLayout_7.addLayout(self.horizontalLayout_15)
        self.gridLayout_6.addLayout(self.verticalLayout_7, 3, 1, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setFrameShape(QtWidgets.QFrame.Box)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.ComboBox_OKToStart = QtWidgets.QComboBox(self.groupBox_6)
        self.ComboBox_OKToStart.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ComboBox_OKToStart.setFont(font)
        self.ComboBox_OKToStart.setObjectName("ComboBox_OKToStart")
        self.ComboBox_OKToStart.addItem("")
        self.ComboBox_OKToStart.setItemText(0, "")
        self.ComboBox_OKToStart.addItem("")
        self.ComboBox_OKToStart.addItem("")
        self.horizontalLayout_11.addWidget(self.ComboBox_OKToStart)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setReadOnly(False)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_5.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.groupBox_5)
        self.gridLayout_6.addLayout(self.verticalLayout_8, 2, 0, 2, 1)
        self.textEditInfo = QtWidgets.QTextEdit(self.groupBox_6)
        self.textEditInfo.setObjectName("textEditInfo")
        self.gridLayout_6.addWidget(self.textEditInfo, 1, 1, 2, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_6, 3, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.comboBox_MeasuredBy.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Results"))
        self.groupBox_4.setTitle(_translate("Dialog", "Patient Details"))
        self.label_7.setText(_translate("Dialog", "Pat Name"))
        self.label_8.setText(_translate("Dialog", "DOB"))
        self.label_9.setText(_translate("Dialog", "Pat ID"))
        self.groupBox.setTitle(_translate("Dialog", "RadCalc Results"))
        self.label.setText(_translate("Dialog", "RadCalc Results"))
        self.label_2.setText(_translate("Dialog", "Within Tolerance"))
        self.ComboBox_RadCalcTol.setItemText(1, _translate("Dialog", "Yes"))
        self.ComboBox_RadCalcTol.setItemText(2, _translate("Dialog", "No"))
        self.groupBox_2.setTitle(_translate("Dialog", "Plan Details"))
        self.label_3.setText(_translate("Dialog", "Linac"))
        self.label_4.setText(_translate("Dialog", "Plan Name"))
        self.ComboBox_LA.setItemText(0, _translate("Dialog", "LA1"))
        self.ComboBox_LA.setItemText(1, _translate("Dialog", "LA3"))
        self.ComboBox_LA.setItemText(2, _translate("Dialog", "LA4"))
        self.label_5.setText(_translate("Dialog", "Date"))
        self.label_6.setText(_translate("Dialog", "Trial"))
        self.label_14.setText(_translate("Dialog", "Site"))
        self.ComboBox_Site.setItemText(0, _translate("Dialog", "Brain"))
        self.ComboBox_Site.setItemText(1, _translate("Dialog", "H&N"))
        self.ComboBox_Site.setItemText(2, _translate("Dialog", "Breast"))
        self.ComboBox_Site.setItemText(3, _translate("Dialog", "Lung"))
        self.ComboBox_Site.setItemText(4, _translate("Dialog", "Thorax"))
        self.ComboBox_Site.setItemText(5, _translate("Dialog", "Prostate"))
        self.ComboBox_Site.setItemText(6, _translate("Dialog", "Pelvis"))
        self.ComboBox_Site.setItemText(7, _translate("Dialog", "Other"))
        self.label_15.setText(_translate("Dialog", "Technique"))
        self.ComboBox_Technique.setItemText(0, _translate("Dialog", "IMRT "))
        self.ComboBox_Technique.setItemText(1, _translate("Dialog", "VMAT"))
        self.groupBox_3.setTitle(_translate("Dialog", "Field Details"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Field No."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Field Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Gantry Angle"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Plan MU"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Delivered MU"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "MUs Match"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Dose Diff (3%)"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Comments"))
        self.groupBox_6.setTitle(_translate("Dialog", "Results"))
        self.pushButtonOK.setText(_translate("Dialog", "Generate Report"))
        self.pushButtonDeliveryDone.setText(_translate("Dialog", "Delivery done!"))
        self.label_13.setText(_translate("Dialog", "Measured By:"))
        self.comboBox_MeasuredBy.setItemText(0, _translate("Dialog", "Ben Cooper"))
        self.comboBox_MeasuredBy.setItemText(1, _translate("Dialog", "Deepak Basuala"))
        self.comboBox_MeasuredBy.setItemText(2, _translate("Dialog", "Helen Gustafsson"))
        self.comboBox_MeasuredBy.setItemText(3, _translate("Dialog", "Jothy Selvaraj"))
        self.comboBox_MeasuredBy.setItemText(4, _translate("Dialog", "Jon Lee"))
        self.comboBox_MeasuredBy.setItemText(5, _translate("Dialog", "Mounir Ibrahim"))
        self.comboBox_MeasuredBy.setItemText(6, _translate("Dialog", "Nigel Freeman"))
        self.comboBox_MeasuredBy.setItemText(7, _translate("Dialog", "Ravi Thura"))
        self.comboBox_MeasuredBy.setItemText(8, _translate("Dialog", "Talat Mahmood"))
        self.comboBox_MeasuredBy.setItemText(9, _translate("Dialog", "Other"))
        self.label_11.setText(_translate("Dialog", "OK to start treatment"))
        self.ComboBox_OKToStart.setItemText(1, _translate("Dialog", "Yes"))
        self.ComboBox_OKToStart.setItemText(2, _translate("Dialog", "No"))
        self.groupBox_5.setTitle(_translate("Dialog", "Notes"))
