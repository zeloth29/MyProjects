
TotalVal = float(input("What is your the total value of your order?\n£"))
Guarantee = input("Do you want to pay for the Guaranteed next day delivery?\n(Y/N) > ")
Cost = 0

if TotalVal < 15:
  Cost = TotalVal + 3.50
else:
  Cost = TotalVal + Cost

if Guarantee == "Y":
  Cost= Cost + 5

print("Your total comes to " + str(Cost))
