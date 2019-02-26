import numpy as np
import random as rn
import sys
import matplotlib.pyplot as plt
from matplotlib import animation

# Probabilistic Robotics - Chapter 2 - Problem 2
startingfrom = "Rainy"
days_ = 50
states = ["Sunny","Cloudy","Rainy"]

# Possible sequences of events
# First letter: Transition From
# Second letter: Transition To
# SS - From Sunny to Sunny
# SC - From Sunny to Cloudy
# SR - From Sunny to Rainy etc.

transition = [["SS","SC","SR"],["CS","CC","CR"],["RS","RC","RR"]]

# State transition probabilities
# Each row should sum up to 1 to fullfill probability rule
P = [[0.8, 0.2, 0],[0.4, 0.4, 0.2],[0.2, 0.6, 0.2]]

x_ = []
resultList = []

def SimulateMarkovChain(startstate, days):
    print("Start State: " + startstate);
    resultList.clear()
    resultList.append(startstate);  # Keep results on this list
    state = startstate;
    probability = 1;
    i =0;
    x_.insert(i,state);

    while i!=(days):
       
        if state == "Sunny":
            change = np.random.choice(transition[0],replace = False, p=P[0]); # Simulate random change from "Sunny" to any.
            if change == "SS":
                probability = probability*0.8
                resultList.append("Sunny");
                pass
            elif change  == "SC":
                probability *= 0.2
                resultList.append("Cloudy");
                state = "Cloudy"
                pass
            else:
                pass
        elif state == "Cloudy":
            change = np.random.choice(transition[1],replace = False, p=P[1]); # Simulate random change from "Cloudy" to any.
            if change == "CS":
                probability *= 0.4
                resultList.append("Sunny");
                state = "Sunny"
                pass
            elif change  == "CC":
                probability *= 0.4
                resultList.append("Cloudy");
                pass
            else:
                probability *= 0.2
                resultList.append("Rainy");
                state = "Rainy"
        elif state == "Rainy":
            change = np.random.choice(transition[2],replace = False, p=P[2]); # Simulate random change from "Rainy" to any.
            if change == "RS":
                probability *= 0.2
                resultList.append("Sunny");
                state = "Sunny"
                pass
            elif change  == "RC":
                probability *= 0.6
                resultList.append("Cloudy");
                state = "Cloudy"
                pass
            else:
                probability *= 0.2
                resultList.append("Rainy");

        i +=1; # we just finished one day simulation
        x_.insert(i,state);

        print("Probability for sequence of " +str(i) +" days : "  +str(probability))

    print("\nPossible States of This Markov Process: " + str(states));
    print("Transition of simulation for " + str(days) +" days: " + str(resultList))


# Call Simulation
SimulateMarkovChain(startingfrom, days_);

# Create 'time' coordinate for plotting
timePlot = []
for j in range(days_+1):
    timePlot.append(j)

plt.plot(timePlot, resultList)
plt.xlim([-4, days_+1])
plt.ylim([-1, 3])
plt.grid(True)
plt.text(-4,-1, "Simulation for: " + str(days_)+" Days")
plt.savefig("MarkovChainSimulation100days");
plt.show()

# No matter what this array will contain the 
# stationary distribution will always be the same
startprobabilities = [0.5, 0.25, 0.25];

# Stationary distribution calculation
P_tot = P
for x in range(200):
   P_tot = np.matmul(P_tot, P)


stationaryProbabilities = np.matmul(startprobabilities, P_tot)
print("\nStationary distribution : " + str(stationaryProbabilities)+"\n")