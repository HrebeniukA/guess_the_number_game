import random

# Параметри гри
secret_number = random.randint(1, 100)
max_attempts = 7
attempt = 0

print("Вітаю! Я загадав число від 1 до 100. Спробуйте вгадати його за 7 спроб.")

# Головний цикл
while attempt < max_attempts:
    try:
        guess = int(input("Введіть ваше припущення: "))
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        continue

    if guess < 1 or guess > 100:
        print("Число має бути від 1 до 100. Спробуйте ще раз.")
        continue

    attempt += 1

    if guess < secret_number:
        print("Занадто маленьке!")
    elif guess > secret_number:
        print("Занадто велике!")
    else:
        print(f"Ви вгадали! Це число {secret_number}.")
        break
else:
    print(f"Ви використали всі спроби. Загадане число було: {secret_number}.")
