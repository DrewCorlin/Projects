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

# #python 3
# import math
# from random import *
# class Box:
#     def __init__(self, weight, value):
#         self.weight = weight
#         self.value = value

#     def print(self):
#         print("Weight:", self.weight, "Value:", self.value)

# class GeneticKnapsack:
#     def __init__(self, chromosome, rate):
#         self.MAX_WEIGHT = 120
#         self.MUTATION_RATE = rate
#         self.chromosome = chromosome

#     def fitness(self):
#         totalValue = 0
#         for box in self.chromosome:
#             totalValue += box.value
#         return totalValue if self.weight() < self.MAX_WEIGHT else 0

#     def weight(self):
#         totalWeight = 0
#         for box in self.chromosome:
#             totalWeight += box.weight
#         return totalWeight

#     def print(self):
#         print("Total Weight:", self.weight(), "Fitness:", self.fitness())

#     def printBoxes(self):
#         for box in self.chromosome:
#             box.print()

#     def crossover(self, other, randomBoxes):
#         newChr = set()
#         for x in range(0, len(self.chromosome)):
#             proposedGene = self.chromosome[x] if random() > 0.5 else other.chromosome[x]
#             while len(newChr) < len(self.chromosome):
#                 proposedGene = self.chromosome[math.floor(random() * len(self.chromosome))] if random() > 0.5 else chromosome[math.floor(random() * len(self.chromosome))] #If the gene is already in the chromosome pick a new one until you find one that is 
#                 newChr.add(proposedGene)
#         # print(len(newChr), len(self.chromosome))
#         for x in range(0, len(newChr)):
#             if random() < self.MUTATION_RATE:
#                 list(newChr)[x] = randomBoxes[math.floor(random() * len(randomBoxes))]
#         GP = GeneticKnapsack(list(newChr), self.MUTATION_RATE)
#         return GP if GP.fitness() > 0 else self

# class KnapsackPopulation:
#     def __init__(self, initialPopulation, populationSize, generationLimit, randoms):
#         self.populationSize = populationSize
#         self.generationLimit = generationLimit
#         self.population = initialPopulation
#         self.breedingPool = initialPopulation
#         self.randomBoxes = randoms
#         self.currentGeneration = 0
#         self.MAX_WEIGHT = 120
#         self.best = self.mostFit()

#     def simulate(self):
#         for x in range(0, self.generationLimit):
#             self.advanceGeneration()
#         return self

#     def cull(self):
#         self.population.sort(key=GeneticKnapsack.fitness)
#         culledPop = self.population[:math.ceil(len(self.population)/2)] #get the second half of the sorted population
#         culledPop.append(culledPop)
#         culledPop = culledPop[:100]
#         return

#     def mostFit(self):
#         highestFitness = -1
#         mostFit = None
#         for x in range(0, len(self.population)):
#             if self.population[x].fitness() > highestFitness and self.population[x].weight() < self.MAX_WEIGHT:
#                 mostFit = self.population[x]
#         return mostFit

#     def advanceGeneration(self):
#         self.cull()
#         for x in range(0, self.populationSize):
#             self.population[x] = self.breedingPool[math.floor(random() * self.populationSize)].crossover(self.breedingPool[math.floor(random() * self.populationSize)], self.randomBoxes) #Randomly pick 2 members of the population to breed
#         self.best = self.mostFit()
#         print("Best fitness of generation", self.currentGeneration + 1, " is ", self.best.fitness())
#         self.currentGeneration += 1

# def pickBoxes(numBoxes, avaliableBoxes):
#     if numBoxes > len(avaliableBoxes):
#         return
#     boxesPicked = set()
#     while len(boxesPicked) < numBoxes:
#         boxesPicked.add(avaliableBoxes[math.floor(random() * len(avaliableBoxes))])
#     return list(boxesPicked)

# boxWeights = [20, 30, 60, 90, 50, 70, 30]
# boxValues = [6, 5, 8, 7, 6, 9, 4]
# extendedWeights = [20, 30, 60, 90, 50, 70, 30, 24, 19, 13, 16, 10, 12, 12, 23, 59, 32]
# extendedValues = [6, 5, 12, 17, 6, 13, 4, 3, 2, 8, 9, 1, 2, 5, 3, 16, 6]
# boxes = []

# for x in range(0, len(extendedWeights)):
#     boxes.append(Box(extendedWeights[x], extendedValues[x]))

# initPop = []

# MUTATION_RATE = 0.02
# POPULATION_SIZE = 100
# GENERATIONS = 50

# for x in range(0, 100):
#     chromosome = pickBoxes(6, boxes)
#     initPop.append(GeneticKnapsack(chromosome, MUTATION_RATE))

# population = KnapsackPopulation(initPop, POPULATION_SIZE, GENERATIONS, boxes)

# finalPopulation = population.simulate()

# print("The best knapsack after", GENERATIONS, "generations with a mutation rate of", MUTATION_RATE, "and a population size of", POPULATION_SIZE, "contains these bags:")
# finalPopulation.best.printBoxes()

