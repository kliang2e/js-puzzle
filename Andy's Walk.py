import random

GENS = [(1, 0), (0, 1), (-1, -1)]

def run_one_walk():
    a, b = 0, 0
    step = 0
    while True:
        step += 1
        sign = 1 if step % 2 == 1 else -1
        ea, eb = random.choice(GENS)
        a, b = a + sign * ea, b + sign * eb
        if a % 2 == 0 and b % 2 == 0:
            return (a, b) == (0, 0)
        
N = 2000000
discovered = sum(not run_one_walk() for _ in range(N))
print (f"p (discovered) ~ {discovered / N:.4f}")