
def followSound():
    print("*****************************")
    print("You keep moving closer to the sound. The sound suddenly stops!!.\nYOU ARE NOW LOST!!\nYou try to call on you phone but there is no signal📵!!")
    print("*****************************")
def lost():
    print("*****************************")
    print("You start walking back to the starting point. You realize that you are LOST. The sound is behind you and is getting louder.\nPANIC!!!!\n")
    print("*****************************")
    action = input("\nDo you want to run(r) or make a call(c): ") 
    while action == "c":
      print("The call did not go through📵")   
      action = input ("Do you want to call again(c) or make a run(r): ")
    if action == "r":
      print("\n You are running fast and the sound gets really loud " )
