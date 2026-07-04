COLORS = [
    (255, 0, 0),    # red
    (0, 255, 0),    # green
    (0, 0, 255),    # blue
    (255, 255, 0)   # yellow
]


def get_color(value: int):
    if 0 <= value < len(COLORS):
        return COLORS[value]
    return (255, 255, 255)