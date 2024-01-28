from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGroupBox,
    QRadioButton,
    QPushButton,
    QLineEdit,
    QLabel)

def calc_hard_percent(summa_input, percent_input, years_input, layout):
    summa = int(summa_input.text())
    percent = int(percent_input.text())
    years = int(years_input.text())
    percent = percent/100+1
    for i in range(years):
        summa*=percent
    str_summa = str(summa)
    index_dot = str_summa.find(".")
    result = "В итоге сумма вклада составит:\n" + str_summa[0:index_dot+3]
    label = QLabel(result)
    label.setStyleSheet("font-size:18px;font-color:green;")
    layout.addWidget(label)


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

#
label_title = QLabel("Калькулятор вклада")
label_title.setStyleSheet("color:rgb(127,45,92);font-size:32px;")
layout.addWidget(label_title)

label_summa = QLabel("Введите сумму вклада:")
label_summa.setStyleSheet("color:red;font-size:18px;")
layout.addWidget(label_summa)

summa_input = QLineEdit()
summa_input.setStyleSheet("font-size:18px;font-weight:700;")
layout.addWidget(summa_input)

label_years = QLabel("Введите срок вклада в годах:")
label_years.setStyleSheet("color:orange;font-size:18px;")
layout.addWidget(label_years)

years_input = QLineEdit()
years_input.setStyleSheet("font-size:18px;font-weight:700;")
layout.addWidget(years_input)

label_percent = QLabel("Введите процент вклада:")
label_percent.setStyleSheet("color:blue;font-size:18px;")
layout.addWidget(label_percent)

percent_input = QLineEdit()
percent_input.setStyleSheet("font-size:18px;font-weight:700;")
layout.addWidget(percent_input)

btn_submit = QPushButton("Посчитать")
btn_submit.setStyleSheet("color:green;font-size:18px;")
btn_submit.clicked.connect(lambda: calc_hard_percent(summa_input, percent_input, years_input, layout)) ##############
layout.addWidget(btn_submit)
#

window.setLayout(layout)
window.show()
app.exec_()
