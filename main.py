# Створено за допомогою ChatGPT v4
import random
import string

# Целевая фраза
target = "methinks it is like a weasel"

# Функция для генерации случайной строки
def generate_random_string(length):
    characters = string.ascii_lowercase + ' '
    return ''.join(random.choice(characters) for _ in range(length))

# Функция для оценки строки
def evaluate_string(test_string):
    return sum(t == h for t, h in zip(target, test_string))

# Функция для мутации строки
def mutate_string(best_string):
    mutation_chance = 0.01  # Вероятность мутации для каждого символа
    mutated_string = ''
    for char in best_string:
        if random.random() < mutation_chance:
            mutated_string += random.choice(string.ascii_lowercase + ' ')
        else:
            mutated_string += char
    return mutated_string

# Главная функция симуляции
def run_simulation():
    best_string = generate_random_string(len(target))
    best_score = evaluate_string(best_string)

    attempts = 0
    while best_score < len(target):
        attempts += 1
        new_string = mutate_string(best_string)
        new_score = evaluate_string(new_string)

        if new_score > best_score:
            best_string = new_string
            best_score = new_score

        if attempts % 1000 == 0:
            print(f"Attempt: {attempts}, Best String: '{best_string}', Score: {best_score}/{len(target)}")

    print(f"Target reached! String: '{best_string}', Attempts: {attempts}")

# Запуск симуляции


if __name__ == "__main__":
   run_simulation()
   