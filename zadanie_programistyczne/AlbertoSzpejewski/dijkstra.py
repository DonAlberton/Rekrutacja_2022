from typing import List, Dict, Tuple, Union, NoReturn

Graph = Dict[str, Dict[str, float]]
Table = Dict[str, List[Union[float, str]]]

def create_graph(graph: Dict[Tuple[str, str], float]) -> Graph:
    """
    Function reshapes the given data into a more
    human and computer readable format. The data structure contains
    any node neighbors

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


def create_table(graph: Graph) -> Table:
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


def next_node(table: Table, non_visited: List) -> str:
    """
    Chooses the next node available from the non_visited list.
    When the node is not in non_visited, then skips it and 
    proceed to chose other ones

    Args:
        table: Dict[str, List[Union[float, str]]]
        non_visited: List[str]

    Returns:
        str
    """

    looked = {}

    for node in non_visited:
        looked[node] = table[node][0]
    
    if looked: 
        return min(looked, key=looked.get)


def dijkstra(start: str, graph: Graph, table: Table) -> Table:
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

    # Starts putting a zero in the beggining value
    # establishing the lowest value to a node
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


def print_answer(start: str, end: str, graph: Graph) -> NoReturn:
    """
    Groups every function return and processes
    it to get an easy to read shortest path

    Args:
        start str: Start node
        end str: End node
        graph Dict[Tuple[str, str], float]: Graph from create graph function

    Returns:
        NoReturn
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
