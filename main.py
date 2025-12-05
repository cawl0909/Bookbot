from stats import *

def get_book_text(file_path : str) -> str:
    file = open(file_path)
    file_contents = file.read()
    return file_contents

def sort_on(items):
    return items["num"]

def main():
    #word_count(get_book_text("books/frankenstein.txt"))
    #print(count_chars(get_book_text("books/frankenstein.txt")))
    sorted_char_list = (char_dict_to_list(count_chars(get_book_text("books/frankenstein.txt"))))
    print("""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------""")
    for item in sorted_char_list:
        if(item["char"].isalpha()):
            print(f"{item["char"]} : {item["num"]}")
    print("============= END ===============")
        
main()