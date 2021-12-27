from random import uniform


class Gift:
    """A Gift can be stolen if it's been stolen less than 3 times already."""

    def __init__(self, index: int) -> None:
        self.value = round(uniform(0.01, 1), 2)
        self.index = index
        self.times_stolen = 0
        self.current_owner = None

    def __repr__(self) -> str:
        return f"Gift {self.index}"

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other) -> bool:
        return self.value == other.value
