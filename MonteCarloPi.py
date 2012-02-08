# MonteCarloPi.py
# November 15, 2011
# By: Feynman Liang

from random import random


def main():
    printIntro()
    n = getInput()
    pi = simulate(n)
    printResults(pi, n)

def printIntro():
    print "This program will use Monte Carlo techniques to generate an"
    print "experimental value for Pi. A circle of radius 1 will be"
    print "inscribed in a square with side length 2. Random points"
    print "will be selected. Since Pi is the constant of proportionality"
    print "between a square and its inscribed circle, Pi should be"
    print "equal to 2*2*(points inside circle/points total)"

def getInput():
    n = input("Enter number of trials: ")
    return n

def simulate(n):
    hit = 0
    for i in range(n):
        result = simulateOne()
        if result == 1:
            hit = hit + 1
    pi = 4 * float(hit) / n
    return pi

def simulateOne():
    x = genCoord()
    y = genCoord()
    distance = x*x + y*y
    if distance <= 1:
        return 1
    else:
        return 0

def genCoord():
    coord = 2*random()-1
    return coord

def printResults(pi, n):
    print "After", n, "simulations, pi was calculated to be: ", pi

if __name__ == "__main__": main()
