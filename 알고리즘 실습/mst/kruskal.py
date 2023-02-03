# # Kruskal's Algorithm

# # v: vertex의 개수, e: edge의 개수
# v, e = map(int, input().split())

# # 부모 테이블 초기화
# parent = [0] * (v + 1)
# for i in range(1, v+1):
#     parent[i] = i

# # 탐색 연산
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# # 합집합 연산
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# edges = []
# total_cost = 0

# edges.sort()

# for i in range(e):
#     cost, a, b = edges[i]
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         total_cost += cost
    
# print(total_cost)

graph = [(1,2,13), (1,3,5),(2,4,9),(3,4,15), (3,5,3), (4,5,1), (4,6,7), (5,6,2)]
graph.sort(key=lambda x: x[2]) # 가중치로 엣지 정렬 (vertex1, vertex2, weight)

mst = []
n = 6
p = [0]

for i in range(1, n+1):
    p.append(i) # 각 vertex 자신이 집합이 대표

def find(u):
    if u != p[u]:
        p[u] = find(p[u])    # 경로 압축
    return p[u]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1    # root2가 root1의 부모로 설정

edges = 0   # 엣지 개수
total_cost = 0  # 가중치 합

while True:
    if edges == n-1:
        break
    u, v, wt = graph.pop(0)
    if find(u) != find(v):  # u와 v가 서로 다른 집합에 속해 있으면
        union(u, v)
        mst.append((u, v))
        total_cost += wt
        edges += 1

print("MST: ", mst)
print("MST_WEIGHT: ", total_cost)