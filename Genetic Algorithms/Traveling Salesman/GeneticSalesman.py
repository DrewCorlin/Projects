from math import sqrt, floor
from random import random

class City:
    def __init__(self, position):
        self.position = position

    def distanceTo(self, other):
        a = abs(self.position[0] - other.position[0])
        b = abs(self.position[0] - other.position[0])
        return sqrt(a**2 + b**2)

def createCities(locations):
    cities = []
    for location in locations:
        cities.append(City(location))
    return cities



class GeneticSalesman:
    def __init__(self, chromosome, rate):
        self.chromosome = chromosome
        self.MUTATION_RATE = rate

    def fitness(self):
        return sum(self.chromosome[x].distanceTo(self.chromosome[x + 1]) for x in range(0, len(self.chromosome) - 1))

    def crossover(self):
        pass

locations = [(1586, 1463), (1696, 1773), (2594, 767), (1621, 2446), (394, 2740), (2126, 1048), (363, 408), (302, 1529), (497, 85), (459, 2344), (1841, 1553), (693, 328), (2662, 2016), (100, 2955), (1224, 2845), (593, 417), (1792, 2210), (2341, 478), (2321, 263), (2474, 1252)]

cities = createCities(locations)

GS = GeneticSalesman(cities, 0.05)

print(GS.fitness())
