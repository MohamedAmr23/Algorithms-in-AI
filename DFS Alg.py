graph = {
 'S' : ['B', 'D', 'A'],
 'A' : ['C'],
 'B' : ['D'],
 'C' : ['G', 'D'],
 'D' : ['G']
}
def dfs(graph,start,goal):
    visited=[]
    stack=[[start]]
    while stack:
        path=stack.pop()
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
                stack.append(new_path)
sol=dfs(graph,'S','G')
print(sol)                