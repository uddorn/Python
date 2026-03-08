import asyncio
import time
from googletrans import Translator, LANGUAGES

def CodeLang(lang):
    lang = lang.lower().strip()
    for code, name in LANGUAGES.items():
        if name.lower() == lang:
            return code
    if lang in LANGUAGES:
        return LANGUAGES[lang].capitalize()
    return "Error"

def LangDetect(txt):
    try:
        t = Translator()
        res = t.detect(txt)
        return res.lang, res.confidence
    except Exception as e:
        return "Error", 0

def TransLate(str_text, lang):
    try:
        t = Translator()
        dest = CodeLang(lang)
        if dest == "Error":
            dest = lang 
            
        res = t.translate(str_text, dest=dest)
        return res.text
    except Exception as e:
        return "Error"

def main():
    file_name = "Steve_Jobs.txt"
    target_lang = "Slovenian"

    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        print("Помилка читання файлу:", e)
        return

    TxtList = text.split('.')
    TxtList = [s.strip() for s in TxtList if s.strip() != ""]
 
    start_sync = time.time()
    orig_lang, conf = LangDetect(text)
    
    sync_result = []
    for sentence in TxtList:
        sync_result.append(TransLate(sentence, target_lang))
        
    time_sync = time.time() - start_sync
    
    start_async = time.time()
    
    async def run_async():
        lang_task = asyncio.to_thread(LangDetect, text)
        
        trans_tasks = []
        for sentence in TxtList:
            trans_tasks.append(asyncio.to_thread(TransLate, sentence, target_lang))
            
        all_results = await asyncio.gather(lang_task, *trans_tasks)
        return all_results[0], all_results[1:]

    async_lang_info, async_result = asyncio.run(run_async())
    time_async = time.time() - start_async

    print(f"Ім'я файлу: {file_name}")
    print(f"Кількість символів: {len(text)}")
    print(f"Кількість речень: {len(TxtList)}")
    print(f"Мова оригіналу: {orig_lang}, confidence: {conf}")
    print(f"Оригінальний текст:\n{text}\n")
    
    print(f"Мова перекладу: {target_lang} ({CodeLang(target_lang)})")
    print("Перекладений текст:")
    print(". ".join(async_result) + ".\n")
    
    print(f"Час (синхронно): {time_sync:.4f} сек")
    print(f"Час (асинхронно): {time_async:.4f} сек")

if __name__ == "__main__":
    main()