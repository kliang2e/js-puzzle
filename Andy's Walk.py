from fractions import Fraction as F
from collections import defaultdict
import itertools

GENS = [(1, 0), (0, 1), (-1, -1)]
HOME_LABEL = (0, 0)
def label(pos):
    a, b = pos
    return (a % 2, b % 2)