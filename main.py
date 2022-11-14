from dijkstra import print_answer

graph = {
        ("B", "D"): 2,
        ("D", "A"): 1,
        ("B", "A"): 4,
        ("A", "C"): 2,
        ("B", "E"): 3,
        ("C", "D"): 7,
        ("E", "C"): 3
    }

if __name__ == "__main__":
    print_answer("A", "B", graph)
