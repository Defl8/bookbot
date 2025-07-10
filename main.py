def get_book_test(book_path: str) -> str:
    with open(book_path, "r") as book:
        return book.read()


def get_word_count(text: str) -> int:
    return len(text.split(" "))


def main() -> None:
    book_text: str = get_book_test("books/frankenstein.txt")

    word_count: int = get_word_count(book_text)
    print(f"{word_count} words found in document")


if __name__ == "__main__":
    main()
