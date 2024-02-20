# This Python file uses the following encoding: utf-8
import sys
import random
from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_anaSayfa

secenek=["YAZI","TURA"]
pcPuan = 0
myPuan = 0
pc = random.randint(0,1)

class anaSayfa(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_anaSayfa()
        self.ui.setupUi(self)

        self.ui.yazi.clicked.connect(self.kontrol)
        self.ui.tura.clicked.connect(self.kontrol)

    def kontrol(self):
        global pcPuan,myPuan,pc
        if (self.ui.yazi.isChecked()):
            secim= 0
        elif (self.ui.tura.isChecked()):
            secim = 1
        if (((pc==0) and (secim==1)) or ((pc==1) and (secim==0))):
            self.ui.label_2.setText("DURUM : KAZANDINIZ")
            myPuan= myPuan+1
        if (pc==secim):
            self.ui.label_2.setText("DURUM : KAYBETTİNİZ")
            pcPuan = pcPuan+1
        else:
            pass
        self.ui.label_1.setText("PC SEÇİMİ: "+secenek[pc])
        self.ui.label_4.setText("BİZİM SEÇİMİMİZ: "+secenek[secim])
        self.ui.label_3.setText("SİZ: "+str(myPuan)+"   BİLGİSAYAR: "+str(pcPuan))
        pc = random.randint(0,1)

        self.ui.yazi.setCheckable(False)
        self.ui.tura.setCheckable(False)

        self.ui.yazi.setCheckable(True)
        self.ui.tura.setCheckable(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = anaSayfa()
    widget.show()
    sys.exit(app.exec())
