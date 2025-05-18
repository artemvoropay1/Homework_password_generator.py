import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

while True:
    try:
        length = int(input("Введите длину пароля (от 4 до 10 символов): "))
        
        if length < 4:
            print("Слишком маленькое количество символов в пароле.")
        elif length > 10:
            print("Слишком большое количество символов в пароле.")
        else:
            passwort = ""
            for i in range(length):
                passwort += random.choice(symbols)
            print("Сгенерированный пароль:", passwort)
            break  # Выход из цикла после успешного генерации
    except ValueError:
        print("Пожалуйста, введите число.")
