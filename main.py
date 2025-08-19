def get_book_text(fp):
    with open(fp) as f:
        file_contents = f.read()

    return str(file_contents)

def main():
    str_book = get_book_text("books/frankenstein.txt")
    print(str_book)

main()
