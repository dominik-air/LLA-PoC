from enum import Enum
import pyttsx3


class SupportedLanguages(int, Enum):
    ENGLISH = 10
    GERMAN = 4


class Text2Speech:
    def __init__(self) -> None:
        self.engine = pyttsx3.init()

    def switch_language(self, language: SupportedLanguages) -> None:
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[language].id)

    def speak(self, text: str) -> None:
        self.engine.say(text)
        self.engine.runAndWait()
