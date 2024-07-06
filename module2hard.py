while True:
    n = int(input("Введите число от 3 до 20 или введите '0', если ловушка открылась: "))
    def find_pairs_for_number(n):
        pairs = []
        for i in range(1, 21):
            for j in range(i + 1, 21):
                if n % (i + j) == 0:
                    pairs.append((i, j))
        return pairs


    def format_pairs(pairs):
        return ' '.join([f'{a}, {b} |' for a, b in pairs])


    if 3 <= n <= 20:
        pairs = find_pairs_for_number(n)
        if pairs:
            result = format_pairs(pairs)
            print(f"Пароль к числу {n}: {result}")

    if n == 0:
        print("Поздравляю, вы живы! :) ")
        break

    if n < 3 or n > 20:
            print('Неверное число, попробуйте еще раз')





