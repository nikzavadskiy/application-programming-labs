import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap

from iterator import IteratorForImages

class AwesomeWindow (QMainWindow):
    
    def __init__(self):
        super().__init__()  
        self.setWindowTitle("Awesome pictures of horses")

        self.image_label = QLabel(self)  #метка для текста
        self.image_label.setFixedSize(1000, 800)

        self.next_button = QPushButton("Следующее изображение", self) 
        self.next_button.clicked.connect(self.letsgo_to_the_next_image)

        self.open_button = QPushButton("Выбрать csv файл", self)
        self.open_button.clicked.connect(self.open_csv)

        # Создаем вертикальную компоновку и добавляем в нее кнопки
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.next_button)
        layout.addWidget(self.open_button)

        # Создаем виджет-контейнер и устанавливаем для него макет
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.iterator = None

    def open_csv(self) -> None:
        csv_path = QFileDialog.getOpenFileName(self, "Выберите csv файл  ","", "CSV file (*.csv)")
        if csv_path[0]:
            self.iterator = IteratorForImages(csv_path[0])
            if len(self.iterator.images) == 0:
                self.image_label.setText("Изображений нет в папке")
                return None
            # Открытие  первого изображения 
            next_image_path = next(self.iterator)
            pixmap = QPixmap(next_image_path)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), aspectRatioMode=1))

    def letsgo_to_the_next_image(self) -> None:
        if self.iterator and len(self.iterator.images) != 0:
            try:
                next_image_path = next(self.iterator)
                pixmap = QPixmap(next_image_path)  
                self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), aspectRatioMode=1)) 
            except StopIteration:
                self.image_label.setText("Больше изображений нет")

def main():
    try:
        app = QApplication(sys.argv)
        window = AwesomeWindow() 
        window.show() 
        sys.exit(app.exec_())  

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()