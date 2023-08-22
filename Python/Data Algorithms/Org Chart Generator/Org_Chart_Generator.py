import random
from collections import defaultdict
# look into making Name_Generator a package/module later?
from Name_Generator import generate_name


# generate a tree, top-down, with a random number (1 to 3) of direct supervisors for each current level (1 from a previous level,
# the possible others from any higher level (e.g. mentors, relatives))
# some of the reports could be others' direct reports
# have at least 5 levels generated (4 management levels)
# CEO given as root (all_levels[0][0])
def generate_org_chart(level=5, additional_supervisors=2):
    seen_names = set()

    # make an adjacency list of names to parent supervisor names
    graph_map = defaultdict(set)
    root = generate_name()
    seen_names.add(root)
    graph_map[root] = set()
    all_levels = [[root]]

    for i in range(1, level):
        curr_level = []
        # this loop scales with the level of the hierarchy
        # can modify for flatter/taller orgs
        for j in range(0, random.randint(len(all_levels[-1]), max(2, level**2 // 2))):
            curr_name = generate_name()
            while(curr_name in seen_names):
                curr_name = generate_name()
                
            seen_names.add(curr_name)

            # add supervisors from higher levels (at least 1 from the last level)
            last_level_size = len(all_levels[-1])
            direct_supervisor_I = all_levels[-1][random.randint(0, last_level_size - 1)]
            graph_map[curr_name].add(direct_supervisor_I)
            for i in range(random.randint(0, additional_supervisors)):
                upper_level = random.randint(0, len(all_levels) - 1)
                direct_supervisor = list(all_levels[upper_level])[random.randint(0, len(all_levels[upper_level]) - 1)]
                graph_map[curr_name].add(direct_supervisor)
            curr_level.append(curr_name)
        all_levels.append(curr_level)

    return all_levels, graph_map

print(*generate_org_chart())