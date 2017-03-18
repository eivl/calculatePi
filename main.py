from math import gcd
import random

UPPER_BOUND = 120
ITTERATIONS = 500


def two_numbers():
    yield (random.randint(0, UPPER_BOUND), random.randint(0, UPPER_BOUND))

for i in range(ITTERATIONS):
    v = next(two_numbers())
    gcdTest = gcd(v[0], v[0])
    if(gcdTest == 1):
        print("{} and {} are CoPrime with a factor of {}"
              .format(v[0], v[1], gcdTest))
    else:
        print("{} and {} are CoFactor with a factor of {}"
              .format(v[0], v[1], gcdTest))
