from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs

langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
codes_dict = {v: k for k, v in langs_dict.items()}

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translator = GoogleTranslator(source=scr, target=dest)
        return translator.translate(text)
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        if set == "lang":
            return detect(text)
        elif set == "confidence":
            langs = detect_langs(text)
            return str(round(langs[0].prob, 4))
        else:
            langs = detect_langs(text)
            return f"Language: {langs[0].lang}, Confidence: {round(langs[0].prob, 4)}"
    except Exception as e:
        return f"Помилка визначення: {e}"

def CodeLang(lang: str) -> str:
    try:
        lang_lower = lang.lower()
        if lang_lower in langs_dict:
            return langs_dict[lang_lower]
        if lang_lower in codes_dict:
            return codes_dict[lang_lower].capitalize()
        return "Помилка: мову не знайдено."
    except Exception as e:
        return f"Помилка: {e}"

def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        headers = ["N", "Language", "ISO-639 code", "Text"]
        rows = []
        for i, (name, code) in enumerate(list(langs_dict.items())[:10], 1):
            translated = ""
            if text:
                try:
                    translated = GoogleTranslator(source='auto', target=code).translate(text)
                except:
                    translated = "Помилка"
            rows.append([str(i), name.capitalize(), code, translated])
            
        output_str = f"{headers[0]:<5} {headers[1]:<20} {headers[2]:<15} {headers[3]}\n"
        output_str += "-" * 70 + "\n"
        for row in rows:
            output_str += f"{row[0]:<5} {row[1]:<20} {row[2]:<15} {row[3]}\n"

        if out == "screen":
            print(output_str)
        elif out == "file":
            with open("languages_list_mod3.txt", "w", encoding="utf-8") as f:
                f.write(output_str)
        return "Ok"
    except Exception as e:
        return f"Помилка виводу: {e}"
