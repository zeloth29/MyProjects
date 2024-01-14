NameGot = False 
def multiples():
  global NameGot
  Skip = 0
  if NameGot == False:
    StuName = ''
    StuName = input("What is your name?\n")
  NameGot = True
  table = int(input("Enter times table, start number and end number\n"))
  startnum = int(input())
  endnum = int(input())
  if endnum <= startnum:
    print("Sorry endNum must be larger than startnum. Restarting now...")
    Skip = 1
  if Skip != 1:
    print("Hey", StuName, "here is your", table, "times tables")
    while startnum <= endnum :
      print(table, "*", startnum, "=", int(table*startnum))
      startnum += 1

if NameGot == False:
  multiples()
GoAgain = input("Do you want to run again?\n")
Stop = 0
while Stop != 1:
    if GoAgain.upper() == "YES":
      multiples()
    elif GoAgain.upper() != "YES":
      print("Goodbye!")
      Stop = 1