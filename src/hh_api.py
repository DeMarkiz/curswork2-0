import requests
from requests import Response

from src.get_vacancies import GetVacanciesAPI


class HeadHunterAPI(GetVacanciesAPI):
    """ Класс для подключения к hh.ru """

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "per_page": "", "only_with_salary": True}

    def get_response(self, keyword, per_page) -> Response:
        self.params["text"] = keyword
        self.params["per_page"] = per_page
        return requests.get(self.url, params=self.params)

    def get_vacancies(self, keyword: str, per_page: int):
        return self.get_response(keyword, per_page).json()["items"]
    