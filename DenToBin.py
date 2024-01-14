Number = int(input("Enter a denary number"))
Bin = 0
while Number > 0:
  if Number >= 128:
    Bin = Bin + 10**7
    Number = Number - 128
  
  if Number >= 64:
    Bin = Bin + 10**6
    Number = Number - 64
  
  if Number >= 32:
    Bin = Bin + 10**5
    Number = Number - 32
  
  if Number >= 16:
    Bin = Bin + 10**4
    Number = Number - 16
  
  if Number >= 8:
    Bin = Bin + 10**3
    Number = Number - 8
  
  if Number >= 4:
    Bin = Bin + 10**2
    Number = Number - 4
  
  if Number >= 2:
    Bin = Bin + 10**1
    Number = Number - 2
  
  if Number == 1:
    Bin = Bin + 1
    Number = Number - 1
  

print(Bin)