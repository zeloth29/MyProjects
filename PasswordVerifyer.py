def getPword():
  password = 'abc'
  attempts = 0
  success = 0
  while (len(password) <= 6 and len(password) >= 8) or success != 1:
    password = input("Enter your password\n")
    if len(password) < 6 or len(password) > 8:
      print("Error. Password must be 6 to 8 characters long")
      attempts += 1
    if (len(password) >= 6 and len(password) <= 8):
      Re_password = input("Re-enter your password.\n")
      if Re_password == password:
        success = 1
      else:
        attempts += 1
        print("Error passwords do not match!")
  print("Success! Password changed!")
  Check = input("What is your password?")
  if Check == password:
    print("Welcome!")
  else:
    Again = input("Would you like to reset your password?")
    if Again.upper == "YES":
      getPword()
    else:
      print("Alright! Bye!")
while True:
  getPword()