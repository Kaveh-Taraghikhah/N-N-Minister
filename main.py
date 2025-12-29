import random

MOVES = ['U', 'D', 'L', 'R']

def move(pos, action, n):
    x, y = pos
    if action == 'U' and x > 0: x -= 1
    if action == 'D' and x < n - 1: x += 1
    if action == 'L' and y > 0: y -= 1
    if action == 'R' and y < n - 1: y += 1
    return (x, y)

def simulate(path, n):
    pos = (0, 0)
    for m in path:
        pos = move(pos, m, n)
    return pos

def fitness(path, n):
    end = simulate(path, n)
    goal = (n - 1, n - 1)
    dist = abs(end[0] - goal[0]) + abs(end[1] - goal[1])
    return -dist 

def genetic_algorithm(n):
    population_size = 20
    generations = 30

    population = [
        [random.choice(MOVES) for _ in range(n)]
        for _ in range(population_size)
    ]

    for g in range(generations):
        population.sort(key=lambda p: fitness(p, n), reverse=True)

        best = population[0]
        print(f"Generation {g}: best path = {best}, fitness = {fitness(best, n)}")

        if simulate(best, n) == (n - 1, n - 1):
            print("\nSUCCESSFUL PATH FOUND!")
            print(best)
            return

        new_population = population[:5]
        while len(new_population) < population_size:
            parent = random.choice(population[:10])
            child = parent[:]
            idx = random.randint(0, n - 1)
            child[idx] = random.choice(MOVES)
            new_population.append(child)

        population = new_population

    print("\nFinished generations.")
    print("Best path found:", population[0])

n = 5
genetic_algorithm(n)
