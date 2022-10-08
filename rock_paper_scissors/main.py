import random
import time
class Game:
  RD = random.randrange(0, 3)
  CPU = ""
  print("1)Rock")
  print("2)Paper")
  print("3)Scissors")
  opcion = int(input("What do you choose?: "))

  if opcion == 1:
      Player = "rock"
  elif opcion == 2:
      Player = "paper"
  elif opcion == 3:
      Player = "scissors"
  print("you choose: ", Player)

  if RD == 0:
      CPU = "Rock"
  elif RD == 1:
      CPU = "paper"
  elif RD == 2:
      CPU = "scissors"
  print("CPU choose: ", CPU)
  time.sleep(1)
  print("...")
  if CPU == "rock" and Player == "paper":
      print("You win, paper wraps rock")
  elif CPU == "paper" and Player == "scissors":
      print("You win, scissors cut paper")
  elif CPU == "scissors" and Player == "rock":
      print("You win, rock destroys scissors")
  if CPU == "paper" and Player == "rock":
      print("You lose, paper wraps rock")
  elif CPU == "scissors" and Player == "paper":
      print("You lose, scissors cut papel")
  elif CPU == "rock" and Player == "scissors":
      print("You lose, rock destroys scissors")
  elif CPU == Player:
      print("empate")

#piedra papel o tijera