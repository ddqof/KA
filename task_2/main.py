#!/usr/bin/python3

from color import Color
from color import get_opposite_color
from exceptions import GraphIsNotBipartiteException


def dfs(start_node, graph):
    visited = set()
    result_colors = {}

    def internal_dfs(node):
        if node not in visited:
            result_colors.update(paint(node, result_colors, graph))
            visited.add(node)
            for i in range(len(graph)):
                if graph[node][i] == 1:
                    internal_dfs(i)

    internal_dfs(start_node)

    return result_colors


def paint(node, colors_dict, graph):
    upd_colors = colors_dict
    if len(upd_colors) == 0:
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
    splatted_data = raw_text.splitlines()
    splatted_data.pop(0)
    matrix = [[] for _ in range(len(splatted_data))]
    for i in range(len(splatted_data)):
        matrix[i] = [int(x) for x in splatted_data[i].split()]
    return matrix


def get_nodes_by_color_list(colors_by_nodes, target_color):
    return [x[0] + 1 for x in colors_by_nodes.items() if x[1] is target_color]


if __name__ == '__main__':
    with open("input.txt") as input_file:
        try:
            colors = dfs(0, parse(input_file.read()))
            # print("Y")
            red_list = sorted(get_nodes_by_color_list(colors, Color.RED))
            black_list = sorted(get_nodes_by_color_list(colors, Color.BLACK))
            result = "Y\n" + " ".join(str(x) for x in red_list) + "\n" + "0\n" + " ".join(
                str(x) for x in black_list) + "\n"
        except GraphIsNotBipartiteException:
            result = "N\n"
        with open("output.txt", "w+") as output:
            output.write(result)
