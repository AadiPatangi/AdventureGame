
def direction():
    direct = input("What direction would you like to go🧭\nNorth(n), West(w), or South(s):\n")
    #north
    if direct == "n":
      print("*****************************")
      print("You reach the cabin🏚")
      print("*****************************")
      map = input("Want to use map🗺 (y,n):?") 
      if map == "y":
        print("*****************************")
        print("You use the map to find way.")
        print("*****************************")
        print("\nYOU WIN🎉🎈")
      if map == "n":
        print("\nStop. YOU LOSE😥")
    #west
    if direct == "w":
      print("You hurt your leg")
      ambulance = input("Want an ambulance🚑(y,n): ")
      if ambulance == "y":
        print("No ambulances in 100 mile radius🚑")
        print("*****************************")
        print("\nStop. YOU LOSE😥")
      if ambulance == "n":
        print("Poor choice. YOU LOSE😥")
    #south
    if direct == "s":
      print("You reach the highway")
      flashlight = input("\n You want a flashlight🔦(y,n): ")
      if flashlight == "y":
       print("You signal for help")
       print("\n YOU WIN🎉🎈")
      if flashlight == "n":
       print("Poor choice")
       print("\nStop. YOU LOSE😥")
