import sys
input = sys.stdin.readline

N = int(input().rstrip())
requests = list(map(int, input().rstrip().split()))
total_budget = int(input().rstrip())

low, high = 0, max(requests)
result = 0

while low <= high:
    mid = (low + high) // 2
    current_total = sum(min(request, mid) for request in requests)

    if current_total <= total_budget:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)
