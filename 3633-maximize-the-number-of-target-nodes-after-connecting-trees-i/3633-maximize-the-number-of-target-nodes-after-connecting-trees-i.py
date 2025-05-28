class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def build_graph(edges, size):
            g = [[] for _ in range(size)]
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
            return g

        def bfs_count_nodes(graph, k_limit):
            n = len(graph)
            result = [0] * n
            for start in range(n):
                visited = [False] * n
                q = deque([(start, 0)])
                visited[start] = True
                count = 1
                while q:
                    node, dist = q.popleft()
                    if dist == k_limit: continue
                    for neig in graph[node]:
                        if not visited[neig]:
                            visited[neig] = True
                            q.append((neig, dist + 1))
                            count += 1
                result[start] = count
            return result

        n, m = len(edges1) + 1, len(edges2) + 1
        g1, g2 = build_graph(edges1, n), build_graph(edges2, m)
        if k == 0: return [1] * n

        tree1_counts = bfs_count_nodes(g1, k)
        tree2_counts = bfs_count_nodes(g2, k - 1)
        max_tree2 = max(tree2_counts)
        return [tree1_counts[i] + max_tree2 for i in range(n)]