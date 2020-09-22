#! python3

## if\else logic to determine which class of Skyrim (or other Elder Scrolls RPG) hero best suits the user

user_class = []
results = { "Knight (sword, shield, heavy armor)": 0, "Mage (pure magic user)": 0, "Assassin (sneak, daggers, archery)": 0, "Marksman (archery, light armor)": 0, "Battlemage (heavy armor, destruction, and restoration magic)": 0, "Templar (sword, restoration magic)": 0, "Night Blade (daggers, illusion magic, sneak)": 0, "Warrior (two-handed weapon, heavy armor)": 0 }

q1 = input("What attribute is most important?\n1. Strength\n2. Intelligence\n3. Stealth\n")
q2 = input("How do you prefer to face your foes?\n1. Up close and personal\n2. From a distance\n3. Without them know I'm attacking them\n")
q3 = input("What type of weapon do you prefer?\n1. Something I can use with one hand\n2. Heavier is better for smashing!\n3. Projectiles\n4. The arcane\n")
q4 = input("What's the best protection during a fight?\n1. Steel plates and mail\n2. Light leather armor so I can move quickly\n3. A magic barrier\n")

## adds points toward appropriate classes for question one
if q1 == "1":
    results["Knight (sword, shield, heavy armor)"] += 1
    results["Battlemage (heavy armor, destruction, and restoration magic)"] += 1
    results["Templar (sword, restoration magic)"] += 1
    results["Warrior (two-handed weapon, heavy armor)"] += 1
elif q1 == "2":
    results["Mage (pure magic user)"] += 1
    results["Templar (sword, restoration magic)"] += 1
    results["Battlemage (heavy armor, destruction, and restoration magic)"] += 1
    results["Night Blade (daggers, illusion magic, sneak)"] += 1
elif q1 == "3":
    results["Assassin (sneak, daggers, archery)"] += 1
    results["Marksman (archery, light armor)"] += 1
    results["Night Blade (daggers, illusion magic, sneak)"] += 1

## adds points toward appropriate classes for question two
if q2 == "1":
    results["Knight (sword, shield, heavy armor)"] += 1
    results["Battlemage (heavy armor, destruction, and restoration magic)"] += 1
    results["Templar (sword, restoration magic)"] += 1
    results["Warrior (two-handed weapon, heavy armor)"]
elif q2 == "2":
    results["Marksman (archery, light armor)"] += 1
    results["Mage (pure magic user)"] += 1
elif q2 == "3":
    results["Assassin (sneak, daggers, archer)"] += 1
    results["Night Blade (daggers, illusion magic, sneak)"] += 1

## adds points toward appropriate classes for question three
if q3 == "1":
    results["Knight (sword, shield, heavy armor)"] += 1
    results["Assassin (sneak, daggers, archery)"] += 1
    results["Templar (sword, restoration magic)"] += 1
    results["Night Blade (daggers, illusion magic, sneak)"] += 1
elif q3 == "2":
    results["Warrior (two-handed weapon, heavy armor)"] += 1
elif q3 == "3":
    results["Marksman (archery, light armor)"] += 1
elif q3 == "4":
    results["Mage (pure magic user)"] += 1
    results["Battlemage (heavy armor, destruction, and restoration magic)"] += 1

## adds points toward appropriate classes for question four
if q4 == "1":
    results["Knight (sword, shield, heavy armor)"] += 1
    results["Templar (sword, restoration magic)"] += 1
    results["Warrior (two-handed weapon, heavy armor)"] += 1
    results["Battlemage (heavy armor, destruction, and restoration magic)"] += 1
elif q4 == "2":
    results["Assassin (sneak, daggers, archery)"] += 1
    results["Marksman (archery, light armor)"] += 1
    results["Night Blade (daggers, illusion magic, sneak)"] += 1
elif q4 == "3":
    results["Mage (pure magic user)"] += 1

mx_key = max(results, key = lambda x: results[x])
user_class.append(mx_key)

mx_val = max(results.values())

for key, value in results.items():
    if value == mx_val:
        if key != mx_key:
            user_class.append(key)

if len(user_class) == 1:
    print(f"The style that matches you best is:\n{user_class[0]}")
elif len(user_class) > 1:
    print(f"The styles that match you best are:\n{[classes for classes in user_class]}")