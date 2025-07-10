from stats import get_word_count, get_char_count


def get_book_test(book_path: str) -> str:
    with open(book_path, "r") as book:
        return book.read()


def main() -> None:
    book_text: str = get_book_test("books/frankenstein.txt")

    word_count: int = get_word_count(book_text)
    print(f"{word_count} words found in the document")
    char_counts: dict[str, int] = get_char_count(book_text)
    print(char_counts)


if __name__ == "__main__":
    main()
