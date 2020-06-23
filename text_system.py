import os


def get_file_content(path):
    file = open(path)
    content = file.read()
    return content


def get_file_by_name(name):
    path_convert = os.path.abspath(name) + '.201'
    file = open(path_convert.replace(r"b'",  ''))
    content = file.read()
    return content


def archives_out(data_lex, data_tab, name):
    if os.path.isabs(name):
        new_name = os.path.basename(name).replace(".201", "")
    else:
        new_name = name
    lex_file = open(new_name + '.LEX', 'a')
    lex_file.write(data_lex[0])
    lex_file.close()
    tab_file = open(new_name + '.TAB', 'a')
    tab_file.write(data_tab)
    tab_file.close()
    return 1
