import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def calculate_age(birthdate):
    """Рахує повні роки від дати народження до сьогоднішнього дня."""
    today = datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

def get_age_category(age):
    """Визначає вікову категорію."""
    if age < 18:
        return 'younger_18'
    elif 18 <= age <= 45:
        return '18-45'
    elif 45 < age <= 70:
        return '45-70'
    else:
        return 'older_70'

def main():
    print("Запуск аналізатора даних...\n")

    try:
        df = pd.read_csv("employees.csv", encoding='utf-8')
        print("Ok (Файл успішно відкрито)\n")
    except Exception as e:
        print("Повідомлення про відсутність, або проблеми при відкритті файлу CSV.")
        return

    df['Дата народження'] = pd.to_datetime(df['Дата народження'])
    
    df['Вік'] = df['Дата народження'].apply(calculate_age)
    df['Категорія'] = df['Вік'].apply(get_age_category)

    plt.style.use('ggplot')

    gender_counts = df['Стать'].value_counts()
    print("--- Розподіл за статтю ---")
    print(gender_counts.to_string())
    print("-" * 30)
    
    plt.figure(figsize=(8, 6))
    gender_counts.plot(kind='pie', autopct='%1.1f%%', colors=['#66b3ff', '#ff9999'], startangle=90)
    plt.title('Розподіл співробітників за статтю')
    plt.ylabel('') 
    plt.savefig('chart_1_gender.png') 
    plt.close()

    category_counts = df['Категорія'].value_counts()
    print("\n--- Розподіл за віковими категоріями ---")
    print(category_counts.to_string())
    print("-" * 30)

    plt.figure(figsize=(8, 6))
    category_counts.plot(kind='bar', color='#99ff99')
    plt.title('Розподіл співробітників за віковими категоріями')
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість співробітників')
    plt.xticks(rotation=0)
    plt.savefig('chart_2_categories.png')
    plt.close()

    gender_cat_counts = df.groupby(['Категорія', 'Стать']).size().unstack(fill_value=0)
    print("\n--- Розподіл за статтю в кожній категорії ---")
    print(gender_cat_counts.to_string())
    print("-" * 30)

    plt.figure(figsize=(10, 6))
    gender_cat_counts.plot(kind='bar', stacked=False, color=['#ff9999', '#66b3ff'])
    plt.title('Розподіл за статтю у вікових категоріях')
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість співробітників')
    plt.xticks(rotation=0)
    plt.legend(title='Стать')
    plt.tight_layout()
    plt.savefig('chart_3_gender_categories.png')
    plt.close()

    print("\nАналіз завершено! Графіки успішно збережено у вигляді картинок (.png).")

if __name__ == "__main__":
    main()