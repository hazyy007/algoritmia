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
def compare_change(coins: list[int], max_amount: int) -> dict[str,list[int]]:
    solu={ "optimal": [...], "suboptimal": [...], "greedy_failed": [...], "impossible": [...] }
    for i in range(1,max_amount+1):
        greedy_coins, res = greedy_change(coins, i)
        op_coins = optimal_change(coins, i)
        if optimal_change == None:
            solu["impossible"].append(i)
        else:
            if res == 0:
                if len(greedy_coins) == len(op_coins):
                    solu["optimal"].append(i)
                else:
                    solu["suboptimal"].append(i)
            else:
                solu["greedy_failed"].append(i)

    return solu