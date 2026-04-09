import re

UKR_ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

def custom_sort_key(word):
    word_lower = word.lower()
    
    is_ukrainian = any('а' <= char <= 'я' or char in 'ієїґ' for char in word_lower)
    
    char_indexes = []
    for char in word_lower:
        if char in UKR_ALPHABET:
            char_indexes.append(UKR_ALPHABET.find(char))
        else:
            char_indexes.append(ord(char))

    starts_with_lower = word[0].islower()

    return (0 if is_ukrainian else 1, starts_with_lower, char_indexes, word)

def main():
    with open('text.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        
    print("--- Початковий текст ---")
    print(text)
    
    words = re.findall(r'\b[A-Za-zА-Яа-яІіЄєЇїҐґ]+\b', text)
    
    sorted_words = sorted(words, key=custom_sort_key)
    
    print("\n--- Відсортовані слова ---")
    print(sorted_words)

if __name__ == "__main__":
    main()