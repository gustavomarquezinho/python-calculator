from calcs import Calcs
from timeit import timeit


timer_x = timeit(
    "Calcs('2340334 + 32452 - 34647 * 2 + 3224242 - 1234 / 4', True)",
    number=100_000,
    globals=globals()
)


timer_y = timeit(
    "Calcs('12324 + 1246624 + 1 / 345 - 5 * 45', True)",
    number=100_000,
    globals=globals()
)


print(timer_x)
print(timer_y)

