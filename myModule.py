from deep_translator import GoogleTranslator

def check_pythagoras(a, b, c):
    sides = sorted([a, b, c])
    cathetus1, cathetus2, hypotenuse = sides[0], sides[1], sides[2]
    
    is_pythagorean = (cathetus1**2 + cathetus2**2 == hypotenuse**2)
    return is_pythagorean, cathetus1, cathetus2, hypotenuse

def translate_text(text, target_lang):
    if target_lang == 'uk':
        return text
    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return translated
    except Exception:
        return text 