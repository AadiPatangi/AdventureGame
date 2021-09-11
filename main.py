#Creating Interactiv Adventure
import sound
import direction

print("*****************************")
print("Welcome to The Grand Canyon Mountain Adventure Game")
print("*****************************\n")
print("You are visiting the Grand Canyon. You are going along a hike on the Hermit trail. This trail has washouts and rockslides and requires some navigation skills to find the routes. \nEnjoy COWBOY!!⛰🚶😎🤠\n")
item = input("Do you want a: \nmap(m)\nflashlight(f)\nchocolate(c)\nrope(r)\nor sticks(s):\n")

hum = input("You hear a humming sound🐦. Do you want to follow it (y,n) ?:\n")
if hum == "y":
  sound.followSound()
if hum == "n":
  sound.lost()

direction.direction()