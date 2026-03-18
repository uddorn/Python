import json
import os
import re
import importlib

def get_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s for s in sentences if s]

def main():
    config_path = 'config.json'
    if not os.path.exists(config_path):
        print("Помилка: файл config.json не знайдено.")
        return

    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    file_name = config.get('text_file')
    target_lang = config.get('target_language')
    mod_name = config.get('module')
    output_dest = config.get('output')
    max_sent = config.get('max_sentences')

    if not os.path.exists(file_name):
        print(f"Помилка: файл {file_name} не знайдено.")
        return

    try:
        translator_module = importlib.import_module(f"my_trans_pack.{mod_name}")
    except ModuleNotFoundError:
        print(f"Помилка: модуль {mod_name} не знайдено у пакеті my_trans_pack.")
        return

    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()

    file_size = os.path.getsize(file_name)
    char_count = len(text)
    all_sentences = get_sentences(text)
    sent_count = len(all_sentences)
    lang_detect = translator_module.LangDetect(text, 'lang')

    print(f"Статистика файлу {file_name}")
    print(f"Розмір: {file_size} байт")
    print(f"Символів: {char_count}")
    print(f"Речень: {sent_count}")
    print(f"Мова тексту: {lang_detect}")
    print("-" * 35)

    text_to_translate = " ".join(all_sentences[:max_sent])
    
    translated_text = translator_module.TransLate(text_to_translate, 'auto', target_lang)

    if output_dest == "screen":
        lang_name = translator_module.CodeLang(target_lang)
        print(f"\nМова перекладу: {lang_name} ({target_lang})")
        print(f"Використаний модуль: {mod_name}")
        print("\nПерекладений текст:")
        print(translated_text)
    
    elif output_dest == "file":
        name, ext = os.path.splitext(file_name)
        new_file_name = f"{name}_{target_lang}{ext}"
        try:
            with open(new_file_name, 'w', encoding='utf-8') as f:
                f.write(translated_text)
            print("Ok")
        except Exception as e:
            print(f"Помилка запису у файл: {e}")

if __name__ == "__main__":
    main()