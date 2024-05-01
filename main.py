from PySide6.QtCore import QEvent, QObject
from pytube import YouTube
import os
import ssl
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QLineEdit, QPushButton, QMessageBox
from inter.design import Ui_youtubedownload
from PySide6.QtGui import QKeyEvent
from typing import cast
import time

class Setup(QMainWindow, Ui_youtubedownload):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.set_options()

        # Conectando os botões...
        self.folder_path.clicked.connect(self.select_folder_path)
        self.btnDownload.clicked.connect(self.download)

        # Capturando o evendo do click
        # self.btnDownload.installEventFilter(self)

    def validation_items(self):
        link = self.link.text()
        path = self.location.text()
        option = self.option.currentText()

        if not link or not path or not option:
            return False
        
        return True

    # def eventFilter(self, watched: QObject, event: QEvent) -> bool:
    #     if event.type() == QEvent.Type.MouseButtonPress:
    #         if event.type() == 2:
    #             self.download(self)

    #     return super().eventFilter(watched, event)

    def set_options(self):
        # "Audio mp3", "Audio mp3", "Video mp4"
        self.option.addItems(["Audio mp3", "Video mp4"])

    def select_folder_path(self):
        folder_path_target = QFileDialog.getExistingDirectory(self, "Selecione uma pasta", "/")
        # Atualizar o texto do QLineEdit com o caminho da pasta selecionada
        self.location.setText(folder_path_target)

    def show_message_log(self, msg, type=None):
        # Criar uma instância de QMessageBox
        message_box = QMessageBox()
        # Definir o ícone para indicar uma mensagem de sucesso (ícone de informação)
        if type == "error":
            message_box.setIcon(QMessageBox.Critical)
        else:
            message_box.setIcon(QMessageBox.Information)
        # Definir o texto da mensagem
        message_box.setText(msg)
        # Exibir o pop-up de mensagem
        message_box.exec()
        return

    def on_progress(self, stream, chunk, remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - remaining
        percentage = (bytes_downloaded / total_size) * 100
        self.result.setText(f"Porcentagem do download: {percentage:.2f}%")

    def download(self):
        link = self.link.text()
        path = self.location.text()
        option = self.option.currentText()

        if not link or not path or not option:
            self.show_message_log("Por favor adicione um link do youtube", "info")
        elif not path:
            self.show_message_log("Por favor selecione uma pasta para salvar o arquivo", "info")
        elif not option:
            self.show_message_log("Por favor selecione um tipo para download", "info")
        
        if self.validation_items():
            # Inicio do download
            try:
                yt = YouTube(link)
                self.result.setText("Download iniciado, aguarde...")
                self.btnDownload.setText("Carregando...")
                self.btnDownload.setEnabled(False)
                time.sleep(2)
                self.show_message_log("Download iniciado, aguarde...")
                if option == "Audio mp3":
                    stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
                    filename = stream.download(path)
                    # Renomear o arquivo para ter a extensão .mp3
                    os.rename(filename, filename[:-4] + ".mp3")
                else:
                    stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
                    filename = stream.download(path)
                
                self.show_message_log(f"Download finalizado com sucesso: {filename}", "success")
                self.result.setText(f"Download finalizado com sucesso")
                self.btnDownload.setText("Baixar")
                self.btnDownload.setEnabled(True)
            except Exception as e:
                self.result.setText(f"Erro ao fazer o download")
                self.btnDownload.setText("Baixar")
                self.btnDownload.setEnabled(True)
                self.show_message_log(f"Erro ao fazer o download: {str(e)}", "error")


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Setup()
    novo.show()
    qt.exec()

