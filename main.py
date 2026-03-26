import json
import os
from myModule import check_pythagoras, translate_text

DATA_FILE = "MyData.json"

def main():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            a, b, c = data['a'], data['b'], data['c']
            lang = data.get('lang', 'uk')
            
            if not isinstance(lang, str) or not lang.isalpha():
                lang = 'uk'

            lang_name_uk = "Українська" if lang == 'uk' else lang
            msg_lang = f"Мова: {lang_name_uk}"
            msg_input = f"Три цілих числа a, b, c: {a} {b} {c}"
            
            is_pyth, c1, c2, hyp = check_pythagoras(a, b, c)
            
            if is_pyth:
                msg_result = f"Числа {a}, {b}, {c}, являються трійкою Піфагора. Так як {c1}^2+{c2}^2={hyp}^2 ({c1**2}+{c2**2}={hyp**2})."
            else:
                msg_result = f"Числа {a}, {b}, {c}, не являються трійкою Піфагора."

            if lang != 'uk':
                msg_lang = translate_text(msg_lang, lang)
                msg_input = translate_text(msg_input, lang)
                msg_result = translate_text(msg_result, lang)

            print(msg_lang)
            print(msg_input)
            print(msg_result)
            return 
            
        except (json.JSONDecodeError, KeyError, ValueError):
            pass 

    try:
        input_str = input("Введіть три цілих числа a, b, c: ")
        a_str, b_str, c_str = input_str.split()
        a, b, c = int(a_str), int(b_str), int(c_str)
    except ValueError:
        print("Помилка вводу. Потрібно ввести три цілих числа через пробіл.")
        return

    lang_input = input("Введіть мову інтерфейсу: ").strip().lower()

    data_to_save = {
        "a": a,
        "b": b,
        "c": c,
        "lang": lang_input
    }

    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)
    
    print(f"Дані збережено в файл {DATA_FILE}")

if __name__ == "__main__":
    main()