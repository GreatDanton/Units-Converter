# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'converter_gui.ui'
#
# Created: Sun Sep 20 15:03:39 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class Ui_Widget(QWidget):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.setEnabled(True)
        Widget.resize(445, 510)
        Widget.setBaseSize(QtCore.QSize(0, 0))
        Widget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.combo_units = QtWidgets.QComboBox(Widget)
        self.combo_units.setGeometry(QtCore.QRect(120, 50, 190, 27))
        self.combo_units.setObjectName("combo_units")
        self.combo_units.addItem("")
        self.combo_units.addItem("")
        self.combo_units.addItem("")
        self.combo_units.addItem("")
        self.combo_units.addItem("")
        self.combo_units.addItem("")
        self.combo_units.addItem("")
        self.button_swap = QtWidgets.QPushButton(Widget)
        self.button_swap.setGeometry(QtCore.QRect(190, 180, 87, 27))
        self.button_swap.setObjectName("button_swap")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 120, 401, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.textfield_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.textfield_input.setInputMethodHints(QtCore.Qt.ImhNone)
        self.textfield_input.setObjectName("textfield_input")
        self.horizontalLayout.addWidget(self.textfield_input)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.textfield_output = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.textfield_output.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textfield_output.setReadOnly(True)
        self.textfield_output.setObjectName("textfield_output")
        self.horizontalLayout.addWidget(self.textfield_output)
        self.currency_combobox = QtWidgets.QComboBox(Widget)
        self.currency_combobox.setGeometry(QtCore.QRect(120, 290, 190, 27))
        self.currency_combobox.setObjectName("currency_combobox")
        self.currency_combobox.addItem("")
        self.currency_combobox.addItem("")
        self.currency_combobox.addItem("")
        self.currency_combobox.addItem("")
        self.currency_combobox.addItem("")
        self.currency_combobox.addItem("")
        self.currency_combobox.addItem("")
        self.line = QtWidgets.QFrame(Widget)
        self.line.setGeometry(QtCore.QRect(-50, 230, 511, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Widget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 360, 401, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.currency_label_from = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.currency_label_from.setObjectName("currency_label_from")
        self.horizontalLayout_2.addWidget(self.currency_label_from)
        self.currency_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.currency_input.setObjectName("currency_input")
        self.horizontalLayout_2.addWidget(self.currency_input)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.currency_label_to = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.currency_label_to.setObjectName("currency_label_to")
        self.horizontalLayout_2.addWidget(self.currency_label_to)
        self.currency_output = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.currency_output.setFocusPolicy(QtCore.Qt.NoFocus)
        self.currency_output.setReadOnly(True)
        self.currency_output.setObjectName("currency_output")
        self.horizontalLayout_2.addWidget(self.currency_output)
        self.currencybutton_swap = QtWidgets.QPushButton(Widget)
        self.currencybutton_swap.setGeometry(QtCore.QRect(190, 430, 87, 27))
        self.currencybutton_swap.setObjectName("currencybutton_swap")
        self.label_5 = QtWidgets.QLabel(Widget)
        self.label_5.setGeometry(QtCore.QRect(180, 260, 61, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Widget)
        self.label_6.setGeometry(QtCore.QRect(200, 20, 41, 17))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        Widget.setWhatsThis(_translate("Widget", "<html><head/><body><p><br/></p></body></html>"))
        self.combo_units.setItemText(0, _translate("Widget", "---select---"))
        self.combo_units.setItemText(1, _translate("Widget", "inches / cm"))
        self.combo_units.setItemText(2, _translate("Widget", "miles / km"))
        self.combo_units.setItemText(3, _translate("Widget", "lb / kg"))
        self.combo_units.setItemText(4, _translate("Widget", "gallons / liters"))
        self.combo_units.setItemText(5, _translate("Widget", "oz / ml"))
        self.combo_units.setItemText(6, _translate("Widget", "F / ℃ ")) 
        self.button_swap.setText(_translate("Widget", "Swap"))
        self.label.setText(_translate("Widget", "From"))
        self.label_2.setText(_translate("Widget", "To"))
        self.currency_combobox.setItemText(0, _translate("Widget", "---select---"))
        self.currency_combobox.setItemText(1, _translate("Widget", "dollar / eur"))
        self.currency_combobox.setItemText(2, _translate("Widget", "swiss franc / eur"))
        self.currency_combobox.setItemText(3, _translate("Widget", "croatian kuna / eur"))
        self.currency_combobox.setItemText(4, _translate("Widget", "brittish pound / eur"))
        self.currency_combobox.setItemText(5, _translate("Widget", "japanese yen / eur"))
        self.currency_combobox.setItemText(6, _translate("Widget", "bitcoin / eur"))
        self.currency_label_from.setText(_translate("Widget", "From"))
        self.currency_label_to.setText(_translate("Widget", "To"))
        self.currencybutton_swap.setText(_translate("Widget", "Swap"))
        self.label_5.setText(_translate("Widget", "Currency:"))
        self.label_6.setText(_translate("Widget", "Units:"))

