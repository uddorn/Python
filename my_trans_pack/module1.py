import asyncio
from googletrans import Translator, LANGUAGES

async def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        async with Translator() as translator:
            result = await translator.translate(text, src=scr, dest=dest)
            return result.text
    except Exception as e:
        return f"Помилка перекладу: {e}"

async def LangDetect(text: str, set: str = "all") -> str:
    try:
        async with Translator() as translator:
            result = await translator.detect(text)
            if set == "lang": 
                return result.lang
            if set == "confidence": 
                return str(result.confidence)
            return f"Language: {result.lang}, Confidence: {result.confidence}"
    except Exception as e:
        return f"Помилка визначення: {e}"

def CodeLang(lang: str) -> str:
    try:
        lang = lang.lower()
        if lang in LANGUAGES: 
            return LANGUAGES[lang].capitalize()
        for code, name in LANGUAGES.items():
            if name.lower() == lang: 
                return code
        return "Помилка: мову не знайдено."
    except Exception as e: 
        return f"Помилка: {e}"

async def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        headers = ["N", "Language", "ISO-639 code", "Text"]
        rows = []
        
        async with Translator() as translator:
            for i, (code, name) in enumerate(list(LANGUAGES.items())[:10], 1):
                translated_text = ""
                if text:
                    try:
                        res = await translator.translate(text, dest=code)
                        translated_text = res.text
                    except:
                        translated_text = "Помилка"
                rows.append([str(i), name.capitalize(), code, translated_text])

        output_str = f"{headers[0]:<5} {headers[1]:<20} {headers[2]:<15} {headers[3]}\n"
        output_str += "-" * 70 + "\n"
        for row in rows:
            output_str += f"{row[0]:<5} {row[1]:<20} {row[2]:<15} {row[3]}\n"

        if out == "screen": 
            print(output_str)
        elif out == "file":
            with open("languages_list_mod1.txt", "w", encoding="utf-8") as f:
                f.write(output_str)
        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"
