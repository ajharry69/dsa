def solution(images):
    """
    I = render independently
    P1 = render in pair as the first item
    P2 = render in pair as the second item
    """
    r = []
    for i, image in enumerate(images):
        if (i + 1) % 3 == 0:
            r.append((image, 'P2'))
        elif (i + 2) % 3 == 0:
            r.append((image, 'P1'))
        else:
            r.append((image, 'I'))
    return r