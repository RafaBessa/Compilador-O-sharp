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


def archives_out(data_tab, data_lex, name):
    lex_file = open(name + '.LEX', 'a')
    lex_file.write(data_lex + '\n')
    lex_file.close()
    tab_file = open(name + '.TAB', 'a')
    tab_file.write(data_tab + '\n')
    tab_file.close()
    return 1


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
    print("compilation finished!")
    os.system("pause")


if __name__ == "__main__":
    main()
