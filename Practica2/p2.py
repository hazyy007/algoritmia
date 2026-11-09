import random
from typing import List, Tuple, Optional, Dict


# I.A.1
def greedy_change(coins : list[int], amount:int) ->tuple[list[int],int]:
    solu=[]
    coins = sorted(coins, reverse=True)
    for i in range(len(coins)):
        while amount >= coins[i]:
            amount=amount-coins[i]
            solu.append(coins[i])
    return solu,amount


# I.B.1
def optimal_change(coins: List[int], amount: int) -> List[int] | None:
    if amount == 0:
        return []
    if amount < 0 or not coins:
        return None
        
    sorted_coins = sorted(coins, reverse=True)
    dp: List[Optional[List[int]]] = [None] * (amount + 1)
    dp[0] = []
    
    for a in range(1, amount + 1):
        best_comb: Optional[List[int]] = None
        for c in sorted_coins:
            if a >= c and dp[a - c] is not None:
                cand = sorted(dp[a - c] + [c], reverse=True)
                if best_comb is None:
                    best_comb = cand
                else:
                    if len(cand) < len(best_comb) or (len(cand) == len(best_comb) and cand > best_comb):
                        best_comb = cand
        dp[a] = best_comb
        
    return dp[amount]


# I.C.1
def compare_change(coins: List[int], max_amount: int) -> Dict[str, List[int]]:
    result: Dict[str, List[int]] = {
        "optimal": [],
        "suboptimal": [],
        "greedy_failed": [],
        "impossible": []
    }
    
    if max_amount < 1:
        return result

    sorted_coins = sorted(coins, reverse=True)
    dp: List[Optional[List[int]]] = [None] * (max_amount + 1)
    dp[0] = []
    
    for a in range(1, max_amount + 1):
        best_comb: Optional[List[int]] = None
        for c in sorted_coins:
            if a >= c and dp[a - c] is not None:
                cand = sorted(dp[a - c] + [c], reverse=True)
                if best_comb is None or len(cand) < len(best_comb) or (len(cand) == len(best_comb) and cand > best_comb):
                    best_comb = cand
        dp[a] = best_comb

    for a in range(1, max_amount + 1):
        g_selected, g_rem = greedy_change(coins, a)
        opt_selected = dp[a]
        
        if opt_selected is None:
            result["impossible"].append(a)
        elif g_rem != 0:
            result["greedy_failed"].append(a)
        elif len(g_selected) == len(opt_selected):
            result["optimal"].append(a)
        else:
            result["suboptimal"].append(a)
            
    return result


# II.A.1
def activity_selection(activities: List[Tuple[str, int, int]]) -> List[Tuple[str, int, int]]:
    sorted_activities = sorted(activities, key=lambda x: (x[2], x[1], x[0]))
    selected_activities = []
    last_ended_time = 0
    for activity in sorted_activities:
        start_time = activity[1]
        if start_time >= last_ended_time:
            selected_activities.append(activity)
            last_ended_time = activity[2]
    return selected_activities


# II.B.1
def generate_activities(n: int, seed: int = 42) -> List[Tuple[str, int, int]]:
    random.seed(seed)
    activities = []
    for i in range(n):
        identifier = f"A{i}"
        start = random.randint(0, 10000)
        duration = random.randint(1, 100)
        end = start + duration
        activities.append((identifier, start, end))
    return activities

# III.A.1
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


# III.B.1
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
