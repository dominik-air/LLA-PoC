from etl import prepare_word_pairs_func_factory, ENGLISH_GERMAN_FILE_PATH
from tts import Text2Speech, SupportedLanguages

if __name__ == "__main__":

    prepare_english_german_word_pairs = prepare_word_pairs_func_factory(
        ENGLISH_GERMAN_FILE_PATH
    )
    tts_engine = Text2Speech()

    word_pairs = prepare_english_german_word_pairs(n_samples=10)

    for word_pair in word_pairs:
        english, german = word_pair
        tts_engine.switch_language(language=SupportedLanguages.ENGLISH)
        print(english)
        tts_engine.speak(english)
        tts_engine.switch_language(language=SupportedLanguages.GERMAN)
        print(german)
        tts_engine.speak(german)
