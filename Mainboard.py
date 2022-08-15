import sys
from PySide6.QtCore import Qt, QSize, QPoint
from PySide6.QtGui import QScreen, QShortcut, QKeySequence
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,

)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Control Display Board 1")

        layout = QHBoxLayout()
        layout_a_b = QVBoxLayout()
        layout_a_b.setSpacing(0)
        layout_seg_c = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout_a_b.setContentsMargins(0, 0, 0, 0)
        layout_a_b.setSpacing(0)

        a_block = CellBlocks("A BLOCK")
        b_block = CellBlocks("B BLOCK")
        c_block = CellBlocks("C BLOCK")
        d_block = CellBlocks("D BLOCK")
        seg_block = CellBlocks("SEG/CRISIS/HOLDING")

        layout_a_b.addWidget(a_block)
        for i in range(6):
            i = Cells()
            layout_a_b.addWidget(i)
        layout_a_b.addWidget(b_block)
        for i in range(6):
            i = Cells()
            layout_a_b.addWidget(i)

        layout_seg_c.addWidget(seg_block)
        layout_seg_c.addWidget(c_block)

        layout.addLayout(layout_a_b)
        layout.addLayout(layout_seg_c)
        layout.addWidget(d_block)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


class SecondaryWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Control Display Board 2")
        layout = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        layout.setContentsMargins(7, 7, 7, 7)
        layout.setSpacing(7)

        e_block = CellBlocks("E BLOCK")
        f_block = CellBlocks("F BLOCK")
        mod_block = CellBlocks("MOD UNIT")
        superiorior_PI = CellBlocks("superiorIOR COURT PI LIST")
        dist_pi = CellBlocks("DISTRICT COURT PI LIST")
        transports = CellBlocks("TRANSPORTS")
        date_time = CellBlocks("DATE TIME")
        count = CellBlocks("COUNT")

        layout3.addWidget(superiorior_PI)
        layout3.addWidget(dist_pi)

        layout4.addWidget(date_time)
        layout4.addWidget(count)

        layout2.addWidget(e_block)
        layout2.addLayout(layout3)
        layout2.addWidget(transports)
        layout2.addLayout(layout4)

        layout.addWidget(f_block)
        layout.addWidget(mod_block)
        layout.addLayout(layout2)

        self.setLayout(layout)


class CellBlocks(QLabel):
    def __init__(self, blockname):
        super().__init__()

        self.setText(blockname)
        self.setStyleSheet("background-color: black;color: white")


