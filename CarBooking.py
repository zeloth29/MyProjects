def proceed(x):
  if x.upper() == 'YES':
    print("Option confirmed! Have a nice day!")
  else:
    print("Option cancelled.")

CarOption = int(input("Pick a car:\n 1: Economy Car\n 2: Saloon Car\n 3: Sports Car\n"))
if CarOption == 1:
  Confirm = input("Would you like to confirm?\n")
  proceed(Confirm)
elif CarOption == 2:
  Confirm = input("Would you like to confirm?\n")
  proceed(Confirm)
elif CarOption == 3:
  Confirm = input("Would you like to confirm?\n")
  proceed(Confirm)
else:
  print("Invalid Input!")