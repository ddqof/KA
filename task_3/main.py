class PositiveCycleDetected(Exception):

    def __init__(self, msg):
        super(PositiveCycleDetected, self).__init__(msg)


class VertexIsNotReachable(Exception):

    def __init__(self, msg):
        super(VertexIsNotReachable, self).__init__(msg)


def build_graph(input_filename):
    with open(input_filename) as f:
        data = f.read().splitlines()
    vertices_count = int(data.pop(0))
    target = int(data.pop(-1)) - 1
    start = int(data.pop(-1)) - 1
    sled = [[] for _ in range(vertices_count)]
    for i in range(vertices_count):
        sled[i] = [int(x) for x in data[i].split()]
    matrix = [[] for _ in range(vertices_count)]
    for i in range(len(matrix)):
        current_sled = sled[i]
        matrix[i] = [-1 for _ in range(vertices_count)]
        for j in range(0, len(current_sled), 2):
            if current_sled[j] == 0:
                break
            matrix[i][current_sled[j] - 1] = current_sled[j + 1]
    return {
        "matrix": matrix,
        "start": start,
        "target": target,
        "v": vertices_count
    }


def ford_bellman(start, target, matrix):
    dist, previous = {}, {}
    vertices_count = len(matrix)
    dist[start] = 0
    for i in range(len(matrix)):
        dist[i] = 1
        if matrix[i][start] != -1:
            previous[i] = start
    result = {}
    for k in range(vertices_count):
        if k == vertices_count - 1:
            result = dist.copy()
        for u in range(len(matrix)):
            for v in range(len(matrix)):
                weight = matrix[u][v]
                if weight == -1:
                    continue
                update(u, v, dist, previous, matrix)
        if k == vertices_count - 1:
            for item in zip(result.values(), dist.values()):
                if item[0] < item[1]:
                    raise PositiveCycleDetected(
                        "Max path isn't defined due to positive cycle"
                    )
    return dist, previous


def update(u, v, dist, prev, matrix):
    if dist[v] < dist[u] * matrix[u][v]:
        dist[v] = dist[u] * matrix[u][v]
        prev[v] = u


def build_path(previous, start, target):
    path = [target]
    v = previous.get(target)
    if v is None:
        raise VertexIsNotReachable(f"Vertex: {target} isn't reachable")
    path.append(v)
    while v != start:
        v = previous.get(v)
        path.append(v)
    path.reverse()
    path = [str(x + 1) for x in path]
    return " ".join(path)


if __name__ == "__main__":
    try:
        graph = build_graph("in.txt")
        start, target, matrix = graph["start"], graph["target"], graph["matrix"]
        distances, prev = ford_bellman(
            start, target, matrix
        )
        str_path = build_path(prev, start, target)
        result = f"Y\n{str_path}\n{distances[target]}"
    except (PositiveCycleDetected, VertexIsNotReachable):
        result = "N"
    with open("out.txt", "w") as f:
        f.write(result)
