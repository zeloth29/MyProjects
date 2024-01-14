Temp = input("Do you have a temperature?(yes/no)\n")

if Temp.upper() == "YES":
  throat = input("Do you have a sore throat(yes/no)\n")
  if throat.upper() == "YES":
    print("You may have a throat Infection.")
  else:
    cough = input("Do you have a cough?(yes/no)\n")
    if cough.upper() == "YES":
      print("You have a chest infection.")
    else:
      print("You have a fever.")
else:
  print("You're fine.")