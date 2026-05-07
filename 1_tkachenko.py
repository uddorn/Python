import os

surname = os.environ.get("STUDENT_SURNAME")

if surname:
    print(f"Змінна знайдена. Прізвище студента: {surname}")
else:
    print("Помилка: змінна STUDENT_SURNAME відсутня в середовищі.")