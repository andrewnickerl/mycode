#! python3

items = ["biscuit", "broccoli", "dirty dish", "toy", "light", "inside out sock", "penny", "A", "F"]
places = ["room", "plate", "room", "hallway", "room", "laundry", "ground", "report card", "report card"]
results = ["flog you", "slap you", "whoop your ass", "throw them away", "take a dollar", "throw it in the trash", "put 1 cent in my piggy bank to save up for the great depression", "give you a new videogame for your collection", "put another snake in your bed"]

def grandma_threats():
    threats = []
    for i in range(len(items)):
        threats.append(f"For every {items[i]} I find in your {places[i]} I'm going to {results[i]}!")
    return threats

for threat in grandma_threats():
    print(threat + "\n")