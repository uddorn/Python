arr = [5, 3, -6, 5, 0, 3, 1, -4, 13, 9, 0, 6, 18, 4, 4, -1, 1, 12, 10, 9, 1, 7, 7, 11, 12, 16, 23, 9, 7, 3, 4, 1, 8, -2]

print(f"Масив {len(arr)} елементів:")

formatted_arr = []
for num in arr:
    if num % 2 == 0:
        formatted_arr.append(f"\033[34m{num}*\033[0m")
    else:
        formatted_arr.append(str(num))

print(" ".join(formatted_arr))

try:
    p = int(input("Введіть ціле число p: "))
except ValueError:
    p = 4
    print(f"Некоректне введення. Використано значення за замовчуванням p = {p}")

count = 0
for num in arr:
    if num % 2 == 0 and num > p:
        count += 1

print(f"Кількість парних елементів більша {p}: {count}")