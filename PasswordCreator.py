for attempts in range (1,4):
  Password = "Tues1212"
  if attempts == 1:
    UserInput = str(None)
  UserInput = input("Enter the password, you're on " + str(attempts) + "/3 attempts\n>")
  if UserInput == Password:
    print("Password Accepted.")
    break
  elif attempts == 3:
    print("Too many attempts. Try again later.")
  else:
    print("Password Rejected.")