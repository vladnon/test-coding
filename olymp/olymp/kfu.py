
from collections import defaultdict, deque


def solve_game(k, n, m, s, c, edges):
    red_edges = defaultdict(list)
    white_edges = defaultdict(list)
    reverse_red_edges = defaultdict(list)
    reverse_white_edges = defaultdict(list)

    for v, u, b in edges:
        if b == 0:
            red_edges[v].append(u)
            reverse_red_edges[u].append(v)
        else:
            white_edges[v].append(u)
            reverse_white_edges[u].append(v)

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    outdegree = [[0, 0] for _ in range(n + 1)]

    for v in range(1, n + 1):
        if c[v - 1] == 1:
            dp[v][k] = 1
        else:
            dp[v][k] = 2

    for v in range(1, n + 1):
        outdegree[v][0] = len(red_edges[v])
        outdegree[v][1] = len(white_edges[v])

    for step in range(k - 1, -1, -1):
        symbol = int(s[step])
        current_edges = reverse_red_edges if symbol == 0 else reverse_white_edges

        queue = deque()
        for v in range(1, n + 1):
            if dp[v][step + 1] == 2:
                dp[v][step] = 1
                queue.append(v)

        while queue:
            v = queue.popleft()
            for u in current_edges[v]:
                if dp[u][step] == 0:
                    outdegree[u][symbol] -= 1
                    if outdegree[u][symbol] == 0:
                        dp[u][step] = 2
                        queue.append(u)

    if dp[1][0] == 1:
        return 1
    elif dp[1][0] == 2:
        return 2
    else:
        return -1


k, n, m = map(int, input().split())
s = input().strip()
c = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(m)]

print(solve_game(k, n, m, s, c, edges))
