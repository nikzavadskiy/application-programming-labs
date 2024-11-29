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
        rotation_matrix = cv2.getRotationMatrix2D(center,angle,1.0)
        """
            'center' точка в серединке картинки, чтобы вокруг нее вращать
            'rotation_matrix' матрица, ктр используется для поворота
        """
        cos = abs(rotation_matrix[0,0])
        sin = abs(rotation_matrix[0,1])
        new_w = int((h*sin)+(w*cos))
        new_h = int((h*cos)+(w*sin))

        rotation_matrix[0,2] += (new_w/2) - center[0]
        rotation_matrix[1,2] += (new_h/2) - center[1]
        
        rotated = cv2.warpAffine(image, rotation_matrix, (new_w, new_h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT, borderValue(0,0,0))
        return rotated

