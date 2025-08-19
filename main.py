def get_book_text(fp):
    with open(fp) as f:
        file_contents = f.read()

    return str(file_contents)

def get_book_word_count(book_string):
    count = 0
    split_book_string = book_string.split(" ")

    for i in split_book_string:
        count += 1
    
    return count 
    
def main():
    str_book = get_book_text("books/frankenstein.txt")
    word_count = get_book_word_count(str_book)
    return print(f"{word_count} words found in the document")

main()
