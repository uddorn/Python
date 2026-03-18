import asyncio
from my_trans_pack import module1, NAME, AUTHOR

async def main():
    print(f"Пакет: {NAME}\nАвтор: {AUTHOR}\n" + "-"*30)
    
    text_to_translate = "Добрий день"
    
    print("\nДемонстрація TransLate")
    uk_to_en = await module1.TransLate(text_to_translate, "uk", "en")
    print(f"Переклад ('{text_to_translate}' -> en): {uk_to_en}")
    
    print("\nДемонстрація LangDetect")
    detect_res = await module1.LangDetect(text_to_translate, "all")
    print(f"Визначення мови: {detect_res}")
    
    print("\nДемонстрація CodeLang")
    print(f"Код для 'ukrainian': {module1.CodeLang('ukrainian')}")
    print(f"Назва для 'uk': {module1.CodeLang('uk')}")
    
    print("\nДемонстрація LanguageList")
    await module1.LanguageList("screen", "Привіт")

if __name__ == "__main__":
    asyncio.run(main())