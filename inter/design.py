# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_youtubedownload(object):
    def setupUi(self, youtubedownload):
        if not youtubedownload.objectName():
            youtubedownload.setObjectName(u"youtubedownload")
        youtubedownload.resize(602, 378)
        youtubedownload.setMinimumSize(QSize(602, 378))
        youtubedownload.setMaximumSize(QSize(602, 378))
        icon = QIcon()
        icon.addFile(u"../../../../Downloads/Youtube-Icon-square-2340x2340.png", QSize(), QIcon.Normal, QIcon.Off)
        youtubedownload.setWindowIcon(icon)
        youtubedownload.setStyleSheet(u"background-color: rgb(15, 15, 15);")
        self.link = QLineEdit(youtubedownload)
        self.link.setObjectName(u"link")
        self.link.setGeometry(QRect(110, 80, 461, 31))
        self.link.setStyleSheet(u"color: rgb(170, 170, 170);\n"
"border-radius: 10px;\n"
"border: 1px solid #717171;")
        self.label = QLabel(youtubedownload)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 80, 47, 31))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 12px;")
        self.label_2 = QLabel(youtubedownload)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 150, 131, 31))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 12px;")
        self.option = QComboBox(youtubedownload)
        self.option.setObjectName(u"option")
        self.option.setGeometry(QRect(180, 150, 391, 31))
        self.option.setCursor(QCursor(Qt.PointingHandCursor))
        self.option.setStyleSheet(u"color: rgb(170, 170, 170);\n"
"border-radius: 10px;\n"
"border: 1px solid #717171;")
        self.label_3 = QLabel(youtubedownload)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 220, 131, 31))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 12px;")
        self.folder_path = QPushButton(youtubedownload)
        self.folder_path.setObjectName(u"folder_path")
        self.folder_path.setGeometry(QRect(500, 220, 71, 31))
        self.folder_path.setCursor(QCursor(Qt.PointingHandCursor))
        self.folder_path.setStyleSheet(u"color: rgb(170, 170, 170);\n"
"border-radius: 10px;\n"
"border: 1px solid #717171;\n"
"")
        self.location = QLineEdit(youtubedownload)
        self.location.setObjectName(u"location")
        self.location.setEnabled(True)
        self.location.setGeometry(QRect(180, 220, 311, 31))
        self.location.setCursor(QCursor(Qt.ArrowCursor))
        self.location.setStyleSheet(u"color: rgb(170, 170, 170);\n"
"border-radius: 10px;\n"
"border: 1px solid #717171;")
        self.location.setReadOnly(True)
        self.btnDownload = QPushButton(youtubedownload)
        self.btnDownload.setObjectName(u"btnDownload")
        self.btnDownload.setGeometry(QRect(500, 290, 71, 31))
        self.btnDownload.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDownload.setStyleSheet(u"color: #2ba640;\n"
"border-radius: 10px;\n"
"border: 1px solid #2ba640;\n"
"")
        self.result = QLabel(youtubedownload)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(40, 280, 441, 41))
        self.result.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 18px;")
        self.titleTop = QLabel(youtubedownload)
        self.titleTop.setObjectName(u"titleTop")
        self.titleTop.setGeometry(QRect(220, 20, 161, 41))
        self.titleTop.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 18px;")
        self.label_4 = QLabel(youtubedownload)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 350, 371, 20))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.retranslateUi(youtubedownload)

        QMetaObject.connectSlotsByName(youtubedownload)
    # setupUi

    def retranslateUi(self, youtubedownload):
        youtubedownload.setWindowTitle(QCoreApplication.translate("youtubedownload", u"YouTube Download - @ofabioacarvalho", None))
        self.link.setPlaceholderText(QCoreApplication.translate("youtubedownload", u"Cole o link aqui. Por exemplo: https://www.youtube.com/watch?v=YWIhyOWxKPw&t=1090s", None))
        self.label.setText(QCoreApplication.translate("youtubedownload", u"<html><head/><body><p>Link:</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("youtubedownload", u"<html><head/><body><p>Selecione uma op\u00e7\u00e3o:</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("youtubedownload", u"<html><head/><body><p>Onde salvar o arquivo:</p></body></html>", None))
        self.folder_path.setText(QCoreApplication.translate("youtubedownload", u"Escolher", None))
        self.btnDownload.setText(QCoreApplication.translate("youtubedownload", u"Baixar", None))
        self.result.setText("")
        self.titleTop.setText(QCoreApplication.translate("youtubedownload", u"YouTube Download", None))
        self.label_4.setText(QCoreApplication.translate("youtubedownload", u"Developed by F\u00e1bio Carvalho - TikTok / Instagram: @ofabioacarvalho", None))
    # retranslateUi

