def bfs (graph,start,goal):
    visited=[]
    queue=[[start]]
    while queue:
        path=queue.pop(0)
        node=path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node==goal:
            return path
        else:
            adj=graph.get(node,[])
            for node2 in adj:
                new_path=path.copy()
                new_path.append(node2)
                queue.append(new_path)
graph = {
 'S' : ['B', 'D', 'A'],
 'A' : ['C'],
 'B' : ['D'],
 'C' : ['G', 'D'],
 'D' : ['G']
}
sol=bfs(graph,'S','G') 
print(sol)               