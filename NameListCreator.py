black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"
names=["","","","","","","","","",""]
global Quit
Quit = 0
def DisplayMenu(Num):
  while (Num < 1 or Num <= 3):
    if Num == 1:
      name = input("\nEnter the name to be added to the list.\n>")
      namepos = int(input("\nEnter the position you want to enter the name into 1-10\n>"))
      if namepos < 1 or namepos > 10:
        print(red + "\nSorry number must be 1-10. Retry"+ bright_white)
        continue
      names[namepos-1] = name
      Num = 123654
    if Num == 2:
      for i in range(10):
        if i == 0:
          print("\n Here is your list:")
        print(str(i+1) + ": " + names[i])
      Num = 123654
    if Num == 3:
      global Quit
      Quit = 1
      print("\nGoodbye!")
      Num = 123654
    if (Num < 1 or Num > 3) and Num != 123654:
      Num = int(input(blue + "Please pick a option 1,2 or 3."+ white))

while 1 == 1 and Quit != 1:
  Choice = int(input(blue + "\nWhat would you like to do?"+ bright_white +"\n1: Add name\n2: Display list\n3: Quit\n\n>"))
  DisplayMenu(Choice)
