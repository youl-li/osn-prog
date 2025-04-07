class Yana:
    def __init__(self, name="Yana", surname="Naumovich", birth_year=2008):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def calculate_course(self):
        if self.birth_year is None:
            return "Рік народження не вказано"
        current_year = 2025
        age = current_year - self.birth_year
        course = age - 17 + 1
        if course < 1:
            return "Ще не студент"
        elif course > 4:
            return "Закінчив бакалаврат"
        return f"{course} курс"

    def full_name_list(self):
        return [self.name, self.surname]


class YanaExtended(Yana):
    def __init__(self, name="Yana", surname="Naumovich", birth_year=2008,
                 city=None, college=None, specialty=None):
        super().__init__(name, surname, birth_year)
        self.city = city
        self.college = college
        self.__specialty = specialty  # private атрибут

    def _greet_user(self):  # protected метод
        return f"Вітаю! Я {self.name} з міста {self.city}, навчаюся в {self.college}."

    def __calculate_study_years(self):  # private метод
        if self.birth_year is None:
            return None
        current_year = 2025
        return current_year - self.birth_year

    def get_study_years(self):  # відкритий метод для доступу до приватного
        years = self.__calculate_study_years()
        return f"Я навчаюся вже {years - 17 + 1} років" if years else "Немає даних"