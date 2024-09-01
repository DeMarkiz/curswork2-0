from abc import ABC, abstractmethod


class BaseAPIhhParse(ABC):
    """Абстрактный класс для получения вакансии с hh.ru"""

    @abstractmethod
    def get_response(self, keyword, per_page):
        pass

    @abstractmethod
    def get_vacancies(self, keyword, per_page):
        pass
