import re

def custom_sort_key(word):
    word_lower = word.lower()
    
    is_ukrainian = any('а' <= char <= 'я' or char in 'ієїґ' for char in word_lower)
    
    return (0 if is_ukrainian else 1, word_lower)

def main():
    with open('text.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        
    print("Початковий текст")
    print(text)
    
    words = re.findall(r'\b[A-Za-zА-Яа-яІіЄєЇїҐґ]+\b', text)
    
    sorted_words = sorted(words, key=custom_sort_key)
    
    print("\n Відсортовані слова")
    print(sorted_words)

if __name__ == "__main__":
    main()
