import urllib.parse
import pyperclip

def main():
    encoded_url = "https://uk.wikipedia.org/wiki/%D0%A8%D1%82%D1%83%D1%87%D0%BD%D0%B8%D0%B9_%D1%96%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D1%82"
    print("Декодування URL")
    print(f"Закодований URL:\n{encoded_url}\n")
    
    decoded_url = urllib.parse.unquote(encoded_url)
    print(f"Декодований URL:\n{decoded_url}\n")
    
    try:
        pyperclip.copy(decoded_url)
        print("Декодоване посилання успішно скопійовано до буфера обміну!")
    except pyperclip.PyperclipException as e:
        print(f"Не вдалося автоматично скопіювати в буфер обміну. Можливо, на вашому Linux-дистрибутиві не встановлені пакети xclip або xsel.")
        print(f"Помилка: {e}")

if __name__ == "__main__":
    main()
