import os


def get_file_content(path):
    file = open(path)
    content = file.read()
    return str(content), 1


def get_file_by_name(name):
    path_convert = os.path.abspath(name) + '.201'
    file = open(path_convert.replace(r"b'",  ''))
    content = file.read()
    return content


def archives_out(data_lex, data_tab, name):
    lex_file = open(name + '.LEX', 'a')
    lex_file.write(data_lex[0])
    lex_file.close()
    tab_file = open(name + '.TAB', 'a')
    tab_file.write(data_tab + '\n')
    tab_file.close()
    return 1
