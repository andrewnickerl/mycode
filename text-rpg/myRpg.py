#! python3

# I feel like the progress I made over the past two hours was very minimal 
# (my accidental 30-min deep dive on the Elder Scrolls Wiki while looking 
# for info for this app certainly didn't help). My forte is implementation,
# but the creativity piece is always very difficult and time-consuming for
# me.You can see the work I did on changing the rooms dictionary.  I plan
# build about double the current amount of rooms and having the player be 
# able to equip each tier of sword in the sword list, until they eventually
# have a daedric sword and can face the final boss at the top of the Imperial
# Tower.  I'll also be adding custom, room-specific messages for each room so
# that the player understands the context and progression.

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
equipped = []
swords = ['iron', 'steel', 'orcish', 'elven', 'ebony', 'daedric']

#a dictionary linking a room to other rooms
rooms = {

            'Cell' : { 
                  'up' : 'Lower Ramp',
                  'sword' : 'iron'
                },
            'Lower Ramp' : {
                  'down' : 'Cell',
                  'up' : 'Bloodworks',
                  'enemy' : 'skeever'
                },
            'Bloodworks' : {
                'left' : 'Preparation Room',
                'right' : 'Practice Room',
                'down' : 'Pantry'
                },
            'Practice Room' : {
                'sword': 'steel',
                'left' : 'Bloodworks'
                },
            'Preparation Room' : {
                'right' : 'Bloodworks',
                'up' : 'Upper Ramp'
                },
            'Upper Ramp' : {
                'down' : 'Preparation Room',
                'up' : 'Arena'                
                },
            'Arena' : {
                'down' : 'Upper Ramp',
                'enemy' : 'orc gladiator',
                'right' : 'Imperial Tower Courtyard'
                },
            'Imperial Tower Courtyard' : {
                'left' : 'Arena',
                'up' : 'Entry Room',
                'enemy' : 'clannfear'
                },
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
  
  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' sword equipped!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
