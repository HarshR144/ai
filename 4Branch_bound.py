
def is_safe(graph, colours, colour, current):
    neighbours = graph[current]
    for neighbour in neighbours:
        if colour == colours[neighbour - 1]:
            return False
    return True

def graph_traversal(graph, colours, vertices, current, current_colour, min_colours, result):
    if current == vertices + 1:
        min_colours = min(current_colour, min_colours)
        result.append(colours.copy())
        return min_colours
    
    for i in range(1,vertices):
        if i > min_colours:
            break
        if is_safe(graph, colours, i, current):
            colours[current - 1] = i
            min_colours = graph_traversal(graph, colours, vertices, current+1, i, min_colours, result)
            colours[current - 1] = 0
    return min_colours

def graph_colouring(graph, vertices):
    colours = [0 for i in range(vertices)]
    result = list()
    
    graph_traversal(graph, colours, vertices, 1,0,float('inf'), result)
    return result

def print_colours(results):
    for colours in results:
        for i in range(len(colours)):
            print(i + 1, ":", colours[i])
        print("\n")

vertices = int(input("Enter the number of vertices: "))
graph = {}
for i in range(1, vertices + 1):
    neighbours = list(map(int, input(f"Enter the neighbors of vertex {i} (separated by spaces): ").split()))
    graph[i] = neighbours

# Perform graph coloring
col = graph_colouring(graph, vertices)
if col is not None:
    print("Graph can be colored with the following colors:")
    print_colours(col)
else:
    print("Graph cannot be colored.")
# Enter the number of vertices: 4
# Enter the neighbors of vertex 1 (separated by spaces): 2 3
# Enter the neighbors of vertex 2 (separated by spaces): 1 3 4
# Enter the neighbors of vertex 3 (separated by spaces): 1 2 4
# Enter the neighbors of vertex 4 (separated by spaces): 2 3
# Graph can be colored with the following colors:
# 1 : 1
# 2 : 2
# 3 : 3
# 4 : 1

