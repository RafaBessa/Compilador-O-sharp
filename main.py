import os
import sys
import mainLex


def get_file_content(path):
    file = open(path)
    content = file.read()
    return str(content), 1


def get_file_by_name(name):
    dash = r'\\'
    ext = '.201'
    path = os.getcwdb()
    path_convert = os.path.abspath(name) + '.201'
    file = open(path_convert.replace(r"b'",  ''))
    content = file.read()
    return content


def main():
    print("o-script compiler ver 0.1")
    text = str
    user_path = input("enter your file: ")
    if os.path.isabs(user_path):
        try:
            text = get_file_content(user_path)
        except:
            print("file doesn't exist")
    else:
        try:
            text = get_file_by_name(user_path)
        except:
            print("wrong name of file or file doesn't exist")
    mainLex.executarLexico(text)
    os.system("pause")


if __name__ == "__main__":
    main()
