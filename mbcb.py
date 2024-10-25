import argparse
import re


def get_smt_from_cmd() -> str:
    """ 
    получает из командной строки: название файла и имя для подсчета
    """
    parser = argparse.ArgumentParser() 
    parser.add_argument('file_name', type=str, help='file that needs to open')
    parser.add_argument('human_name', type=str, help='name for find how many people same have it')
    return parser.parse_args()


def read(file_name: str) -> str:
    """
     считывает файл
     :param filename: имя исх. файла
    :return: строку со всеми данными из считываемого файла
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            text = file.read()
        return text
    except file_not_found as erorr_reading:
        raise file_not_found(f"Ошибка: файл с именем '{file_name}'  не найден : {erorr_reading}")


def split_to_names (text:str)->list:
    pattern = r'Имя:\s*([а-яА-Я]+)'
    names=re.findall(pattern,text)
    return names
    

def define_count(names: list, human_name:str) -> None:
    print(text.count(human_name))
    

def main():
    """
    """
    try:
        arguments = get_smt_from_cmd()
        txt = read(arguments.file_name)
        names = split_to_names(txt)
        define_count(names, arguments.human_name)
    except exception as erorr:
        print(f"Произошла ошибка: {erorr}")

if __name__ == "__main__":
    main()
