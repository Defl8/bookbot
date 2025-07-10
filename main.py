def get_book_test(book_path: str) -> str:
    with open(book_path, "r") as book:
        return book.read()


def main() -> None:
    book_text: str = get_book_test("books/frankenstein.txt")
    print(book_text)


if __name__ == "__main__":
    main()
