import os
import json
import random
import requests
from typing import Callable
from functools import partial

Dictionary = dict[str, str]
WordPair = tuple[str, str]
PrepareWordPairsFunc = Callable[[int], list[WordPair]]

ENGLISH_GERMAN_FILE_PATH = "data/english_german.json"
GERMAN_ENGLISH_FILE_PATH = "data/german_english.json"


def prepare_word_pairs_func_factory(dictionary_path: str) -> PrepareWordPairsFunc:
    return partial(draw_word_pairs, dictionary=load_dictionary(dictionary_path))


def draw_word_pairs(dictionary: Dictionary, n_samples: int) -> list[WordPair]:
    unused_keys = list(dictionary.keys())
    word_pairs: list[WordPair] = []
    while len(word_pairs) < n_samples:
        key = random.choice(unused_keys)
        word_pairs.append((key, dictionary.get(key)))
        unused_keys.remove(key)
    return word_pairs


def load_dictionary(dictionary_path: str) -> Dictionary:
    with open(dictionary_path) as file:
        return json.load(file)


def setup_sample_dictionaries() -> None:
    english_german_url = "https://raw.githubusercontent.com/hathibelagal/German-English-JSON-Dictionary/master/english_german.json"
    german_english_url = "https://raw.githubusercontent.com/hathibelagal/German-English-JSON-Dictionary/master/german_english.json"

    if not is_file_present(ENGLISH_GERMAN_FILE_PATH):
        download_file(url=english_german_url, local_path=ENGLISH_GERMAN_FILE_PATH)
    if not is_file_present(GERMAN_ENGLISH_FILE_PATH):
        download_file(url=german_english_url, local_path=GERMAN_ENGLISH_FILE_PATH)


def is_file_present(file_path: str) -> bool:
    return os.path.exists(file_path)


def download_file(url: str, local_path: str) -> None:
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(
            f"The GET request for the '{url}' url returned a reponse with status code {response.status_code}."
        )
    with open(local_path, "wb") as file:
        file.write(response.content)


if __name__ == "__main__":
    setup_sample_dictionaries()
    prepare_english_german_word_pairs = prepare_word_pairs_func_factory(
        ENGLISH_GERMAN_FILE_PATH
    )
    print(prepare_english_german_word_pairs(n_samples=10))
