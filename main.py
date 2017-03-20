from math import gcd, sqrt, pi
from statistics import mean
import random

UPPER_BOUND = 1000  # the upper bound of the random number generator
ITTERATIONS = 500  # the number of itterations when calculating Pi
RUN_NUMBER_OF_TIMES = 10  # the number of times the caluclation of Pi


# funcion to yield two random numbers
def two_numbers():
    yield (random.randint(0, UPPER_BOUND), random.randint(0, UPPER_BOUND))


# calculate pi based on the ration of coprimes and the number of itterations
def calculatePi():
    coprime = 0
    cofactor = 0  # the cofactor is not actually needed for anything.
    for i in range(ITTERATIONS):
        twoNumbers = next(two_numbers())
        gcdTest = gcd(twoNumbers[0], twoNumbers[1])
        if(gcdTest == 1):
            coprime += 1
        else:
            cofactor += 1
    return (sqrt(6/(coprime/ITTERATIONS)))

# make an array of pi calculations that is RUN_NUMBER_OF_TIMES long
piray = [calculatePi() for _ in range(RUN_NUMBER_OF_TIMES)]
calculatedPi = mean(piray)  # mean for the array
piError = calculatedPi/pi  # error ratio with the real pi

# output result based on if the calculation is above or below real pi.
# numbers are trunchated to 6 decimal places.
if(piError > 1):
    p = (piError-1)*100
    print("The calculated value of Pi is {:.6f},"
          "this is {:.6f} % above the correct value".format(calculatedPi, p))
elif(piError < 1):
    p = (1-piError)*100
    print("The calculated value of Pi is {:.6f},"
          "this is {:.6f} % below the correct value".format(calculatedPi, p))
else:
    print("Calculated Pi is exacly eaqual to Pi")  # GLHF tusse!