class Cells(QWidget):
    def __init__(
        self,
        cellname="A1U",
        inmate_name="test inmate",
        pi="PI",
        dist_bond="test",
        dist_cash="test",
        superior_bond="test",
        superior_cash="test",
        release_date="06/23/22",
        alert1="test",
        alert2="test",
        alert3="test",
        note="this is a test note",
    ):
        super().__init__()

        layout = QHBoxLayout()  # cell frame layout to include cell number, and inmate name
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout2 = QVBoxLayout()  # cell data frame within layout to include notes
        layout3 = QHBoxLayout()  # cell data frame within layout2 to include release date
        # cell data frame within layout3 to include pi, Dist and superior labels
        layout4 = QVBoxLayout()
        # cell data frame within layout3 to include bond, distbond, superiorbond
        layout5 = QVBoxLayout()
        # cell data frame within layout3 to include cash, distcash, superiorcash
        layout6 = QVBoxLayout()
        layout7 = QVBoxLayout()  # cell data frame within layout3 to include alert labels x3

        # font-weight: bold;"
        cell_name_style = '''background-color: black;
                                  color: white;
                                  border: 1px solid rgb(140, 140, 140);
                                  font: bold 8pt "Arial";
                                  '''
        inmate_name_style = '''background-color: black;
                                  color: white;
                                  border: 1px solid rgb(140, 140, 140);
                                  font: bold 18pt "Arial";
                                  '''

        self.cellname = QLabel(cellname)
        self.cellname.setFixedSize(28, 60)
        self.cellname.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.cellname.setStyleSheet(cell_name_style)

        self.inmate_name = QLabel(inmate_name)
        self.inmate_name.setFixedSize(286, 60)
        self.inmate_name.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.inmate_name.setStyleSheet(inmate_name_style)

        self.pi = QLabel(pi)
        self.pi.setFixedSize(20, 15)
        self.pi.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.pi.setStyleSheet(cell_name_style)

        self.dist = QLabel("D")
        self.dist.setFixedSize(20, 15)
        self.dist.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.dist.setStyleSheet(cell_name_style)

        self.superior = QLabel("S")
        self.superior.setFixedSize(20, 15)
        self.superior.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.superior.setStyleSheet(cell_name_style)

        self.bond = QLabel("Bond")
        self.bond.setFixedSize(64, 15)
        self.bond.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.bond.setStyleSheet(cell_name_style)

        self.cash = QLabel("Cash")
        self.cash.setFixedSize(64, 15)
        self.cash.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.cash.setStyleSheet(cell_name_style)

        self.dist_bond = QLabel(dist_bond)
        self.dist_bond.setFixedSize(64, 15)
        self.dist_bond.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.dist_bond.setStyleSheet(cell_name_style)

        self.dist_cash = QLabel(dist_cash)
        self.dist_cash.setFixedSize(64, 15)
        self.dist_cash.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.dist_cash.setStyleSheet(cell_name_style)

        self.superior_bond = QLabel(superior_bond)
        self.superior_bond.setFixedSize(64, 15)
        self.superior_bond.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.superior_bond.setStyleSheet(cell_name_style)

        self.superior_cash = QLabel(superior_cash)
        self.superior_cash.setFixedSize(64, 15)
        self.superior_cash.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.superior_cash.setStyleSheet(cell_name_style)

        self.release_date = QLabel(release_date)
        self.release_date.setFixedSize(100, 45)
        self.release_date.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.release_date.setStyleSheet(inmate_name_style)

        self.alert1 = QLabel(alert1)
        self.alert1.setFixedSize(64, 15)
        self.alert1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.alert1.setStyleSheet(cell_name_style)

        self.alert2 = QLabel(alert2)
        self.alert2.setFixedSize(64, 15)
        self.alert2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.alert2.setStyleSheet(cell_name_style)

        self.alert3 = QLabel(alert3)
        self.alert3.setFixedSize(64, 15)
        self.alert3.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.alert3.setStyleSheet(cell_name_style)

        self.note = QLabel(note)
        self.note.setFixedSize(312, 15)
        self.note.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.note.setStyleSheet(cell_name_style)

        layout.addWidget(self.cellname)
        layout.addWidget(self.inmate_name)
        layout.addLayout(layout2)
        layout.setSpacing(0)

        layout2.addLayout(layout3)
        layout2.addWidget(self.note)
        layout2.setSpacing(0)

        layout3.addLayout(layout4)
        layout3.addLayout(layout5)
        layout3.addLayout(layout6)
        layout3.addWidget(self.release_date)
        layout3.addLayout(layout7)
        layout3.setSpacing(0)

        layout4.addWidget(self.pi)
        layout4.addWidget(self.dist)
        layout4.addWidget(self.superior)
        layout4.setSpacing(0)

        layout5.addWidget(self.bond)
        layout5.addWidget(self.dist_bond)
        layout5.addWidget(self.superior_bond)
        layout5.setSpacing(0)

        layout6.addWidget(self.cash)
        layout6.addWidget(self.dist_cash)
        layout6.addWidget(self.superior_cash)
        layout6.setSpacing(0)

        layout7.addWidget(self.alert1)
        layout7.addWidget(self.alert2)
        layout7.addWidget(self.alert3)
        layout7.setSpacing(0)

        self.setLayout(layout)


class Inmate():
    pass


class Bail():
    pass


class Notes():
    pass


class ReleaseDate():
    pass


class Alerts():
    pass


app = QApplication(sys.argv)
app.setStyle("Fusion")

window = MainWindow()
window.showMaximized()

# window2 = SecondaryWindow()
# window2.show()

# window3 = CellBlocks('A Block')
# window3.show()

app.exec()
