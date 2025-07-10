import sys


from stats import (
    get_word_count,
    get_char_count,
    sort_n_spread,
    sort_on_int_val,
    ValidValue,
)

BOOK_ARG_IDX: int = 1


def get_book_test(book_path: str) -> str:
    with open(book_path, "r") as book:
        return book.read()


def main() -> None:
    args: list[str] = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path: str = args[BOOK_ARG_IDX]

    print("============ BOOKBOT ============")

    # book_text: str = get_book_test("books/frankenstein.txt")
    book_text: str = get_book_test(book_path)

    print(f"Analyzing book found found at {book_path}...")
    print("----------- Word Count ----------")

    word_count: int = get_word_count(book_text)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")

    char_counts: dict[str, int] = get_char_count(book_text)

    sorted_char_counts: list[dict[str, ValidValue]] = sort_n_spread(
        char_counts, sort_on=sort_on_int_val
    )

    for d in sorted_char_counts:
        char: str = str(d["char"])
        if not char.isalpha():
            continue
        print(f"{char}: {d["num"]}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
