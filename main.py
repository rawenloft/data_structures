import random
import string

# Constants
TARGET = "methinks it is like a weasel"
CHARACTERS = string.ascii_lowercase + ' '
MUTATION_CHANCE = 0.01  # You might adjust this for faster convergence

def generate_random_string(length):
    """Generate a random string of a given length."""
    return ''.join(random.choice(CHARACTERS) for _ in range(length))

def evaluate_string(test_string):
    """Evaluate how similar the test string is to the target string."""
    return sum(t == h for t, h in zip(TARGET, test_string))

def mutate_string(best_string):
    """Mutate the best string by changing only the incorrect characters."""
    mutated = list(best_string)  # Convert to list for easier manipulation
    for i, (char_from_best, char_from_target) in enumerate(zip(best_string, TARGET)):
        if char_from_best != char_from_target and random.random() < MUTATION_CHANCE:
            mutated[i] = random.choice(CHARACTERS)
    return ''.join(mutated)

def run_simulation(print_frequency=1000):
    """Run the simulation to evolve a string to match the target."""
    best_string = generate_random_string(len(TARGET))
    best_score = evaluate_string(best_string)

    attempts = 0
    while best_score < len(TARGET):
        attempts += 1
        new_string = mutate_string(best_string)
        new_score = evaluate_string(new_string)

        if new_score > best_score:
            best_string = new_string
            best_score = new_score

        if attempts % print_frequency == 0:
            print(f"Attempt: {attempts}, Best String: '{best_string}', Score: {best_score}/{len(TARGET)}")

    print(f"Target reached! String: '{best_string}', Attempts: {attempts}")

if __name__ == "__main__":
    run_simulation()
