import random


genres = [
    ("Приключения", 9),
    ("Апокалипсис", 8),
    ("Киберпанк", 7),
    ("Тёмное фэнтези", 8),
    ("Детектив", 8),
    ("Дизельпанк", 5),
    ("Антиутопия/Утопия", 7),
    ("Эпическое фэнтези", 10),
    ("Фэнтези", 10),
    ("Аниме-фэнтези", 7),
    ("Жёсткая научная фантастика", 8),
    ("Исторический роман", 5),
    ("Хоррор", 7),
    ("Исекай", 8),
    ("Лавкрафтовский хоррор", 7),
    ("Магический реализм", 6),
    ("Меха", 6),
    ("Военный триллер", 7),
    ("Мистика", 6),
    ("Мифологическая история", 5),
    ("Полицейская драма", 6),
    ("Постапокалипсис", 8),
    ("Психологический триллер", 8),
    ("Романтическая комедия", 7),
    ("Научная фантастика", 9),
    ("Сэйнен", 7),
    ("Сёнен", 7),
    ("Слайс оф лайф", 5),
    ("Космическая опера", 8),
    ("Стимпанк", 6),
    ("Супергеройская история", 7),
    ("Путешествие во времени", 6),
    ("Вестерн", 6)
]

settings = [
    ("Древний Китай", 6),
    ("Древний Египет", 6),
    ("Древняя Греция", 7),
    ("Древний Рим", 6),
    ("Киберпанковый", 8),
    ("Фэнтезийный", 9),
    ("Футуристический", 8),
    ("Средневековый", 9),
    ("Модерн", 5),
    ("Мифологический", 7),
    ("Неон-нуар", 5),
    ("Пиратский", 7),
    ("Постапокалиптический", 8),
    ("Ренессансный", 6),
    ("Самурайский", 7),
    ("Скандинавский", 6),
    ("Космический", 8),
    ("Стимпанковый", 6),
    ("Викторианский", 6),
    ("Дикий Запад", 7)
]


def randomSettings() -> str:
    return random.choices([randomGenre(genre[0]) for genre in genres] +
                          [randomSetting(setting[0]) for setting in settings],
                          weights=[genre[1] for genre in genres] + [setting[1] for setting in settings],
                          k=1
                          )[0]


def randomGenre(genre): return f'История в жанре "{genre}"'
def randomSetting(setting): return f'История в сеттинге "{setting}"'


def settingsPrompt(user_settings: str = None):
    return (
        'Пожелания игрока:\n'
        f'{user_settings if user_settings else randomSettings()}'
    )
