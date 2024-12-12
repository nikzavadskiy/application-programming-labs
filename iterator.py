import os
import csv

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