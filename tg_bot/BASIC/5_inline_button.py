'''variable & value'''

a: int = 8
b: str = '8'

# ---------------------------------------

'''class'''
from dataclasses import dataclass

@dataclass
class Point:
    lat: float
    long: float


# ---------------------------------------

'''dict'''
d = {}
d.update([(2, 'two'), (5, "five")])
d.update(six=6)
print(d)

# --------------------------------------
'''function'''


def my_function():
    '''Run some computation'''
    return None


print(my_function.__doc__)

# --------------------------------------
'''class and function'''
@dataclass
class Point:
    lat: float
    long: float


def locate(latitude: float, longitude: float) -> Point:
    """Xaritadagi ob'ektni koordinatalari bo'yicha toping"""


print(locate.__annotations__)

# --------------------------------------

p: list[tuple[int, str]]

# --------------------------------------


