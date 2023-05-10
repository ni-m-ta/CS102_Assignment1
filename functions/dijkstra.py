import sys

def dijkstra(graph, start):
    # 初期化 (スタート地点から各点の距離をinfinityにする)
    n = len(graph)
    visited = [False] * n
    distance = [sys.maxsize] * n
    distance[start] = 0

    # ダイクストラ法
    for i in range(n):
        # 未処理の中で最小の距離を持つ頂点を探す
        min_distance = sys.maxsize
        for j in range(n):
            if not visited[j] and distance[j] < min_distance:
                min_distance = distance[j]
                u = j

        # 訪問済みにする
        visited[u] = True

        # uから到達可能な頂点の距離を更新する
        for v in range(n):
            if not visited[v] and graph[u][v] != 0:
                new_distance = distance[u] + graph[u][v]
                if new_distance < distance[v]:
                    distance[v] = new_distance

    return distance
graph = [
    [0, 2, 4, 0, 0],
    [2, 0, 2, 4, 0],
    [4, 2, 0, 1, 3],
    [0, 4, 1, 0, 1],
    [0, 0, 3, 1, 0]
]
start = 0
distance = dijkstra(graph, start)
print(distance) # [0, 2, 3, 5, 6]
