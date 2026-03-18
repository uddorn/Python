from my_trans_pack import module2, NAME, AUTHOR

def main():
    print(f"Пакет: {NAME}\nАвтор: {AUTHOR}\n" + "-"*30)
    
    text_to_translate = "Привіт світ!"
    
    print("\n--- Демонстрація TransLate (Module 2) ---")
    uk_to_en = module2.TransLate(text_to_translate, "uk", "en")
    print(f"Переклад ('{text_to_translate}' -> en): {uk_to_en}")
    
    print("\n--- Демонстрація LangDetect (Module 2) ---")
    print(f"Визначення: {module2.LangDetect(text_to_translate, 'all')}")

if __name__ == "__main__":
    main()
