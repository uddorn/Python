import sys

if sys.version_info >= (3, 13):
    print("="*65)
    print(f"УВАГА: Поточна версія Python: {sys.version.split()[0]}")
    print("Цей модуль (module2) оптимізовано для googletrans==3.1.0a0, ")
    print("який несумісний з Python >= 3.13 (через відсутність модуля cgi).")
    print("Будь ласка, запустіть цю програму в Docker-контейнері з Python 3.12.")
    print("="*65 + "\n")

try:
    from googletrans import Translator, LANGUAGES
except ModuleNotFoundError:
    Translator = None
    LANGUAGES = {}

def TransLate(text: str, scr: str, dest: str) -> str:
    if Translator is None: return "Помилка: несумісна версія Python."
    try:
        return Translator().translate(text, src=scr, dest=dest).text
    except Exception as e: return f"Помилка: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    if Translator is None: return "Помилка: несумісна версія Python."
    try:
        res = Translator().detect(text)
        if set == "lang": return res.lang
        if set == "confidence": return str(res.confidence)
        return f"Language: {res.lang}, Confidence: {res.confidence}"
    except Exception as e: return f"Помилка: {e}"

def CodeLang(lang: str) -> str:
    if not LANGUAGES: return "Помилка: несумісна версія Python."
    try:
        lang = lang.lower()
        if lang in LANGUAGES: return LANGUAGES[lang].capitalize()
        for c, n in LANGUAGES.items():
            if n.lower() == lang: return c
        return "Не знайдено."
    except Exception as e: return f"Помилка: {e}"

def LanguageList(out: str = "screen", text: str = "") -> str:
    if not LANGUAGES: return "Помилка: несумісна версія Python."
    return "Ok"
