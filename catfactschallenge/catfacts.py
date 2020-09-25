#! python3

import requests
import random

def main():
    r = requests.get("https://cat-fact.herokuapp.com/facts")
    rand_fact = random.choice(r.json().get("all"))
    print(rand_fact.get("text") + "\n")

    most_upvotes = 0
    for cat_fact in r.json().get("all"):
        upvotes = int(cat_fact.get("upvotes"))
        if upvotes > most_upvotes:
               most_upvotes = int(cat_fact.get("upvotes"))

    for cat_fact in r.json().get("all"):
        upvotes = int(cat_fact.get("upvotes"))
        if upvotes == most_upvotes:
            print(f"This cat fact has the most upvotes! --> {cat_fact.get('text')}")
            break

main()