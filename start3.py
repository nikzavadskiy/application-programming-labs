import  argparse
import numpy as np
import cv2


from smt_with_image import image_opener, histogram, rotation



def get_smt_from_cmd() -> None:
    """
    получает из командной строки путь к картинке, путь для сохранения, и угол поворота картинки 
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('directory_to_open',type=str, help='directory to open image')
    parser.add_argument('directory_to_save',type=str, help='directory to save changed image')
    parser.add_argument('angle',type=int, help="angle for image's rotation")
    return parser.parse_args()

def main():

    arg = get_smt_from_cmd()

    try:
        
        exodus_image = image_opener(arg.directory_to_open)
        cv2.imshow('awesome picture', exodus_image)
        cv2.waitKey(0)

        exodus_shape = exodus_image.shape
        print(f"Размер изображения: {exodus_shape}")


        rotated_image = rotation(exodus_image,arg.angle)
        cv2.imshow('awesome picture2', rotated_image)
        cv2.waitKey(0)

        histogram(exodus_image)

        cv2.imwrite(arg.directory_to_save, rotated_image)


    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
