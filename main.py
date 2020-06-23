import os
import mainLex
import text_system as tx


def main():
    lex_out = str
    print("o-script compiler ver 0.1")
    text = str
    user_path = input("enter your file: ")
    if os.path.isabs(user_path):
        try:
            text = tx.get_file_content(user_path)
        except:
            print("file doesn't exist")
    else:
        try:
            text = tx.get_file_by_name(user_path)
        except:
            print("wrong name of file or file doesn't exist, wrong path")
    try:
        lex_out, tolkens, TAB = mainLex.executarLexico(text)
        tx.archives_out(lex_out, TAB, '0')
        print("compilation finished!")
    except:
        print("invalid archive path")
        print("compilation failed!")

    os.system("pause")


if __name__ == "__main__":
    main()
