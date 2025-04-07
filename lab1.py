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