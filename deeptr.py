from my_trans_pack import module3, NAME, AUTHOR

def main():
    print(f"Пакет: {NAME}")
    print(f"Автор: {AUTHOR}")
    
    text = "Хуцпізм - надзвичайна зухвалість, нахабство або безсоромність, часто поєднану з упевненістю у власній правоті."
    
    print("\nДемонстрація deep-translator")
    sl_trans = module3.TransLate(text, 'auto', 'sl')
    print(f"Оригінал:      {text}")
    print(f"Переклад (sl): {sl_trans}")
    
    print("\nДемонстрація langdetect")
    print(f"Результат:     {module3.LangDetect(text, 'all')}")
    
    print("\nДемонстрація CodeLang")
    print(f"Код для 'slovenian': {module3.CodeLang('slovenian')}")
    print(f"Назва для 'sl':      {module3.CodeLang('sl')}")

    print("\nДемонстрація LanguageList")
    module3.LanguageList("screen", "Привіт")

if __name__ == "__main__":
    main()