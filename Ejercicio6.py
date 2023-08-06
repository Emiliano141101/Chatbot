import numpy as np
import random
import matplotlib.pyplot as plt

num_agents = 10
num_food_sources = 10
grid_size = 10
max_steps = 100

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)])
        self.x = (self.x + dx) % grid_size
        self.y = (self.y + dy) % grid_size

    def calculate_distance(self, x, y):
        return np.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

class FoodSource:
    def __init__(self, x, y):
        self.x = x
        self.y = y

agents = [Agent(random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)) for _ in range(num_agents)]
food_sources = [FoodSource(random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)) for _ in range(num_food_sources)]

def draw_simulation():
    plt.clf()
    plt.xlim(0, grid_size)
    plt.ylim(0, grid_size)

    for food in food_sources:
        plt.plot(food.x, food.y, 'go', markersize=10)

    for agent in agents:
        plt.plot(agent.x, agent.y, 'bo')

    plt.pause(0.1)

plt.ion() 

for step in range(max_steps):
    for agent in agents:
        if len(food_sources) > 0:
            closest_food = min(food_sources, key=lambda food: agent.calculate_distance(food.x, food.y))
            agent.move()

            if (agent.x, agent.y) == (closest_food.x, closest_food.y):
                food_sources.remove(closest_food)

    food_coords = [(food.x, food.y) for food in food_sources]
    for agent in agents:
        agent_coords = (agent.x, agent.y)
        for food_coord in food_coords:
            distance_to_food = agent.calculate_distance(food_coord[0], food_coord[1])
            sharing_probability = 1 / (distance_to_food + 0.1) 
            if random.random() < sharing_probability:
                agent.x, agent.y = food_coord

    draw_simulation()

plt.ioff()  
plt.show()  
