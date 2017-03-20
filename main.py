from math import gcd, sqrt, pi
from statistics import mean
import random

UPPER_BOUND = 1000
ITTERATIONS = 500
RUN_NUMBER_OF_TIMES = 10


def two_numbers():
    yield (random.randint(0, UPPER_BOUND), random.randint(0, UPPER_BOUND))


def calculatePi():
    coprime = 0
    cofactor = 0
    for i in range(ITTERATIONS):
        twoNumbers = next(two_numbers())
        gcdTest = gcd(twoNumbers[0], twoNumbers[1])
        if(gcdTest == 1):
            coprime += 1
        else:
            cofactor += 1
    return (sqrt(6/(coprime/ITTERATIONS)))

piray = [calculatePi() for _ in range(RUN_NUMBER_OF_TIMES)]
calculatedPi = mean(piray)
piError = calculatedPi/pi

if(piError > 1):
    p = (piError-1)/100
    print("The calculated value of Pi is {:.6f},"
          "this is {:.6f}% above the correct value".format(calculatedPi, p))
elif(piError < 1):
    p = (1-piError)/100
    print("The calculated value of Pi is {:.6f},"
          "this is {:.6f}% below the correct value".format(calculatedPi, p))
else:
    print("Calculated Pi is exacly eaqual to Pi")
