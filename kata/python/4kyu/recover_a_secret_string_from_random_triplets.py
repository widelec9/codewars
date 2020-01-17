def dfs(adj_list, v, visited, stack):
    visited[v] = True
    for k in adj_list[v]:
        if not visited[k]:
            dfs(adj_list, k, visited, stack)
    stack.insert(0, v)


def recoverSecret(triplets):
    adj_list = {k: set() for k in set(sum(triplets, []))}
    for t in triplets:
        adj_list[t[0]] |= {t[1]}
        adj_list[t[1]] |= {t[2]}
    visited = {k: False for k in adj_list}
    stack = []
    for k in adj_list:
        if not visited[k]:
            dfs(adj_list, k, visited, stack)
    return ''.join(stack)
