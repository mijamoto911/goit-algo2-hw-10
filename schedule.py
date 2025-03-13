# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()

    def __repr__(self):
        return f"{self.first_name} {self.last_name} ({self.age} років)"


def create_schedule(subjects, teachers):
    """
    Жадібний алгоритм для призначення викладачів на предмети.
    Вибирає викладачів так, щоб покрити всі предмети, мінімізуючи їхню кількість.
    """
    remaining_subjects = set(subjects)
    assigned_teachers = []

    while remaining_subjects:
        best_teacher = None
        best_covered = set()

        for teacher in teachers:
            can_teach = teacher.can_teach_subjects & remaining_subjects
            if len(can_teach) > len(best_covered) or (
                len(can_teach) == len(best_covered)
                and best_teacher
                and teacher.age < best_teacher.age
            ):
                best_teacher = teacher
                best_covered = can_teach

        if not best_teacher:
            print("Неможливо покрити всі предмети наявними викладачами.")
            return []

        best_teacher.assigned_subjects = best_covered
        assigned_teachers.append(best_teacher)
        remaining_subjects -= best_covered

    return assigned_teachers


if __name__ == "__main__":
    # Множина предметів
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}

    # Список викладачів
    teachers = [
        Teacher(
            "Олександр",
            "Іваненко",
            45,
            "o.ivanenko@example.com",
            {"Математика", "Фізика"},
        ),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher(
            "Сергій",
            "Коваленко",
            50,
            "s.kovalenko@example.com",
            {"Інформатика", "Математика"},
        ),
        Teacher(
            "Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}
        ),
        Teacher(
            "Дмитро",
            "Бондаренко",
            35,
            "d.bondarenko@example.com",
            {"Фізика", "Інформатика"},
        ),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("\nРозклад занять:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
