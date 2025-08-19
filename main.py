from stats import *

def get_book_text(fp):
    with open(fp) as f:
        file_contents = f.read()

    return str(file_contents)

    
def main():
    str_book = get_book_text("books/frankenstein.txt")
    word_count = get_book_word_count(str_book)
    print(f"{word_count} words found in the document")
    print(count_frequency(str_book))
main()
