import argparse
import os 
import csv

from icrawler.builtin import GoogleImageCrawler

def get_smt_from_cmd() -> str:
    """ 
    получает из командной строки: ключевое слово, путь к директории и путь к аннотации
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('key_word', type=str, help='this is word means your dreams about some animals')
    parser.add_argument('dir_for_save', type=str, help='directory to save images')
    parser.add_argument('anotation_file', type=str, help='directory where keeps annotation file')
    args = parser.parse_args()  
    return args

def download_images(key_word:str, dir_for_save:str, number_of_images:int) -> None:
    """
    закачка изображений в указанную директорию
    """
    if not os.path.exists(dir_for_save):
        os.makedirs(dir_for_save)
    google_crawler = GoogleImageCrawler(storage={'root_dir': dir_for_save})
    google_crawler.crawl(keyword=key_word, max_num=number_of_images)

def create_annotation(dir_for_save:str,anotation_file:str)-> None:
     """
    создание аннотации
    """
     if not os.path.exists(anotation_file):
        os.makedirs(anotation_file)
     with open(anotation_file, 'w', newline='') as csv:
        writer = csv.DictWriter(csv, fieldnames=['absolute_path', 'relative_path'])
        writer.writeheader()
        for root, _, files in os.walk(dir_for_save):
            for file in files:
                if file.endswith(('jpg', 'jpeg', 'png')):
                    """
                    смотрит, чтобы заканчивался файл данными расширениями файлов
                    """
                    abs_path = os.path.join(root, file)
                    rel_path = os.path.relpath(abs_path, start=dir_for_save)
                    writer.writerow({'absolute_path': abs_path, 'relative_path': rel_path})

class IteratorForImages:
    """
    конструктор, создающий список из файлов по аннотации
    """
    def __init__(self, anotation_file:str):
        self.images = []  
        self.counter = 0    
        with open(anotation_file, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.images.append(row['absolute_path'])

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.images):
            image_path = self.images[self.counter]
            self.counter += 1
            return image_path
        else:
            raise StopIteration
       
def main():
    args = get_smt_from_cmd()
    try:
        download_images(args.key_word, args.dir_for_save, 83)
        create_annotation(args.dir_for_save, args.anotation_file)
        iterator = IteratorForImages(args.anotation_file)
        for image_path in iterator:
            print(image_path)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()       