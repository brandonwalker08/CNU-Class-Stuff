

import random, math, copy, matplotlib.pyplot as plt


def main():
    numCities = 10
    temp = 100000
    coolRate = 0.95
    cities = []
    cnt = 0

    # Generate random cities
    while cnt != numCities:
        x1 = random.randint(1,99)
        y1 = random.randint(1,99)
        point = [x1,y1]
        #River??
        if x1 > 45 and x1 <55 or point in cities:
            # do nothing, in river
            donothing = 0
        else:
            cities.append(point)
            cnt += 1


    # Order in which each city will be visited
    visitOrder = random.sample(range(numCities), numCities)


    # Start Cooling
    while temp > 1:

        # Keep track of reconfigurations, either 10N or 100N to rethermalize
        rethermalize = False
        successfulConfig = 0
        reconfigs = 0
        while rethermalize == False:

            # Generate a new order of cities
            newOrder = copy.copy(visitOrder)
            tempVal = range(len(visitOrder))
            city1, city2 = random.sample(tempVal, 2)
            newOrder[city1], newOrder[city2] = newOrder[city2], newOrder[city1]

            # newOrder = generateNewVisitOrder(visitOrder)

            # Generate "energies" (total distance) of each visit order
            energies = energyFunction(cities, visitOrder, newOrder, numCities, city1, city2)

            # Generate probability of swap
            schedulingFactor = scheduling(energies[0], energies[1], temp)

            # Function returned 1.0 if old energy was better than new
            if schedulingFactor == 1.0:
                visitOrder = copy.copy(newOrder)
                successfulConfig += 1

            # Function delivered probability, if it's greater than a random probability, swap
            elif schedulingFactor > random.random():
                successfulConfig += 1
                visitOrder = copy.copy(newOrder)

            reconfigs += 1

            if successfulConfig == (10 * numCities) or reconfigs == (100 * numCities):
                rethermalize = True

        # Alter temp
        temp = temp * coolRate

    # Make graph
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.axvline(x=50, linewidth=4, color='b')
    plt.tick_params(direction='out', width=2, colors='g', grid_color='r', grid_alpha=0.5)

    x, y = list(zip(*cities))
    plt.plot(x, y, 'bo')
    i = 0
    while i < numCities:
        plt.text(x[i], y[i], str(i + 1))
        i += 1
    plt.show()

    i = 0
    while i < numCities:
        plt.text(x[i], y[i], str(i + 1))
        i += 1
    plt.plot(x,y, '-.bo')
    plt.show()

    i = 0
    while i < numCities:
        plt.text(x[i], y[i], str(i + 1))
        i += 1
    plt.plot(list(zip(*[cities[visitOrder[i % numCities]] for i in range(numCities+1)]))[0], list(zip(*[cities[visitOrder[i % numCities]] for i in range(numCities+1)]))[1], '-.bo')

    plt.show()


def energyFunction(cities, visitOrder, newVisitOrder, numCities, city1, city2):
    # Energy Function
    energy  = 0
    newEnergy = 0
    for j in [city2, city2 - 1, city1, city1 - 1]:
        for i in [0, 1]:
            energy += math.sqrt(sum([(cities[visitOrder[(j + 1) % numCities]][i] - cities[visitOrder[j % numCities]][i]) ** 2]))
    for j in [city2, city2 - 1, city1, city1 - 1]:
         for i in [0, 1]:
            newEnergy += math.sqrt(sum([(cities[newVisitOrder[(j + 1) % numCities]][i] - cities[newVisitOrder[j % numCities]][i]) ** 2]))

    energies = [energy, newEnergy]
    return energies


def scheduling(energy, newEnergy, temp):
    if newEnergy <= energy:
        return 1.0
    elif newEnergy > energy:
        return math.exp((energy - newEnergy) / temp)


# def cooling(origTemp, coolFactor):
#     temp = origTemp
#     while True:
#         yield temp
#         temp = coolFactor * temp

def generateNewVisitOrder(oldVisitOrder):
    newOrder = copy.copy(oldVisitOrder)
    temp = range(len(oldVisitOrder))
    city1, city2 = random.sample(temp, 2)
    newOrder[city1], newOrder[city2] = newOrder[city2], newOrder[city1]
    return newOrder


main()