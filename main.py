import os
import mainLex
import text_system as tx


def main():
    lex_out = str
    print("o-script compiler written in python")
    text = str
    user_path = input("enter your file path or name: ")
    if os.path.isabs(user_path):
        try:
            text = tx.get_file_content(user_path)
        except:
            print("file doesn't exist")
            return 1
    else:
        try:
            text = tx.get_file_by_name(user_path)
        except:
            print("wrong name of file or file doesn't exist, wrong path")
            return -1
    try:
        lex_out, tolkens, TAB = mainLex.executarLexico(text)
        tx.archives_out(lex_out, TAB, '0')
        print("compilation finished!")
        os.system("pause")
        return 0
    except: 
        print("invalid written archive path")
        print("compilation failed!")
        os.system("pause")
        return -1


if __name__ == "__main__":
    main()
