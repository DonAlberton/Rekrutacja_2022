from typing import List, Dict, Tuple, Union


def create_graph(graph: Dict[Tuple[str, str], float]
                 ) -> Dict[str, Dict[str, float]]:
    """
    Function reshapes the given data into a more
    human and computer readable format. The data structure contains
    any nodes neighbor

    Args:
        graph Dict[Tuple[str, str], float]: Given data structure

    Returns:
        Dict[str, Dict[str, int]]
    """

    connection_graph = {}

    for connection, value in graph.items():
        if connection[0] in connection_graph:
            connection_graph[connection[0]][connection[1]] = value
        else:
            connection_graph[connection[0]] = {connection[1]: value}

        if connection[1] in connection_graph:
            connection_graph[connection[1]][connection[0]] = value
        else:
            connection_graph[connection[1]] = {connection[0]: value}
    return connection_graph


def create_table(graph: Dict[str, Dict[str, int]]
                 ) -> Dict[str, List[Union[float, str]]]:
    """
    Creates a table needed to perform Dijkstra algorithm

    Args:
        graph (Dict[str, Dict[str, int]]): Data returned by create_graph function

    Returns:
        Dict[str, List[Union[float, str]]]
    """
    table = {}

    for node in graph.keys():
        table[node] = [float("inf"), None]

    return table


def next_node(table, non_visited):
    copy_table = table.copy()

    for element in table:
        print(element, non_visited)
        if element not in non_visited:
            del copy_table[element]

    for element in table:
        if element in non_visited:
            if table[element][0] == copy_table[min(copy_table, key=lambda x: table[x][0])][0]:
                return element


def dijkstra(start: str, graph: Dict[str, Dict[str, int]],
             table: Dict[str, List[Union[int, str]]]
             ) -> Dict[str, List[Union[int, str]]]:
    """
    Performs Dijkstra algorithm on the
    processed graph

    Args:
        start str: Start node
        end str: End node
        graph Dict[str, Dict[str, int]]: Graph from create graph function
        table Dict[str, List[Union[int, str]]]: Dijkstra table to save distances

    Returns:
        Dict[str, List[Union[int, str]]]: Final unprocessed Dijkstra's table
    """

    table[start][0] = 0
    current_node = start

    non_visited = [node for node in graph.keys()]
    visited = []

    while non_visited:

        neighbours = graph[current_node].items()

        for node, length in neighbours:
            if length + table[current_node][0] < table[node][0]:
                table[node][0], table[node][1] = length + table[current_node][0], current_node

        non_visited.remove(current_node)
        visited.append(current_node)

        current_node = next_node(table, non_visited)

    return table


def print_answer(start: str, end: str,
                 graph: Dict[Tuple[str, str], float]
                 ) -> None:
    """
    Groups every function return and processes
    it to get an easy to read shortest path

    Args:
        start str: Start node
        end str: End node
        graph Dict[Tuple[str, str], float]: Graph from create graph function

    Returns:
        None
    """

    graph = create_graph(graph)
    table = create_table(graph)

    answer = dijkstra(start, graph, table)

    node = end

    traversal = [end]

    while answer[node][1] != start:
        node = answer[node][1]
        traversal.append(node)
    traversal.append(start)

    while traversal:
        print(traversal.pop(), end='')

    print()
    print(table[end][0])
