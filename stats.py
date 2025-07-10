def get_word_count(text: str) -> int:
    return len(text.split())


def get_char_count(text: str) -> dict[str, int]:
    char_count_dict: dict[str, int] = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in char_count_dict:
            char_count_dict[lower_char] = 1
            continue
        char_count_dict[lower_char] += 1
    return char_count_dict


def sort_on_int_val[P](int_val_dict: dict[P, int], key: P) -> int:
    return int_val_dict[key]
