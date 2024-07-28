__SOURCE = '*'

__POSITION_MOVES_EXCLUSION = {
    'L': 'R',
    'R': 'L',
    'T': 'B',
    'B': 'T',
}


def connected_sinks(filepath):
    """
    This function determines which sinks are connected to the source in a pipe system.

    Args:
        filepath: Path to the file containing the pipe system data.

    Returns:
        A string of uppercase letters representing the connected sinks in alphabetical order.
    """
    grid = {}
    source_position = None
    x_max = y_max = 0

    # Read pipe system data
    with open(filepath, 'r') as f:
        for line in f:
            obj, x, y = line.strip().split()
            x, y = int(x), int(y)
            grid[(x, y)] = obj
            if obj == __SOURCE:
                source_position = (x, y)

            x_max = max(x_max, x)
            y_max = max(y_max, y)

    # print_seq_matrix(grid, x_max, y_max)
    matrix = get_coordinated_seq_matrix(grid, x_max, y_max)

    print("=" * 80)

    print_reverse_seq_matrix(grid, x_max, y_max)
    print_coordinated_reverse_seq_matrix(matrix, y_max)

    return _get_sinks_connected_to_source(source_position, grid)


def _get_next_position_by_move(current_position, move):
    c2 = {
        'L': (-1, 0),
        'R': (1, 0),
        'T': (0, 1),
        'B': (0, -1),
    }[move]
    return (
        (current_position[0] + c2[0]),
        (current_position[1] + c2[1])
    )


def _is_sink(val):
    return val.isalpha()


def _get_sinks_connected_to_source(source_position, grid):
    incomplete_position_moves = {
        source_position: {'R', 'L', 'T', 'B'},
    }
    incomplete_position_moves_reverse_stack = [
        source_position,
    ]
    _connected_sinks = set()
    while len(incomplete_position_moves_reverse_stack) > 0:
        pending_checks_cleanup_position = -1
        checked_moves = set()
        current_position = incomplete_position_moves_reverse_stack[-1]
        moves = incomplete_position_moves[current_position]
        for move in moves:
            checked_moves.add(move)
            next_position = _get_next_position_by_move(current_position, move)

            val = grid.get(next_position)
            if val is None:
                continue

            if _is_sink(val):
                _connected_sinks.add(val)

            next_position_moves = incomplete_position_moves.get(
                next_position,
                {
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
                }.get(val, {'R', 'L', 'T', 'B'}),
            )
            # will avoid rechecking a move that has just been checked
            next_position_moves -= {__POSITION_MOVES_EXCLUSION[move]}
            if not next_position_moves:
                # will avoid checking moves from a position that does not technically have any more moves left.
                continue

            if next_position in incomplete_position_moves:
                continue

            incomplete_position_moves_reverse_stack.append(next_position)
            incomplete_position_moves[next_position] = next_position_moves
            pending_checks_cleanup_position += -1
            break

        unchecked_moves = moves - checked_moves
        if not unchecked_moves:
            # all moves have been checked
            position = incomplete_position_moves_reverse_stack.pop(pending_checks_cleanup_position)
            del incomplete_position_moves[position]
            continue

        incomplete_position_moves_reverse_stack[pending_checks_cleanup_position] = current_position
        incomplete_position_moves[current_position] = unchecked_moves
    return ''.join(sorted(_connected_sinks))


def print_seq_matrix(grid, x_max, y_max):
    y = y_max
    while y >= 0:
        yc = (y_max - y)
        data = ""
        for x in range(x_max + 1):
            data += grid.get((x, yc), " ")
        print(data)
        y -= 1


def get_coordinated_seq_matrix(grid, x_max, y_max, on_each=None):
    matrix = []
    y = y_max
    while y >= 0:
        yc = (y_max - y)
        matrix_row = []
        for x in range(x_max + 1):
            matrix_row.append((x, yc, grid.get((x, yc), " ")))
        matrix.append(matrix_row)
        if on_each is not None:
            on_each(matrix_row)
        y -= 1
    return matrix


def print_reverse_seq_matrix(grid, x_max, y_max):
    y = y_max
    while y >= 0:
        data = ""
        for x in range(x_max + 1):
            data += grid.get((x, y), " ")
        print(data)
        y -= 1


def print_coordinated_reverse_seq_matrix(matrix, y_max):
    y = y_max
    while y >= 0:
        print(matrix[y])
        y -= 1


if __name__ == '__main__':
    for (path, expected_output) in (
            ("input1.txt", "AC"),
            ("input1.1.txt", "ACDE"),
            ("input1.2.txt", "ACDEFGHIJ"),
            ("input1.3.txt", "ACDEFGHIJK"),
            # ("input1.4.txt", "A"),
            # ("input1.5.txt", "A"),
            # ("input1.5.1.txt", "A"),
            # ("input2.txt", "-"),
    ):
        for i in range(1):
            sinks = connected_sinks(filepath=path)
            assert sinks == expected_output, f"{expected_output} != {sinks}"
            print(f"Connected sinks for '{path}':", sinks)
