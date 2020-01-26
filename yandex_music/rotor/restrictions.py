from typing import TYPE_CHECKING, Optional, Union

from yandex_music import YandexMusicObject, Enum, DiscreteScale

if TYPE_CHECKING:
    from yandex_music import Client

de_json = {
    'enum': Enum.de_json,
    'discrete-scale': DiscreteScale.de_json
}


class Restrictions(YandexMusicObject):
    """Класс, представляющий .

    Attributes:
        client (:obj:`yandex_music.Client`): Объект класса :class:`yandex_music.Client`, представляющий клиент
                Yandex Music.

    Args:
        client (:obj:`yandex_music.Client`, optional): Объект класса :class:`yandex_music.Client`, представляющий клиент
            Yandex Music.
        **kwargs: Произвольные ключевые аргументы полученные от API.
    """

    def __init__(self,
                 language: Optional[Union['Enum', 'DiscreteScale']],
                 diversity: Optional[Union['Enum', 'DiscreteScale']],
                 mood: Optional[Union['Enum', 'DiscreteScale']] = None,
                 energy: Optional[Union['Enum', 'DiscreteScale']] = None,
                 mood_energy: Optional[Union['Enum', 'DiscreteScale']] = None,
                 client: Optional['Client'] = None,
                 **kwargs) -> None:
        self.language = language
        self.diversity = diversity
        self.mood = mood
        self.energy = energy
        self.mood_energy = mood_energy

        self.client = client
        self._id_attrs = (self.language, self.diversity)

    @classmethod
    def de_json(cls, data: dict, client: 'Client') -> Optional['Restrictions']:
        """Десериализация объекта.

        Args:
            data (:obj:`dict`): Поля и значения десериализуемого объекта.
            client (:obj:`yandex_music.Client`): Объект класса :class:`yandex_music.Client`, представляющий клиент
                Yandex Music.

        Returns:
            :obj:`yandex_music.Restrictions`: Объект класса :class:`yandex_music.Restrictions`.
        """
        if not data:
            return None

        data = super(Restrictions, cls).de_json(data, client)

        for key, value in data.items():
            data[key] = de_json.get(value.get('type_'))(value, client)

        return cls(client=client, **data)
