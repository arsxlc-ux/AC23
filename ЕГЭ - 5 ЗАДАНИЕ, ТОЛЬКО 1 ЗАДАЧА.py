#ЕГЭ
import heapq
def dijkstra(graph, src):
    dist = {v: float('inf') for v in graph}; dist[src] = 0
    priori = [(0, src)]
    while priori:
        d, u = heapq.heappop(priori)
        if d > dist[u]: continue
        for v, w in graph[u]:
            alt = d + w
            if alt < dist[v]:
                dist[v] = alt
                heapq.heappush(priori, (alt, v))
    return dist
data = """5 4 5 1
1 2 3 4 5
1 2 1
2 3 10
3 4 100
4 5 100"""
lines = data.strip().split("\n")
N, M, K, cap = map(int, lines[0].split())
cities = set(map(int, lines[1].split()))
graph = {i: [] for i in range(1, N + 1)}
for u, v, w in map(lambda x: map(int, x.split()), lines[2:]):
    graph[u].append((v, w)); graph[v].append((u, w))
dist = dijkstra(graph, cap)
print(*sorted((c, dist[c]) for c in cities))
