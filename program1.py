import csv
import random
from datetime import date
from faker import Faker

fake = Faker(locale='uk_UA')

male_patronymics = [
    "Олександрович", "Іванович", "Васильович", "Петрович", "Миколайович", 
    "Сергійович", "Вікторович", "Михайлович", "Андрійович", "Дмитрович", 
    "Володимирович", "Юрійович", "Анатолійович", "Степанович", "Богданович", 
    "Григорович", "Тарасович", "Романович", "Максимович", "Олегович"
]

female_patronymics = [
    "Олександрівна", "Іванівна", "Василівна", "Петрівна", "Миколаївна", 
    "Сергіївна", "Вікторівна", "Михайлівна", "Андріївна", "Дмитрівна", 
    "Володимирівна", "Юріївна", "Анатоліївна", "Степанівна", "Богданівна", 
    "Григорівна", "Тарасівна", "Романівна", "Максимівна", "Олегівна"
]

def generate_employees():
    employees = []
    
    for _ in range(300):
        employees.append({
            "Прізвище": fake.last_name_male(),
            "Ім’я": fake.first_name_male(),
            "По батькові": random.choice(male_patronymics),
            "Стать": "Чоловіча",
            "Дата народження": fake.date_between_dates(date_start=date(1946, 1, 1), date_end=date(2011, 12, 31)).strftime("%Y-%m-%d"),
            "Посада": fake.job(),
            "Місто проживання": fake.city(),
            "Адреса проживання": fake.address().replace('\n', ', '),
            "Телефон": fake.phone_number(),
            "Email": fake.email()
        })
        
    for _ in range(200):
        employees.append({
            "Прізвище": fake.last_name_female(),
            "Ім’я": fake.first_name_female(),
            "По батькові": random.choice(female_patronymics),
            "Стать": "Жіноча",
            "Дата народження": fake.date_between_dates(date_start=date(1946, 1, 1), date_end=date(2011, 12, 31)).strftime("%Y-%m-%d"),
            "Посада": fake.job(),
            "Місто проживання": fake.city(),
            "Адреса проживання": fake.address().replace('\n', ', '),
            "Телефон": fake.phone_number(),
            "Email": fake.email()
        })
        
    random.shuffle(employees)
    return employees

def main():
    print("Генерація даних співробітників...")
    employees_data = generate_employees()
    
    fieldnames = ["Прізвище", "Ім’я", "По батькові", "Стать", "Дата народження", 
                  "Посада", "Місто проживання", "Адреса проживання", "Телефон", "Email"]
    
    filename = "employees.csv"
    
    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(employees_data)
        
    print(f"Успішно згенеровано 500 записів та збережено у файл '{filename}'.")

if __name__ == "__main__":
    main()