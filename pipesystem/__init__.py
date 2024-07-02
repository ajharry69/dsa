def connected_sinks(filepath):
    """
    This function determines which sinks are connected to the source in a pipe system.

    Args:
        filepath: Path to the file containing the pipe system data.

    Returns:
        A string of uppercase letters representing the connected sinks in alphabetical order.
    """
    grid = {}
    x_max = y_max = 0

    # Read pipe system data
    with open(filepath, 'r') as f:
        for line in f:
            obj, x, y = line.strip().split()
            x, y = int(x), int(y)
            grid[(x, y)] = obj

            x_max = max(x_max, x)
            y_max = max(y_max, y)

    pipes = {
        '═': {'R', 'L'},
        '║': {'T', 'B'},
        '╔': {'R', 'B'},
        '╗': {'L', 'B'},
        '╚': {'R', 'T'},
        '╝': {'L', 'T'},
        '╠': {'R', 'T', 'B'},
        '╣': {'L', 'T', 'B'},
        '╦': {'R', 'L', 'B'},
        '╩': {'R', 'L', 'T'},
    }
    y_count = y_max
    while y_count >= 0:
        data = ""
        for x in range(x_max + 1):
            d = grid.get((x, y_count), " ")
            data += d
        print(data)
        y_count -= 1
    return ""


if __name__ == '__main__':
    # for path in ("input1.txt", "input2.txt"):
    for path in ("input1.txt", "input1d.txt",):
        print(f"Connected sinks for '{path}':", connected_sinks(filepath=path))
