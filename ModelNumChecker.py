part = ""
total_parts = 0
old_model_parts = 0
while part != "9999":
    part = input("Enter a 4-digit part number (enter 9999 to exit): ")
    if len(part) != 4:
        print("Invalid part number. Part number must be 4 digits.")
        continue
    total_parts += 1
    last_digit = int(part[-1])
    if last_digit in [6, 7, 8]:
        old_model_parts += 1
print("Total number of parts entered:", total_parts)
print("Number of old model parts:", old_model_parts)