from googletrans import Translator, LANGUAGES

def TransLate(text, lang):
    t = Translator()
    dest = lang.lower()
    for c, n in LANGUAGES.items():
        if n.lower() == dest:
            dest = c
            break
    res = t.translate(text, dest=dest)
    return res.text

def LangDetect(txt):
    t = Translator()
    d = t.detect(txt)
    return "Detected(lang=" + str(d.lang) + ", confidence=" + str(d.confidence) + ")"

def CodeLang(l):
    l = l.lower()
    if l in LANGUAGES:
        return LANGUAGES[l].title()
    for c, n in LANGUAGES.items():
        if n.lower() == l:
            return c
    return "error"

txt = "Доброго дня. Як справи?"
l = "en"

print(txt)
print(LangDetect(txt))
print(TransLate(txt, l))
print(CodeLang("En"))
print(CodeLang("English"))
