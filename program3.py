import json

def main():
    students_data = {
        "Алексеєвич": ["Дмитро", "Романович", 2006],
        "Босенко": ["Христина", "Ростиславівна", 2006],
        "Бурмака": ["Ігор", "Олександрович", 2006],
        "Голуб": ["Олександр", "Андрійович", 2006],
        "Діброва": ["Андрій", "Сергійович", 2006],
        "Карпенко": ["Роман", "Васильович", 2006],
        "Коваленко": ["Сергій", "Миколайович", 2006],
        "Крамаренко": ["Владислав", "Вікторович", 2005],
        "Печкур": ["Максим", "Миколайович", 2006],
        "Підгорний": ["Олександр", "Сергійович", 2006]
    }
    
    filename = "students.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(students_data, f, ensure_ascii=False, indent=4)
        
    print(f"Дані успішно збережено у файл {filename}")
    print("\n Прочитані дані з файлу")
    with open(filename, 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
        
        for surname, details in loaded_data.items():
            print(f"Прізвище: {surname}, Ім'я: {details[0]}, По батькові: {details[1]}, Рік народження: {details[2]}")

if __name__ == "__main__":
    main()
