#! python3

stars = ""
iterations = int(input("How many lines do you want in the pattern? "))
for i in range(iterations):
    if i < iterations / 2:
        stars += "*"
    elif i >= iterations / 2:
        stars = stars[:-1]
    print(stars)
