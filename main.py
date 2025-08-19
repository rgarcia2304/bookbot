from stats import *

def get_book_text(fp):
    with open(fp) as f:
        file_contents = f.read()

    return str(file_contents)

    
def main():
    str_book = get_book_text("books/frankenstein.txt")
    word_count = get_book_word_count(str_book)
    ranked_dicts = format_count(count_frequency(str_book))
    #print(f"{word_count} words found in the document")
    #print(count_frequency(str_book))
    #print(ranked_dicts)


    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for val in ranked_dicts:
        print(f"{val} \n ")

main()
