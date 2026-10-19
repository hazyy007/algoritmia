import random
from typing import List, Tuple







#II.B.1
def generate_activities(n: int, seed: int = 42) -> List[Tuple[str, int, int]]:
    random.seed(seed)
    activities = []

    for i in range(n):
        identifier = f"A{i}"
        start = random.randint(0, 10000)
        duration =random.randint(1,100)
        end = start + duration
        activities.append(identifier, start, end)

    return activities