import heapq

def kruskal(graph, R):
    mst = []
    edges = [(c, v, w) for v in range(R) for w, c in graph[v]]
    edges.sort()

    parent = list(range(R))
    rank = [0] * R

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(v, w):
        root1 = find(v)
        root2 = find(w)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                root1, root2 = root2, root1
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1
            return True
        return False

    for c, v, w in edges:
        if union(v, w):
            mst.append((v, w, c))

    return sum(c for v, w, c in mst)

def main():
    R, C = map(int, input().split())
    graph = [[] for _ in range(R)]
    for _ in range(C):
        v, w, c = map(int, input().split())
        v -= 1
        w -= 1
        graph[v].append((c, w))
        graph[w].append((c, v))
    print(kruskal(graph, R))

if __name__ == '__main__':
    main()


