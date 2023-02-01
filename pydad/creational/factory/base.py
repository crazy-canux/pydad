from typing import Protocol, Dict, Type


class Localizer(Protocol):
    def localize(self, msg: str) -> str:
        pass
    
    
class GreekLocalizer:

    def __init__(self) -> None:
        self.translations = {"dog": "god", "cat": "tac"}

    def localize(self, msg: str) -> str:
        return self.translations.get(msg, msg)


class EnglishLocalizer:

    def localize(self, msg: str) -> str:
        return msg


def get_localizer(language: str = "English") -> Localizer:
    localizers: Dict[str, Type[Localizer]] = {
        "English": EnglishLocalizer,
        "Greek": GreekLocalizer,
    }
    return localizers[language]()


if __name__ == "__main__":
    e, g = get_localizer(language="English"), get_localizer(language="Greek")
    print(e, type(e))
    print(g, type(g))
    for msg in "dog parrot cat".split():
        print(e.localize(msg), g.localize(msg))