import time
print("You have to type the alphabet in correct order you will be timed.")
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter = "0"
counter = 0
game = 0
Start = 0
while letter != alphabet[25] and game == 0:
  if letter == "0":
    input("press enter to start")
    Start = time.time()
    print("Timer started")
    letter = input()
  if letter.upper() == alphabet[counter].upper():
    letter = input("Correct! Next letter!\n")
  else:
    print("Incorrect")
    game = 1
  counter += 1
end = time.time()
if game == 1:
  print("You lose!")
else:
  print("Well done! You won!")
print("That was", round((end - Start),1), "seconds")

# HSr = open("HighscoreFile.txt", "r")
# if float(HSr.readline(1)) > round((end - Start),1):
#   oldhs = HSr.read(1)
#   print(oldhs)