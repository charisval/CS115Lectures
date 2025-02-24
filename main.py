import pygame

age = 15
age2 = 15

if age > 21:
  print("you are an adult")
  print("You are old")
else:
  print("You are young")

# if/elif statements
difference = age - age2
if difference > 0:
  print("positive")
elif difference > 5:
  print("Big number")
elif difference < 0:
  print("negative")
elif difference == 0:
  print("no difference")

# while loop
counter = 0
while counter <= 10:
  print(counter)
  counter += 1
  # increment counter by 1

# for loop
inventory = ["sword", "shield", "key"]
for item in inventory:
  print(item)

# boolean operators
# True/False should be capitalized
is_game_paused = False
is_dead = True
# only one variable has to evaluate as True
if is_game_paused or is_dead:
  print('game paused')
else:
  print("game not paused")
# both variables have to evaluate as True
if is_game_paused and is_dead:
  print("game over")

health = 50
if health <= 0:
  is_dead = True

break
# used in order to break a loop

while not
# runs when a boolean value is False