
# Map Coloring using CSP

# Regions and their neighboring regions
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
coloring = {}

def is_safe(region, color):
    for neighbor in graph[region]:
        if coloring.get(neighbor) == color:
            return False
    return True

def solve(regions):
    if not regions:
        return True

    region = regions[0]

    for color in colors:
        if is_safe(region, color):
            coloring[region] = color

            if solve(regions[1:]):
                return True

            del coloring[region]

    return False

# Main program
if solve(list(graph.keys())):
    print("Map Coloring Solution:")
    for region, color in coloring.items():
        print(region, ":", color)
else:
    print("No solution exists")
