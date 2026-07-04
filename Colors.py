class Colors:
    GEMS = {
        0: (255, 0, 0),       # Red
        1: (0, 220, 0),       # Green
        2: (40, 120, 255),    # Blue
        3: (255, 220, 0),     # Yellow
        4: (180, 0, 255),     # Purple
    }

    @classmethod
    def get_color(cls, value: int) -> tuple[int, int, int]:
        return cls.GEMS.get(value, (255, 255, 255))