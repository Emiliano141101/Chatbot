import random
import tkinter as tk

TARGET_STRING = "HELLO WORLD"
POPULATION_SIZE = 20
GENERATIONS = 10
MUTATION_RATE = 0.1

def generate_random_string(length):
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ ') for _ in range(length))

def calculate_fitness(string):
    return sum(1 for a, b in zip(string, TARGET_STRING) if a == b)

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(string):
    mutated_string = ""
    for char in string:
        if random.random() < MUTATION_RATE:
            mutated_string += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
        else:
            mutated_string += char
    return mutated_string

def genetic_algorithm():
    population = [generate_random_string(len(TARGET_STRING)) for _ in range(POPULATION_SIZE)]

    root = tk.Tk()
    root.title("Genetic Algorithm - Hello World")

    text_area = tk.Text(root, height=15, width=50)
    text_area.pack()

    for generation in range(GENERATIONS):
        text_area.insert(tk.END, f"Generation {generation + 1}:\n")
        for individual in population:
            fitness = calculate_fitness(individual)
            text_area.insert(tk.END, f"    {individual}  Fitness: {fitness}\n")

            if individual == TARGET_STRING:
                text_area.insert(tk.END, "¡Cadena objetivo encontrada!\n")
                root.mainloop()
                return

        selected_parents = []
        for _ in range(POPULATION_SIZE // 2):
            tournament = random.sample(population, 5)
            selected_parents.append(max(tournament, key=calculate_fitness))

        new_population = []
        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = random.sample(selected_parents, 2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])

        population = new_population

        root.update()
        root.after(1000) 

    root.mainloop()

if __name__ == "__main__":
    genetic_algorithm()
