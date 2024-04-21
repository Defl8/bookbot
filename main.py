def count_words(raw_text):
    word_count = 0
    words = raw_text.split()

    word_count = sum([1 for word in words])

    return word_count


def count_chars(raw_text):
    count_dict = dict()
    lower_raw_text = raw_text.lower()

    for char in lower_raw_text:
        if char in count_dict:
            count_dict[char] += 1  # increment char count
        else:
            count_dict[char] = 1  # make new entry for char

    return count_dict


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        word_count = count_words(file_contents)
        print(f"{word_count} found in the document.\n")

        char_count = count_chars(file_contents)
        sorted_char_count = dict(sorted(char_count.items(), reverse=True, key=lambda item: item[1]))  # Sort dict by value

        for entry in sorted_char_count:
            if entry.isalpha():
                print(f"The '{entry}' was found {char_count[entry]} times.")


if __name__ == "__main__":
    main()
