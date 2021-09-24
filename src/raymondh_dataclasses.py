from dataclasses import dataclass

@dataclass
class Color:
    hue: int
    saturation: float
    lightness: float = 0.5

#################################################################

from typing import NamedTuple

class Color2(NamedTuple):
    hue: int
    saturation: float
    lightness: float = 0.5

#################################################################


if __name__ == "__main__":
    pass
