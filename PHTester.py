pH = 0
pH = int(input("Enter pH level: "))
if pH > -1 and pH < 7:
  print("pH is acidic")
else:
  if pH == 7:
    print("pH is neutral")
  else:
    if pH > 7 and pH < 15:
      print("pH is basic")
    else:
      print("Error... enter a number from 0 to 14")