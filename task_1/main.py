#!/usr/bin/python3
import collections
import string
from pathlib import Path
from arg_parser import parse_args


def get_horse_and_pawn_pos():
    file_data = Path(parse_args().input_filename[0]) \
        .read_text().split('\n')
    return file_data[0], file_data[1]


def init_graph():
    """Initialize graph empty lists"""
    graph = {}
    for letter in string.ascii_lowercase[:8]:
        for number in range(1, 9):
            graph[letter + str(number)] = []
    return graph


def build_all_possible_paths(letter, number):
    """Return possible paths in order recording to `task_1` doc"""
    return [
        (ord(letter) + 1, number + 2),
        (ord(letter) - 1, number + 2),
        (ord(letter) + 2, number + 1),
        (ord(letter) + 2, number - 1),
        (ord(letter) + 1, number - 2),
        (ord(letter) - 1, number - 2),
        (ord(letter) - 2, number + 1),
        (ord(letter) - 2, number - 1)
    ]


def build_graph():
    """Build graph using `build_all_possible_paths`"""
    graph = init_graph()
    for letter in string.ascii_lowercase[:8]:
        for number in range(1, 9):
            for move in build_all_possible_paths(letter, number):
                move_letter = chr(move[0])
                move_number = move[1]
                if "a" <= move_letter <= "h" and 1 <= move_number <= 8:
                    graph[letter + str(number)].append(str(move_letter) + str(move_number))
    return graph


def build_result_path(visited, target):
    current_key = target
    result = [target]
    while current_key is not None:
        value = visited[current_key]
        result.append(value)
        current_key = value
    return result


def bfs(graph, root, target):
    visited, queue = {}, collections.deque([root])
    visited[root] = None
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited[neighbour] = vertex
                if neighbour == target:
                    return build_result_path(visited, target)
                queue.append(neighbour)


def main():
    horse_pos, pawn_pos = get_horse_and_pawn_pos()
    graph = build_graph()
    res = bfs(graph, horse_pos, pawn_pos)
    res.remove(None)
    p = Path("output.txt")
    if not p.exists():
        p.touch()
    p.write_text("\n".join(res))


if __name__ == '__main__':
    main()
