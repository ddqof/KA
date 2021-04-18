from exceptions import GraphIsNotBipartiteException
from color import Color
from color import get_opposite_color


def dfs(start_node, graph):
    visited = set()
    colors = {}

    def internal_dfs(node, nodes_colors):
        if node not in visited:
            upd_colors = paint(node, nodes_colors, graph)
            colors.update(upd_colors)
            visited.add(node)
            for i in range(len(graph)):
                if graph[node][i] == 1:
                    internal_dfs(i, upd_colors)

    internal_dfs(start_node, colors)

    return colors


def paint(node, colors, graph):
    upd_colors = colors
    if len(colors) == 0:
        upd_colors[node] = Color.RED
    else:
        adjacent_colors_set = set()
        for adj_node in range(len(graph)):
            if graph[node][adj_node] == 1 and adj_node in upd_colors:
                adjacent_colors_set.add(upd_colors[adj_node])
        if len(adjacent_colors_set) == 1:
            upd_colors[node] = get_opposite_color(adjacent_colors_set.pop())
        else:
            raise GraphIsNotBipartiteException()
    return upd_colors


def parse(raw_text):
    splatted_data = raw_text.split("\n")
    matrix = [[] for _ in range(1, len(splatted_data) - 1)]
    for i in range(1, len(splatted_data) - 1):
        matrix[i - 1] = [int(x) for x in splatted_data[i].split()]
    return matrix


def get_nodes_by_color_list(colors_by_nodes, target_color):
    return [x[0] + 1 for x in colors_by_nodes.items() if x[1] is target_color]


if __name__ == '__main__':
    with open("input.txt") as f:
        try:
            colors = dfs(0, parse(f.read()))
            print("Y")
            red_list = get_nodes_by_color_list(colors, Color.RED)
            black_list = get_nodes_by_color_list(colors, Color.BLACK)
            print(red_list)
            print(0)
            print(black_list)
        except GraphIsNotBipartiteException:
            print("N")
