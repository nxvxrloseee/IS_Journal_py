import json

class Student:
    def __init__(self, name, surname, grade):
        self.__name = name
        self.__surname = surname
        self.__grade = grade

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade

    def to_dict(self):
        return {
            "name": self.__name,
            "surname": self.__surname,
            "grade": self.__grade
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["surname"], data["grade"])


class Journal:
    def __init__(self):
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)

    def remove_student(self, student):
        self.__students.remove(student)

    def get_students(self):
        return self.__students

    def to_dict(self):
        return {
            "students": [student.to_dict() for student in self.__students]
        }

    @classmethod
    def from_dict(cls, data):
        journal = cls()
        for student_data in data["students"]:
            journal.add_student(Student.from_dict(student_data))
        return journal


class University:
    def __init__(self):
        self.__journals = []

    def add_journal(self, journal):
        self.__journals.append(journal)

    def remove_journal(self, journal):
        self.__journals.remove(journal)

    def get_journals(self):
        return self.__journals

    def to_dict(self):
        return {
            "journals": [journal.to_dict() for journal in self.__journals]
        }

    @classmethod
    def from_dict(cls, data):
        university = cls()
        for journal_data in data["journals"]:
            university.add_journal(Journal.from_dict(journal_data))
        return university


def export_data(university, filename):
    data = university.to_dict()
    with open(filename, "w") as f:
        json.dump(data, f)


def import_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return University.from_dict(data)


def main():
    university = University()

    while True:
        print("\nМеню:")
        print("1. Добавить студента")
        print("2. Удалить студента")
        print("3. Просмотреть список студентов")
        print("4. Экспортировать данные")
        print("5. Импортировать данные")
        print("6. Выход")

        choice = input("Введите номер пункта меню: ")

        if choice == "1":
            name = input("Введите имя студента: ")
            surname = input("Введите фамилию студента: ")
            grade = int(input("Введите оценку студента: "))
            student = Student(name, surname, grade)
            journal = Journal()
            journal.add_student(student)
            university.add_journal(journal)
            print("Студент добавлен успешно!")

        elif choice == "2":
            name = input("Введите имя студента: ")
            surname = input("Введите фамилию студента: ")
            for journal in university.get_journals():
                for student in journal.get_students():
                    if student.get_name() == name and student.get_surname() == surname:
                        journal.remove_student(student)
                        print("Студент удален успешно!")
                        break
                else:
                    continue
                break
            else:
                print("Студент не найден!")

        elif choice == "3":
            for journal in university.get_journals():
                for student in journal.get_students():
                    print(f"Имя: {student.get_name()}, Фамилия: {student.get_surname()}, Оценка: {student.get_grade()}")

        elif choice == "4":
            filename = input("Введите имя файла для экспорта: ")
            export_data(university, filename)
            print("Данные экспортированы успешно!")

        elif choice == "5":
            filename = input("Введите имя файла для импорта: ")
            university = import_data(filename)
            print("Данные импортированы успешно!")

        elif choice == "6":
            print("Выход из программы!")
            break

        else:
            print("Недопустимый выбор! Пожалуйста, выберите другой пункт меню.")


if __name__ == "__main__":
    main()
