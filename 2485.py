def find_neighbors(coordinate):
    x, y = coordinate
    possible_neighbors = {(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2)}
    return {neighbor for neighbor in possible_neighbors if neighbor != coordinate and 
            all(0 <= dim < columns if idx else 0 <= dim < lines for idx, dim in enumerate(neighbor))}
 
def cure_trees(lines, columns, cure, affected_coordinates):
    cured = {cure}
    affected_coordinates.remove(cure)
    days = 0
    while affected_coordinates:
        days += 1
        new_cured = set()
        for treated_tree in cured:
            affected_neighbors = affected_coordinates.intersection(find_neighbors(treated_tree))
            new_cured.update(affected_neighbors)
            affected_coordinates.difference_update(affected_neighbors)
        cured = new_cured
    return days

tests = int(input())
for _ in range(tests):
    lines, columns = [int(x) for x in input().split()]
    g = [list(map(int, input().split())) for i in range(lines)]
    affected_coordinates = {(i, j) for i in range(lines) for j in range(columns) if g[i][j] == 1}
    cure = tuple(map(lambda x: x - 1, map(int, input().split())))
    print(cure_trees(lines, columns, cure, affected_coordinates))
