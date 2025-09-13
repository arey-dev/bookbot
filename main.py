import sys
from stats import get_num_words, get_chars_count, get_sorted_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

        return file_contents

def main():
    cmds = sys.argv
    
    if len(cmds) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = cmds[1] 
    book_text = get_book_text(file_path)
    word_count = get_num_words(book_text) 
    char_dict = get_chars_count(book_text)
    sorted_list_dic = get_sorted_dict(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {75767} total words")
    print("--------- Character Count -------")
    
    for dic in sorted_list_dic:
        if dic["name"].isalpha():
            print(f"{dic["name"]}: {dic["num"]}")

    print('============= END ===============')

main()
