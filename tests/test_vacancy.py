def test_vacancy_init(vacancy):
    """ Тесты конструктора класса """

    assert vacancy.name == "Менеджер по работе с клиентами"
    assert vacancy.alternate_url == "https://hh.ru/vacancy/101709979"
    assert vacancy.salary_from == 4_000_000
    assert vacancy.salary_to == 7_000_000
    assert vacancy.area_name == "Ташкент"
    assert vacancy.requirement == "Опыт работы в продажах обязателен"
    assert vacancy.responsibility == "Консультирование клиентов"


def test_vacancy_str(vacancy):
    """ Тест строкового представления вакансии """

    assert str(vacancy) == ("Наименование вакансии: Менеджер по работе с клиентами\n"
                            "Ссылка на вакансию: https://hh.ru/vacancy/101709979\n"
                            "Зарплата: от 4000000 до 7000000\n"
                            "Место работы: Ташкент\n"
                            "Краткое описание: Опыт работы в продажах обязателен\n"
                            "Консультирование клиентов\n")


def test_vacancy_lt(vacancy, vacancy2):
    """ Тест утверждает, что одно значение меньше другого """

    assert vacancy2 < vacancy
    if vacancy > vacancy2:
        assert ValueError


def test_vacancy_from_hh_dict(vacancy):
    """ Тест утверждает, что метод вернет экземпляр класса в виде списка """

    assert (
        "Наименование вакансии: Менеджер по работе с клиентами,"
        "Ссылка на вакансию: https://hh.ru/vacancy/101709979,"
        "Зарплата: от 4000000 до 7000000,"
        "Место работы: Ташкент,"
        "Краткое описание: Опыт работы в продажах обязателен,"
        "Консультирование клиентов,"
    )


def test_vacancy_to_dict(vacancy):
    """ Тест утверждает, что метод вернет вакансию в виде словаря """

    assert {
        "name": "Менеджер по работе с клиентами",
        "alternate_url": "https://hh.ru/vacancy/101709979",
        "salary_from": 4000000,
        "salary_to": 7000000,
        "area_name": "Ташкент",
        "requirement": "Опыт работы в продажах обязателен",
        "responsibility": "Консультирование клиентов"
    }
