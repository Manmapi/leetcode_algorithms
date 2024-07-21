class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(edges, k):
            adj = [[] for _ in range(k)]
            for edge in edges:
                adj[edge[0]].append(edge[1])
            indegree = [0] * k
            for i in range(k):
                for a in adj[i]:
                    indegree[a] = indegree[a] + 1 
            list_source = []
            for i in range(k):
                if indegree[i] == 0:
                    list_source.append(i)
            result = []
            while list_source:
                source = list_source.pop(0)
                result.append(source)
                adj_points = adj[source]
                for adj_point in adj_points:
                    indegree[adj_point] = indegree[adj_point] - 1
                    if indegree[adj_point] == 0:
                        list_source.append(adj_point)
            if len(result) != k:
                return []
            return result 
                    
        for row in rowConditions:
            row[0], row[1] = row[0] - 1, row[1] -1
        for col in colConditions:
            col[0], col[1] = col[0] - 1, col[1] -1
        topo_row = topo_sort(rowConditions, k)
        topo_row = [x + 1 for x in topo_row]
        topo_col = topo_sort(colConditions, k)
        topo_col = [x + 1 for x in topo_col]
        if not topo_row or not topo_col:
            return []
        row_index = dict()
        for i in range(k):
            row_index[topo_row[i]] = i
        col_index = dict()
        for i in range(k):
            col_index[topo_col[i]] = i
        result = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            result[row_index[i]][col_index[i]] = i
        return result
