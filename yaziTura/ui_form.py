# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QRadioButton, QSizePolicy, QWidget)

class Ui_anaSayfa(object):
    def setupUi(self, anaSayfa):
        if not anaSayfa.objectName():
            anaSayfa.setObjectName(u"anaSayfa")
        anaSayfa.resize(301, 236)
        self.horizontalLayout = QHBoxLayout(anaSayfa)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(anaSayfa)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 2)

        self.tura = QRadioButton(anaSayfa)
        self.tura.setObjectName(u"tura")

        self.gridLayout.addWidget(self.tura, 0, 1, 1, 1)

        self.yazi = QRadioButton(anaSayfa)
        self.yazi.setObjectName(u"yazi")

        self.gridLayout.addWidget(self.yazi, 0, 0, 1, 1)

        self.label_1 = QLabel(anaSayfa)
        self.label_1.setObjectName(u"label_1")

        self.gridLayout.addWidget(self.label_1, 1, 0, 1, 2)

        self.label_3 = QLabel(anaSayfa)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 2)

        self.label_4 = QLineEdit(anaSayfa)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 2)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(anaSayfa)

        QMetaObject.connectSlotsByName(anaSayfa)
    # setupUi

    def retranslateUi(self, anaSayfa):
        anaSayfa.setWindowTitle(QCoreApplication.translate("anaSayfa", u"anaSayfa", None))
        self.label_2.setText(QCoreApplication.translate("anaSayfa", u"DURUM : ", None))
        self.tura.setText(QCoreApplication.translate("anaSayfa", u"Tura", None))
        self.yazi.setText(QCoreApplication.translate("anaSayfa", u"Yaz\u0131", None))
        self.label_1.setText(QCoreApplication.translate("anaSayfa", u"PC SE\u00c7\u0130M\u0130", None))
        self.label_3.setText(QCoreApplication.translate("anaSayfa", u"S\u0130Z :              B\u0130LG\u0130SAYAR:", None))
        self.label_4.setText(QCoreApplication.translate("anaSayfa", u"B\u0130Z\u0130M SE\u00c7\u0130M\u0130M\u0130Z:", None))
    # retranslateUi

