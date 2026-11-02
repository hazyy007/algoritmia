import random
from typing import List, Tuple, Optional


#II.A.1
def activity_selection(activities: List[Tuple[str, int, int]]) -> List[Tuple[str, int, int]]:
    sorted_activites = sorted(activities, key=lambda x: (x[2], x[1], x[0]))

    selected_activities = []
    last_ended_time = 0

    for activity in sorted_activites:
        start_time = activity[1]


        if start_time >= last_ended_time:
            selected_activities.append(activity)
            last_ended_time = activity[2]

    return selected_activities




#II.B.1
def generate_activities(n: int, seed: int = 42) -> List[Tuple[str, int, int]]:
    random.seed(seed)
    activities = []

    for i in range(n):
        identifier = f"A{i}"
        start = random.randint(0, 10000)
        duration =random.randint(1,100)
        end = start + duration
        activities.append((identifier, start, end))
    return activities



#III.A.1
def job_scheduling(jobs: List[Tuple[str, int, int]]) -> Tuple[List[Optional[Tuple[str, int, int]]], int]:
    if not jobs:
        return [], 0
    
    max_deadline = max(job[2] for job in jobs)
    
    sorted_jobs = sorted(jobs, key=lambda x: (-x[1], x[2], x[0]))
    schedule: List[Optional[Tuple[str, int, int]]] = [None] * max_deadline
    total_profit = 0
    
    for job in sorted_jobs:
        profit = job[1]
        deadline = job[2]
        for i in range(min(deadline, max_deadline) - 1, -1, -1):
            if schedule[i] is None:
                schedule[i] = job
                total_profit += profit
                break
                
    return schedule, total_profit

#III.B.1
def generate_jobs(n: int, seed: int = 42) -> List[Tuple[str, int, int]]:
    random.seed(seed)
    jobs = []


    max_deadline = max(1, n // 10)

    for i in range(n):
        identifier = f"J{i}"


        profit = random.randint(1, 1000)

        deadline = random.randint(1, max_deadline)

        jobs.append((identifier, profit, deadline))

    return jobs

def greedy_change(coins : list[int], amount:int) ->tuple[list[int],int]:
    solu=[]
    coins = sorted(coins, reverse=True)
    for i in range(len(coins)):
        while amount >= coins[i]:
            amount=amount-coins[i]
            solu.append(coins[i])
    return solu,amount


def optimal_change(coins: list[int], amount: int) -> list[int] | None:
    if amount == 0:
        return []
    coins = sorted(coins, reverse=True)
    dp = [None] * (amount + 1)
    dp[0] = 0                                  

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i-coin] is not None:
                if dp[i] is None or dp[i-coin] + 1 < dp[i]:
                    dp[i] = dp[i-coin] + 1

    if dp[amount] is None:
        return None

    solu = []
    i = amount
    while i > 0:
        for coin in coins:
            if i >= coin and dp[i-coin] is not None and dp[i-coin] == dp[i] - 1:
                solu.append(coin)
                i = i - coin
                break

    return solu