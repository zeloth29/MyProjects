Num = int(input("Enter a three digit number\n"))
print("\n100s:", str(Num//100) + "00" + "\n10s:", str(Num//10%10) + "0")
print("1s:", str(Num%10))