#!/usr/bin/env python3

import sys
import urllib.request
import os
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QMainWindow, QDesktopWidget, QComboBox
from converter_gui import Ui_Widget
import config


class Main(QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Widget(self)
        self.ui.setupUi(self)
        self.center()
        self.setWindowTitle('Unit Converter')
        self.show()

        # on click swap ratios
        swap_button = self.ui.button_swap
        swap_button.setCheckable(True)
        swap_button.clicked.connect(self.clear_textfields)
        # units part
        self.ui.textfield_input.textChanged.connect(self.on_text_change)
        self.ui.combo_units.activated[str].connect(self.combo_changed)
        # currency part
        self.ui.currency_input.textChanged.connect(self.on_text_change_currency)
        self.ui.currency_combobox.activated[str].connect(self.combo_currency_changed)
        self.ui.currencybutton_swap.setCheckable(True)
        self.ui.currencybutton_swap.clicked.connect(self.clear_textfields_currency)

    # on text_field_input text changes
    def on_text_change(self):
        num_input = self.ui.textfield_input.text()
        swap_button = self.ui.button_swap
        combo_units = self.ui.combo_units
        ratios = {1: 2.54, 2: 1.609344, 3: 0.45359237, 4: 3.78541178, 5: 29.5735296, 6: 1 }
        index = combo_units.currentIndex()
        if swap_button.isChecked():

            if len(self.ui.textfield_input.text()) == 0:
                self.ui.textfield_output.clear()
                return
            else:
                ratio = ratios[index]
# converting celsius to fahrenheit
                if index == 6:
                    output = (float(num_input) * 9 / 5) + 32
                    output = '%.2f' % output
                    self.ui.textfield_output.setText(output)
# for all other conversions
                else:
                    output = float(num_input) / ratio
                    output = '%.2f' % output
                    self.ui.textfield_output.setText(output)
        else:

            if len(self.ui.textfield_input.text()) == 0:
                self.ui.textfield_output.clear()
                return
            else:
                ratio = ratios[index]
# index 6 = code for fahrenheit to celsius
                if index == 6:
                    output = (float(num_input)-32) * 5 / 9
                    output = '%.2f' % output
                    self.ui.textfield_output.setText(output)
# for all other conversions
                else:
                    output = float(num_input) * ratio
                    output = '%.2f' % output
                    self.ui.textfield_output.setText(output)

    def clear_textfields(self):
        self.ui.textfield_input.clear()
        self.ui.textfield_output.clear()
        label_from = self.ui.label
        label_to = self.ui.label_2
        # switch labels on swap button pressed
        change = label_from.text()
        label_from.setText(label_to.text())
        label_to.setText(change)

    def combo_changed(self):
        combo_units = self.ui.combo_units
        label_from = self.ui.label
        label_to = self.ui.label_2
        swap_button = self.ui.button_swap
        # clears textfields upon switching in combobox.
        self.ui.textfield_input.clear()
        self.ui.textfield_output.clear()
        # if swap_button is checked return it to unchecked
        if swap_button.isChecked():
            swap_button.setChecked(False)

        # get index of combobox selected item:
        index = combo_units.currentIndex()
        sentence = combo_units.itemText(index)
        # find position of slash from combobox
        position_of_slash = sentence.find('/')

        # change labels to the words in combobox
        if index > 0:
            label_from.setText(sentence[:position_of_slash])
            label_to.setText(sentence[position_of_slash+2:])
        else:
            label_from.setText('From')
            label_to.setText('To')

    def combo_currency_changed(self):
            combo_units = self.ui.currency_combobox
            label_from = self.ui.currency_label_from
            label_to = self.ui.currency_label_to
            swap_button = self.ui.currencybutton_swap

            # clears textfields upon switching in combobox.
            self.ui.currency_input.clear()
            self.ui.currency_output.clear()
            # if swap_button is checked return it to unchecked
            if swap_button.isChecked():
                swap_button.setChecked(False)

            # get index + text of combobox selected item:
            index = combo_units.currentIndex()
            sentence = combo_units.itemText(index)
            # find position of slash in combobox
            position_of_slash = sentence.find('/')

            # money ratios:
            ratios = {1: ['USD', 'EUR'], 2: ['CHF', 'EUR'], 3: ['HRK', 'EUR'], 4: ['GBP', 'EUR'],
                      5: ['JPY', 'EUR'], 6: ['BTC', 'EUR']}

            if index == 0:
                label_from.setText('From')
                label_to.setText('To')
                return
            else:
                try:
                    connection = urllib.request.urlopen("https://www.google.com/finance/converter?a=1&from="+ratios[index][0]+"&to="+ratios[index][1], timeout = 0.5)

                    ratio_text = str(connection.read())
                    connection.close()
                    # print(ratio_text)
                    characters_number = ratio_text.find("class=bld")
                    ratio = float(ratio_text[characters_number+10: characters_number+16])
                    print(ratio)
                    config.currency_ratios[index] = ratio
                    print("Internet on")
                    
                    input_file = open('currency_ratios', 'r')
                    output_text = input_file.read()
                    input_file.close()
                    # finds the position of the correct ratio number
                    position_of_number = output_text.find(str(index)+':')
                    # print(output_text[position_of_number+2:position_of_number+9])
                    new_ratio = ratio
                    final_output_text = output_text[:position_of_number+3] + str(new_ratio) + ','  \
                            + output_text[position_of_number+10:]
                    
                    output_file = open('currency_ratios', 'w')
                    output_file.write(final_output_text)
                    print(final_output_text)
                    output_file.close()

                # if internet is not working read numbers from txt file 
                except urllib.request.URLError:
                    print("Internet off")
                    input_file = open('currency_ratios', 'r')
                    input_file_text = input_file.read()
                    input_file.close()

                    position = input_file_text.find(str(index)+':')
                    new_ratio = float(input_file_text[position+3: position+9])
                    config.currency_ratios[index] = new_ratio
                    print(config.currency_ratios)

                # set correct label text
                label_from.setText(sentence[:position_of_slash])
                label_to.setText(sentence[position_of_slash+2:])

    def on_text_change_currency(self):
        num_input = self.ui.currency_input.text()
        swap_button = self.ui.currencybutton_swap
        combo_units = self.ui.currency_combobox
        ratio = config.currency_ratios
        index = combo_units.currentIndex()

        if swap_button.isChecked():

            if len(self.ui.currency_input.text()) == 0:
                self.ui.currency_output.clear()
                return
            else:
                output = float(num_input) / ratio[index]
                output = '%.4f' % output
                self.ui.currency_output.setText(output)
        else:

            if len(self.ui.currency_input.text()) == 0:
                self.ui.currency_output.clear()
                return
            else:
                output = float(num_input) * ratio[index]
                output = '%.4f' % output
                self.ui.currency_output.setText(output)

    def clear_textfields_currency(self):
        self.ui.currency_input.clear()
        self.ui.currency_output.clear()
        label_from = self.ui.currency_label_from
        label_to = self.ui.currency_label_to

        change = label_from.text()
        label_from.setText(label_to.text())
        label_to.setText(change)

    # used to move window to the centre of the screen
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
