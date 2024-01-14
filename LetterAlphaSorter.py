letters = []
for i in range(5):
  if i == 0:
    print(
      "Im going to ask you for 5 lowercase letters (Press enter each letter)and i will sort them."
    )
  letter = input("Enter a lowercase letter: ")
  letters.append(letter)
letters.sort(reverse=True)
output = ''.join(letters)
print("The letters from highest to lowest is " + output)