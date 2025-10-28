def solve(test_cases):
    results = []
    for n in test_cases:
        ops = []
        for i in range(2, n + 1):
            if i <= n:
                ops.append((i, i, n))     # Reverse from i to n
                ops.append((i, 1, n))     # Reverse the entire row
        results.append(ops)
    return results

# Read input and run
t = int(input())
test_cases = [int(input()) for _ in range(t)]
solutions = solve(test_cases)

for ops in solutions:
    print(len(ops))
    for op in ops:
        print(*op)
