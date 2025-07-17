def getMinimumCost(k, c):
        total_cost = 0
        c.sort(reverse=True)
        for i in range(len(c)):
            multiplier = i // k + 1  
            total_cost += multiplier * c[i]
        return total_cost
if __name__ == '__main__':
    nk = input("enter space sperated values for N , K: ").split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input("enter space seperated cost of flowers: ").rstrip().split()))
    minimumCost = getMinimumCost(k, c)
    print(f"Minimum Cost = {minimumCost}")
