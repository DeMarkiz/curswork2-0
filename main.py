from config import VACANCIES_PATH_TXT, VACANCIES_PATH_JSON
from src.json_saver import JSONSaver
from src.txt_saver import TXTSaver
from src.utils import user_choice_json, user_choice_txt
from src.db import DBManager


def main():
    """ Запуск программы """
    user_input = input("Здравствуйте!\n"
                       "В каком формате хотите записать данные?\n"
                       "Если в json формат, введите 1\n"
                       "Если в txt формат, введите 2\n"
                       "Если хотите удалить данные из файла, введите 3\n")

    if user_input == "1":
        user_choice_json()
    elif user_input == "2":
        user_choice_txt()
    elif user_input == "3":
        user_input = input("Какой файл вы хотите отчистить?\n"
                           "json-файл, введите 1\n"
                           "txt-файл, введите 2\n")
        if user_input == "1":
            deleter = JSONSaver(VACANCIES_PATH_JSON)
            deleter.del_data()
            print("Данные удалены!")
        elif user_input == "2":
            deleter = TXTSaver(VACANCIES_PATH_TXT)
            deleter.del_data()
            print("Данные удалены!")
    return


if __name__ == "__main__":
    main()
    db = DBManager(dbname='test', user='postgres', password='2585')
    # Пример данных для добавления
    employer_data = {
        "naming": "Компания XYZ",
        "industry": "Информационные технологии",
        "website": "https://xyz.com",
        "location": "Москва"
    }

    # Добавление работодателя
    employer_id = db.add_employer(
        employer_data["naming"],
        employer_data["industry"],
        employer_data["website"],
        employer_data["location"]
    )

    # Пример данных вакансии
    vacancy_data = {
        "title": "Программист Python",
        "description": "Разработка приложений на Python",
        "salary": 100000,
        "data_posted": "2024-10-07"
    }

    # Добавление вакансии с указанием ID работодателя
    db.add_vacancy(
        vacancy_data["title"],
        vacancy_data["description"],
        vacancy_data["salary"],
        employer_id,
        vacancy_data["data_posted"]
    )

    db.close()
