import matplotlib.pyplot as plt
import numpy as np
import cv2

def image_opener(image_jpg :str)-> np.ndarray:
    """
        функция открывания картинки
        :image_jpg: картинка получаемая из строки
        :return: массив двумерный, бывшая картинка
    """
    img = cv2.imread(image_jpg)
    if img is None:
        raise Exception ('Не удалось считать картинку')
    return  img

def histogram (image: np.ndarray) -> None:
    """
        функция построения гистограммы для картинки
    """
    plt.figure(figsize=(10,5))
    colors = ('blue','green','red')
    for i, color in enumerate(colors):
        histogram = cv2.calcHist([image],[i], None, [256], [0,256])
        plt.plot(histogram, color = color, label= f'{color} - канал')

    plt.title("Гистограмма")
    plt.xlabel("Интенсивность цвета")
    plt.ylabel("Частота цвета")
    plt.legend()
    plt.xlim([0, 256])
    plt.show()

def rotation(image :np.ndarray,angle:int)-> np.ndarray:
        """
            функция поворота картинки
        """
        (h, w) = image.shape[:2]
        center = (int(w/2),int(h/2))
        rotation_matrix = cv2.getRotationMatrix2D(center,angle, 0.5)
        """
            'center' точка в серединке картинки, чтобы вокруг нее вращать
            'rotation_matrix' матрица, ктр используется для поворота
        """
        rotated = cv2.warpAffine(image, rotation_matrix, (w, h))
        return rotated

