from typing import Callable

NUM_KEY: str = "num"


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


type ValidValue = str | int


def sort_on_int_val(int_val_dict: dict[str, ValidValue]) -> ValidValue:
    return int_val_dict[NUM_KEY]


def spread_dict(dictToSpread: dict[str, ValidValue]) -> list[dict[str, ValidValue]]:
    spread_dicts: list[dict[str, ValidValue]] = []
    for k, v in dictToSpread.items():
        spread_dicts.append({"char": k, NUM_KEY: v})
    return spread_dicts


def sort_n_spread(
    dictionary: dict[str, ValidValue],
    sort_on: Callable[[dict[str, ValidValue]], ValidValue],
) -> list[dict[str, ValidValue]]:
    dicts: list[dict[str, ValidValue]] = spread_dict(dictionary)
    dicts.sort(reverse=True, key=sort_on)
    return dicts
