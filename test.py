import pytest

# 1 задание


def find_unique_names(courses, mentors):
    all_list = []
    for m in mentors:
        all_list.extend(m)
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)

    unique_names = list(set(all_names_list))
    all_names_sorted = sorted(unique_names)
    return f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}'


def test_find_unique_names():
    courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
               "Frontend-разработчик с нуля"]

    mentors = [
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
         "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
         "Азамат Искаков",
         "Роман Гордиенко"],
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
         "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
         "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
         "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
         "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
         "Денис Ежков",
         "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
         "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]
    res = find_unique_names(courses, mentors)
    expected = 'Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий'
    assert res == expected


def top_3_names(courses, mentors):
    all_list = []
    for m in mentors:
        all_list.extend(m)

    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)

    unique_names = set(all_names_list)

    popular = []
    for name in unique_names:
        popular.append([name, all_names_list.count(name)])  # Добавьте подсчёт имён

    popular.sort(key=lambda x: x[1], reverse=True)

    top_3 = popular[0:3]
    final_result = []
    for name in top_3:
        final_result.append(name)
    top = [f"{str(i[0])}: {str(i[1])} раз(а)" for i in top_3]
    return ", ".join(top)


def test_top_3_names():
    courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
               "Frontend-разработчик с нуля"]

    mentors = [
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
         "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
         "Азамат Искаков", "Роман Гордиенко"],
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
         "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
         "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
         "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
         "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
         "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
         "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]
    res = top_3_names(courses, mentors)
    expected = 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'
    assert res == expected


def connection_research(courses, mentors, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)
    duration_index = []
    mcount_index = []
    for index, course in enumerate(courses_list):
        duration_index.append([course['duration'], index])
        mcount_index.append([len(course['mentors']), index])
    duration_index.sort()
    mcount_index.sort()
    indexes_d = []
    indexes_m = []
    for el in duration_index:
        indexes_d.append(el[1])
    for el in mcount_index:
        indexes_m.append(el[1])
    return f"""Связь есть
Порядок курсов по длительности: {indexes_d}
Порядок курсов по количеству преподавателей: {indexes_m}""" if indexes_m == indexes_d else f"""Связи нет
Порядок курсов по длительности: {indexes_d}
Порядок курсов по количеству преподавателей: {indexes_m}"""


def test_connection_research():
    courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
               "Frontend-разработчик с нуля"]
    mentors = [
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
         "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
         "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
         "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
         "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
         "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
         "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
         "Азамат Искаков", "Роман Гордиенко"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
         "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]
    durations = [14, 20, 12, 20]
    res = connection_research(courses, mentors, durations)
    expected = '''Связи нет
Порядок курсов по длительности: [2, 0, 1, 3]
Порядок курсов по количеству преподавателей: [2, 3, 1, 0]'''
    assert res == expected

# 2 задание

import os

import requests
from dotenv import load_dotenv

load_dotenv()

yandex_token = os.getenv('yandex_token')
def get_headers(yandex_token):
        yandex_token = yandex_token
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {yandex_token}'
        }

def yandex_put_folder(url_yandex, path, yandex_token):
    headers = get_headers(f'{yandex_token}')
    params = {'path': path}
    response = requests.put(url=url_yandex, headers=headers, params=params)
    return response

def test_yandex_put_folder():
    url_yandex = 'https://cloud-api.yandex.net/v1/disk/resources'
    path = 'Тестовая папка'
    yandex_token = os.getenv('yandex_token')
    response = yandex_put_folder(url_yandex, path, yandex_token)
    res = response.status_code
    assert res == 201

import unittest

class MyTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_failure_yandex_put_folder(self):
        self.url_yandex = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.path = 'Тестовая папка'
        self.yandex_token = os.getenv('yandex_token')
        response = yandex_put_folder(self.url_yandex, self.path, self.yandex_token)
        res = response.status_code
        self.assertFalse(res != 400, 'Некорректные данные.')
        self.assertFalse(res != 401, 'Не авторизован.')
        self.assertFalse(res != 403, 'API недоступно. Ваши файлы занимают больше места, чем у вас есть.')
        self.assertFalse(res != 404, 'Не удалось найти запрошенный ресурс.')