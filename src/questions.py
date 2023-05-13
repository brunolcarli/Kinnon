import enum
from random import randint


class Scopes(enum.Enum):
    """
    Enumerate question scopes
    """
    SCOPE_1 = "Só por hoje meus pensamentos estarão concentrados na minha recuperação, em viver e apreciar a vida sem drogas."
    SCOPE_2 = "Só por hoje terei fé em alguém de NA que acredita em mim e quer ajudar na minha recuperação."
    SCOPE_3 = "Só por hoje terei um programa. Tentarei segui-lo o melhor que puder."
    SCOPE_4 = "Só por hoje tentarei conseguir uma melhor perspectiva da minha vida através de NA."
    SCOPE_5 = "Só por hoje não sentirei medo, pensarei nos meus novos companheiros, pessoas que não estão usando drogas e que encontraram uma nova maneira de viver. Enquanto eu seguir este caminho, não terei nada a temer."


def random_question_id():
    """
    Randomly returns a question ID.
    There are currently 42 questions registered on the backend,
    this number may change in the future.

    return: int
    """
    return randint(1, 42)
