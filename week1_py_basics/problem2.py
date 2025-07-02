def server1(n, requests):
    total = 0
    for i in range (n):
        if i % 2 == 0:
            total += requests[i]
    return total
n = int(input("enter number of requests: "))
requests = list(map(int, input("enter space seperated requests: ").split()))
print(server1(n, requests))