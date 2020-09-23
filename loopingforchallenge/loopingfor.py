#! python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

def get_animals_ne_farm():
    animals_ne_farm = []
    for animal in farms[0]["agriculture"]:
        animals_ne_farm.append(animal)
    return animals_ne_farm

def specify_farm():
    ag_from_farm = []
    farm = input('Please select:\n1. NE Farm\n2. W Farm\n3. SE Farm\n')
    if farm == '1':
        for ag in farms[0]["agriculture"]:
            ag_from_farm.append(ag)
    elif farm == '2':
        for ag in farms[1]["agriculture"]:
            ag_from_farm.append(ag)
    elif farm == '3':
        for ag in farms[2]["agriculture"]:
            ag_from_farm.append(ag)
    return ag_from_farm

def specify_farm_animals_only():
    animals_from_farm = []
    farm = input('Please select:\n1. NE Farm\n2. W Farm\n3. SE Farm\n')
    if farm == '1':
        for animal in farms[0]["agriculture"]:
            animals_from_farm.append(animal)
    elif farm == '2':
        for animal in farms[1]["agriculture"]:
            animals_from_farm.append(animal)
    elif farm == '3':
        animals_from_farm.append("chickens")
    return animals_from_farm

print("EASY(ISH):")
for animal in get_animals_ne_farm():
    print(animal + " ")
print("\n")

print("MEDIUM:")
for ag in specify_farm():
    print(ag + " ")
print("\n")

print("HARD:")
for animal in specify_farm_animals_only():
    print(animal + " ")
