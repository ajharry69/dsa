def connected_sinks(filepath):
    """
    This function determines which sinks are connected to the source in a pipe system.

    Args:
        filepath: Path to the file containing the pipe system data.

    Returns:
        A string of uppercase letters representing the connected sinks in alphabetical order.
    """
    grid = {}
    sinks = set()
    x_max = y_max = 0

    # Read pipe system data
    with open(filepath, 'r') as f:
        for line in f:
            obj, x, y = line.strip().split()
            x, y = int(x), int(y)
            grid[(x, y)] = obj
            if obj.isalpha():
                sinks.add(obj)

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

    matrix = seq_matrix(grid, x_max, y_max)

    print("=" * 80)

    reverse_seq_matrix(grid, matrix, x_max, y_max)
    return ""


def seq_matrix(grid, x_max, y_max):
    y = y_max
    while y >= 0:
        yc = (y_max - y)
        data = ""
        for x in range(x_max + 1):
            data += grid.get((x, yc), " ")
        print(data)
        y -= 1
    matrix = []
    y = y_max
    while y >= 0:
        yc = (y_max - y)
        matrix_row = []
        for x in range(x_max + 1):
            matrix_row.append((x, yc, grid.get((x, yc), " ")))
        matrix.append(matrix_row)
        print(matrix_row)
        y -= 1
    return matrix


def reverse_seq_matrix(grid, matrix, x_max, y_max):
    y = y_max
    while y >= 0:
        data = ""
        for x in range(x_max + 1):
            data += grid.get((x, y), " ")
        print(data)
        y -= 1
    y = y_max
    while y >= 0:
        print(matrix[y])
        y -= 1


if __name__ == '__main__':
    for path in (
            "input1.txt",
            # "input2.txt",
    ):
        print(f"Connected sinks for '{path}':", connected_sinks(filepath=path))
