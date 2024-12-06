import argparse
import cv2
import matplotlib.pyplot as plt
import pandas as pd

def get_smt_from_cmd() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("annotation's_path", type=str, help='directory where keeps annotation file')
    args = parser.parse_args()
    args = parser.parse_args()  
    return args

def get_images_information(path: str) -> tuple:
    '''
    получение параметров изображения: высоту, ширина, глубина
    :param path: path_to_image
    :return: height, width, depth
    '''
    image = cv2.imread(path)
    if image is not None:
         height, width, depth = image.shape
         return height, width, depth
    else:
        return None, None, None
    
def three_columns_of_param(df: pd.DataFrame) -> None:
    '''
    создание столбцов с параметрами изображения
    :param df: датафрейм
    :return: None
    '''
    heights, widths, depths = [], [], []
    for path in df['absolute_path']:
        height, width, depth = get_images_information(path)
        heights.append(height)
        widths.append(width)
        depths.append(depth)

    df['height'] = heights
    df['width'] = widths
    df['depth'] = depths


def filter_by_size(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
   """
   фильтрует DataFrame по размеру изображений
   :param df: датафрейм
   :param max_width: макс ширина 
   :param max_height:макс высота
   :return: объект датафрейм
   """
   return df[(df['height'] <= max_height) & (df['width'] <= max_width)]

def add_column_area(df: pd.DataFrame) -> None:
    '''
    добавления нового столбца площади
    :param df: датафрейм
    :return: None
    '''
    df['area'] = df['height'] * df['width']

def histogram(df: pd.DataFrame) -> None:
   """
   гистограмма
   :param df:датафрейм
   :return: None
   """
   plt.figure(figsize=(10, 5))
   plt.hist(df['area'], bins=20, color='orange', edgecolor='black')
   plt.title("Распределение площадей изображений")
   plt.xlabel("Площадь")
   plt.ylabel("Кол-во")
   plt.show()


def main():

    try:
        annotation_path = get_smt_from_cmd()
        df = pd.read_csv(annotation_path)

        three_columns_of_param(df)

        statistick = df[['height', 'width', 'depth']].describe()
        print(statistick)

        filtered_df = filter_by_size(df, 1000, 1000)
        print(filtered_df)

        add_column_area(df)
        
        filtered_df_by_area = df.sort_values(by='area')

        histogram(df)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()