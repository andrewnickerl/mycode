#! python3

easy= ["science", "turbo", ["goggles", "eyes"], "nothing"]


medium= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


hard= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

print(f'{easy[2][1]} {easy[2][0]} {easy[-0]}')
print(f'{medium[2]["goggles"]} {medium[2]["eyes"]} {medium[-0]}')
print(f'{hard[0]["user"]["name"]["first"]} {hard[0]["kumquat"]} {hard[0]["d"]}')
