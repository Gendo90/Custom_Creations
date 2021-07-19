from collections import defaultdict

# try cutting the leaves off the tree and keep track of how many cuts are made
# before all nodes are completely disconnected
# n is the number of nodes in the tree
# tree is given as an array of pairs of vertices (not validated as a tree here)
# like tree = [[2, 5], [5, 7], [5, 1], [1, 9], [1, 0], [7, 6], [6, 3], [3, 8], [8, 4]]
# but can be modified so it just takes an adjacency list
def treeDiameter(n, tree):
        # edge cases
    if(n==1):
        return 0
    elif(n==2):
        return 1

    # need to start at one of the border nodes/leaves (only one connection to other nodes)
    graph_map = defaultdict(list)
    freq_map = defaultdict(int)

    for first, second in tree:
        graph_map[first].append(second)
        graph_map[second].append(first)

        freq_map[first] += 1
        freq_map[second] += 1

    #core tree
    core_tree = set(range(n))
    #get all leaves
    leaves = [a for a in range(n) if freq_map[a] == 1]
    total_dist = 0

    while(len(core_tree) > 1):
        if(len(core_tree) == 2):
            total_dist += 1
            break

        graph_map, freq_map, leaves, core_tree = cutTree(graph_map, freq_map, core_tree, leaves)

        total_dist += 2

        # print(graph_map, core_tree, total_dist, leaves)


    return total_dist


def cutTree(graph_map, freq_map, core_tree, leaves):
    new_leaves = []

    for leaf in leaves:
        core_tree.discard(leaf)
        freq_map[leaf] -= 1
        if(len(graph_map[leaf]) == 1):
            new_possible_leaf = graph_map[leaf][0]
            graph_map[new_possible_leaf].remove(leaf)
            freq_map[new_possible_leaf] -= 1
        graph_map[leaf].pop()

        if(freq_map[new_possible_leaf] == 1):
            new_leaves.append(new_possible_leaf)

    return (graph_map, freq_map, new_leaves, core_tree)


def treeDiameterSlow(n, tree):
    # edge case
    if(n==1):
        return 0

    # need to start at one of the border nodes/leaves (only one connection to other nodes)
    graph_map = defaultdict(list)
    freq_map = defaultdict(int)

    for first, second in tree:
        graph_map[first].append(second)
        graph_map[second].append(first)

        freq_map[first] += 1
        freq_map[second] += 1

    #get all leaves
    leaves = [a for a in range(n) if freq_map[a] == 1]
    seen_dist = set()

    for leaf in leaves:
        all_dist = getEdgeDist(leaf, graph_map)
        seen_dist = seen_dist.union(all_dist)

    return max(seen_dist)




#setup BFS counting levels
def getEdgeDist(node, graph_map):
    queue = [[0, node]]
    seen = set()
    seen.add(node)
    distances = set()

    while(len(queue) > 0):
        curr_node = queue.pop(0)
        count_edges = 0

        for node in graph_map[curr_node[1]]:
            count_edges += 1
            if(node not in seen):
                seen.add(node)
                queue.append([curr_node[0]+1, node])
        else:
            if(count_edges == 1):
                distances.add(curr_node[0])

    return distances
