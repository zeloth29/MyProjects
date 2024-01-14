def evenNum(n):
  n = n + evenNum(n - 2) if n > 1 and n % 2 == 0 else n + 0
  return n
Number = int(input("Enter your even number.\n\n"))
print("\nThe sum of all the even numbers between that and 0 is " + str(evenNum(Number)))