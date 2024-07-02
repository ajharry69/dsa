from collections import deque


def connected_sinks(filepath):
    """
    This function determines which sinks are connected to the source in a pipe system.

    Args:
        filepath: Path to the file containing the pipe system data.

    Returns:
        A string of uppercase letters representing the connected sinks in alphabetical order.
    """
    grid = []
    source = None
    sinks = set()

    # Read pipe system data
    with open(filepath, 'r') as f:
        for line in f:
            obj, x, y = line.strip().split()
            x, y = int(x), int(y)
            grid.append((obj, x, y))
            if obj == '*':
                source = (x, y)
            elif obj.isupper():
                sinks.add(obj)

    # Define directions and opposite directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    opposite_directions = {
        (0, 1): (0, -1),
        (1, 0): (-1, 0),
        (0, -1): (0, 1),
        (-1, 0): (1, 0),
    }

    # Perform BFS starting from the source
    visited = set()
    connected = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                obj, _, _ = grid[new_y * len(grid[0]) + new_x]
                if (new_x, new_y) not in visited:
                    if obj in sinks:
                        connected.add(obj)
                    elif obj in '═║╔╝╚╗╠╣╦╩':
                        # Check if the pipe connects to the current cell from the previous cell
                        prev_dx, prev_dy = opposite_directions[(dx, dy)]
                        prev_x, prev_y = x + prev_dx, y + prev_dy
                        if 0 <= prev_x < len(grid[0]) and 0 <= prev_y < len(grid):
                            prev_obj, _, _ = grid[prev_y * len(grid[0]) + prev_x]
                            if prev_obj in '═║╔╝╚╗╠╣╦╩':
                                queue.append((new_x, new_y))
                                visited.add((new_x, new_y))

    # Return connected sinks in alphabetical order
    return ''.join(sorted(connected))


if __name__ == '__main__':
    # Example usage - "pipe_system.txt"
    for path in ("input1.txt", "input2.txt"):
        try:
            print(f"Connected sinks for '{path}':", connected_sinks(filepath=path))
        except Exception as e:
            print("Error for", path, e)
