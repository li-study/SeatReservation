
import math
from PyQt5.QtWidgets import QWidget, QGridLayout,QPushButton


class seatUI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        # self.move(300, 150)
        self.setWindowTitle('座位示意图')

    def initSeat(self,seatState):
        names = []
        seatnum = len(seatState)
        for num in range(seatnum):
            names.append(str(num))
        colnum = int(math.ceil(math.sqrt(seatnum / 2)))
        rownum = 2 * colnum
        # print(rownum, colnum)

        positions = [(i, j) for i in range(rownum) for j in range(colnum)]

        count = 0
        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)

            if seatState[count] :
                button.setStyleSheet("background-color: red")
            else:
                button.setStyleSheet("background-color: green")
            self.grid.addWidget(button, *position)
            count = count + 1

    def open(self):
        self.show()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     ex.open()
#     sys.exit(app.exec_())